from paho.mqtt.client import PayloadType


def publish(payload: PayloadType, *, mqtt_client) -> bool:
    msg = mqtt_client.publish('steamid', payload, qos=1)
    return msg.is_published()
