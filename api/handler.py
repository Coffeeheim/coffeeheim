import paho.mqtt.client as paho
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from paho.mqtt.enums import CallbackAPIVersion

import mqtt_pub
import steamid
from configs import MQTT_HOST, MQTT_PASSWORD, MQTT_USERNAME

tracer = Tracer()
logger = Logger()
app = LambdaFunctionUrlResolver()
mqtt_client = paho.Client(
    protocol=paho.MQTTv5,
    callback_api_version=CallbackAPIVersion.VERSION2,
)
mqtt_client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)  # type: ignore
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_HOST, 8883)


@app.get('/')
@tracer.capture_method
def index():
    mqtt_pub.publish(
        payload=str(steamid.get_steamid_64('sergiors')),
        mqtt_client=mqtt_client,
    )

    return {}


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL
)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
