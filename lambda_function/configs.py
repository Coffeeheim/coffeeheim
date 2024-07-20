import os

MQTT_HOST: str = os.environ.get('MQTT_HOST')  # type: ignore
MQTT_USERNAME: str = os.environ.get('MQTT_USERNAME')  # type: ignore
MQTT_PASSWORD: str = os.environ.get('MQTT_PASSWORD')  # type: ignore
