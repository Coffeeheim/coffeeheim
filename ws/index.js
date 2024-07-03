async function handleRequest(request) {
  const upgradeHeader = request.headers.get('Upgrade')

  if (!upgradeHeader || upgradeHeader !== 'websocket') {
    return new Response('Expected websocket', { status: 426 })
  }

  const [client, server] = Object.values(new WebSocketPair())
  server.accept()

  server.addEventListener('message', async ({ data }) => {
    console.log(data)
    server.send(JSON.stringify({ tz: new Date() }))
  })

  server.addEventListener('close', async (event) => {
    console.log(event)
  })

  return new Response(null, {
    status: 101,
    webSocket: client,
  })
}

export default handleRequest
