import mqtt from 'mqtt'

export function onRequest({ request, env }) {
  const MQTT_HOST = env.MQTT_HOST
  const MQTT_USERNAME = env.MQTT_USERNAME
  const MQTT_PASSWORD = env.MQTT_PASSWORD

  // const client = mqtt.connect(MQTT_HOST, {
  //   username: MQTT_USERNAME,
  //   password: MQTT_PASSWORD,
  // })

  // client.publish('cluster/messages/node7', 'Hello, HiveMQ!')
  return new Response('Hello,!')
}
