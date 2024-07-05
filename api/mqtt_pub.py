from paho.mqtt.client import MQTTMessageInfo, PayloadType


def publish(payload: PayloadType, *, mqtt_client) -> MQTTMessageInfo:
    return mqtt_client.publish('steamid', payload, qos=1)
