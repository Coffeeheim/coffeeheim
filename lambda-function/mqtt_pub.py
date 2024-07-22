from paho.mqtt.client import PayloadType


def publish(payload: PayloadType, *, topic: str, mqtt_client) -> bool:
    succ, _ = mqtt_client.publish(topic, payload, qos=1)
    return succ == 0
