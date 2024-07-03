// export function onRequest(request) {
//   const upgradeHeader = request.headers.get('Upgrade')
//   if (!upgradeHeader || upgradeHeader !== 'websocket') {
//     return new Response('Expected Upgrade: websocket', { status: 426 })
//   }

//   const webSocketPair = new WebSocketPair()
//   const [client, server] = Object.values(webSocketPair)

//   server.accept()

//   return new Response(null, {
//     status: 101,
//     webSocket: client,
//   })
// }

export function onRequest(context) {
  return new Response('Hello, world!')
}
