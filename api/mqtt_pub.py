from paho.mqtt.client import PayloadType


def publish(payload: PayloadType, *, mqtt_client) -> bool:
    succ, _ = mqtt_client.publish('steamid', payload, qos=1)
    return succ == 0
