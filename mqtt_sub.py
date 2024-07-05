import logging
import os

import paho.mqtt.client as paho
from paho.mqtt.enums import CallbackAPIVersion

import permittedlist

CLIENT_ID: str = os.environ.get('CLIENT_ID')  # type: ignore
PERMITTED_FILE: str = os.environ.get('PERMITTED_FILE')  # type: ignore
MQTT_HOST: str = os.environ.get('MQTT_HOST')  # type: ignore
MQTT_USERNAME: str = os.environ.get('MQTT_USERNAME')  # type: ignore
MQTT_PASSWORD: str = os.environ.get('MQTT_PASSWORD')  # type: ignore

logging.basicConfig(level=logging.DEBUG)


def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f'CONNACK received with code {rc}.')


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    logging.info(f'Subscribed: {str(mid)} {str(granted_qos)}')


def on_message(client, userdata, msg):
    logging.info(f'{msg.topic} {str(msg.qos)} {str(msg.payload)}')

    try:
        payload = str(msg.payload.decode())
        permittedlist.append(PERMITTED_FILE, payload)
    except Exception:
        pass


client = paho.Client(
    client_id=CLIENT_ID,
    userdata=None,
    protocol=paho.MQTTv5,
    callback_api_version=CallbackAPIVersion.VERSION2,
)

client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)  # type: ignore
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_HOST, 8883)

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.subscribe('steamid/#', qos=1)

try:
    logging.info('Press CTRL+C to exit...')
    client.loop_forever()
except Exception:
    logging.info('Caught an Exception, something went wrong...')
finally:
    logging.info('Disconnecting from the MQTT broker')
    client.disconnect()
