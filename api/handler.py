from http import HTTPStatus

import paho.mqtt.client as paho
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from paho.mqtt.enums import CallbackAPIVersion
from pydantic import BaseModel, HttpUrl

import mqtt_pub
import steamid
from configs import MQTT_HOST, MQTT_PASSWORD, MQTT_USERNAME

logger = Logger()
app = LambdaFunctionUrlResolver(enable_validation=True)
mqtt_client = paho.Client(
    protocol=paho.MQTTv5,
    callback_api_version=CallbackAPIVersion.VERSION2,
)
mqtt_client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)  # type: ignore
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_HOST, 8883)


class Payload(BaseModel):
    steamid: str | HttpUrl


@app.post('/')
def index(payload: Payload):
    steamid_64 = steamid.get_steamid_64(str(payload.steamid))

    succ = mqtt_pub.publish(
        topic='steamid',
        payload=steamid_64,
        mqtt_client=mqtt_client,
    )
    logger.info('Published on steamid', succ)

    return {}, HTTPStatus.CREATED


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL
)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
