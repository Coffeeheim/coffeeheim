import logging
import os
import sqlite3
from contextlib import closing

import paho.mqtt.client as paho
from paho.mqtt.enums import CallbackAPIVersion

import fileutils
import sqlite3utils

CLIENT_ID: str = os.environ.get('CLIENT_ID')  # type: ignore
SQLITE_FILE: str = os.environ.get('SQLITE_FILE')  # type: ignore
SQLITE_TABLE: str = os.environ.get('SQLITE_TABLE')  # type: ignore
PERMITTED_FILE: str = os.environ.get('PERMITTED_FILE')  # type: ignore

MQTT_HOST: str = os.environ.get('MQTT_HOST')  # type: ignore
MQTT_USERNAME: str = os.environ.get('MQTT_USERNAME')  # type: ignore
MQTT_PASSWORD: str = os.environ.get('MQTT_PASSWORD')  # type: ignore

logging.basicConfig(level=logging.DEBUG)


def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f'CONNACK received with code {rc}.')

    with closing(sqlite3.connect(SQLITE_FILE)) as conn:
        sqlite3utils.create_table(table_name=SQLITE_TABLE, conn=conn)


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    logging.info(f'Subscribed: {str(mid)} {str(granted_qos)}')


def on_message(client, userdata, msg):
    logging.info(f'{msg.topic} {str(msg.qos)} {str(msg.payload)}')

    with closing(sqlite3.connect(SQLITE_FILE)) as conn:
        try:
            payload = str(msg.payload.decode())
            sqlite3utils.write_row(
                table_name=SQLITE_TABLE,
                rowdict={'steamid64': payload},
                conn=conn,
            )
            fileutils.append_row(PERMITTED_FILE, payload)
        except Exception as exc:
            logging.error(str(exc))


mqtt_client = paho.Client(
    client_id=CLIENT_ID,
    userdata=None,
    protocol=paho.MQTTv5,
    callback_api_version=CallbackAPIVersion.VERSION2,
)

mqtt_client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)  # type: ignore
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_HOST, 8883)

mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_message = on_message

mqtt_client.subscribe('steamid/#', qos=1)

try:
    logging.info('Press CTRL+C to exit...')
    mqtt_client.loop_forever()
except Exception as exc:
    logging.exception(exc)
    logging.info('Caught an Exception, something went wrong...')
finally:
    logging.info('Disconnecting from the MQTT broker')
    mqtt_client.disconnect()
