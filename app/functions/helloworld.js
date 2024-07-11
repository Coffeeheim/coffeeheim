import mqtt from 'mqtt'

const MQTT_HOST = process.env.MQTT_HOST
const MQTT_USERNAME = process.env.MQTT_USERNAME
const MQTT_PASSWORD = process.env.MQTT_PASSWORD

const client = mqtt.connect(MQTT_HOST, {
  username: MQTT_USERNAME,
  password: MQTT_PASSWORD,
})

export function onRequest(context) {
  client.publish('cluster/messages/node7', 'Hello, HiveMQ!')
  return new Response('Hello, world!')
}
