import logging
import os
from datetime import datetime

from pytz import timezone

import fileutils
import paho.mqtt.client as paho
import redis
from paho.mqtt.enums import CallbackAPIVersion

PERMITTED_FILE: str = os.environ.get('PERMITTED_FILE')  # type: ignore
TZ: str = os.environ.get('TZ')  # type: ignore

MQTT_CLIENT_ID: str = os.environ.get('CLIENT_ID')  # type: ignore
MQTT_HOST: str = os.environ.get('HOST')  # type: ignore
MQTT_USERNAME: str = os.environ.get('USERNAME')  # type: ignore
MQTT_PASSWORD: str = os.environ.get('PASSWORD')  # type: ignore


logging.basicConfig(level=logging.DEBUG)

r = redis.Redis.from_url('redis://redis:6379', decode_responses=True)


class Steamid64ExistsError(Exception):
    ...


def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f'CONNACK received with code {rc}.')


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    logging.info(f'Subscribed: {str(mid)} {str(granted_qos)}')


def on_message(client, userdata, msg):
    logging.info(f'{msg.topic} {str(msg.qos)} {str(msg.payload)}')
    now = datetime.now(tz=timezone(TZ))

    try:
        steamid64 = str(msg.payload.decode())
        succ = r.hsetnx(
            name=f'permittedlist:{steamid64}',
            key='create_date',
            value=now.isoformat(),
        )

        if succ == 0:
            raise Steamid64ExistsError

        fileutils.append_row(PERMITTED_FILE, steamid64)
    except Exception as exc:
        logging.exception(exc)


mqtt_client = paho.Client(
    client_id=MQTT_CLIENT_ID,
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
    logging.info('Caught an Exception, something went wrong...')
    logging.exception(exc)
finally:
    logging.info('Disconnecting from the MQTT broker')
    mqtt_client.disconnect()
