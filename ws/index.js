addEventListener('fetch', (event) => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  if (request.headers.get('Upgrade') !== 'websocket') {
    return new Response('Expected websocket', { status: 400 })
  }

  const [client, server] = Object.values(new WebSocketPair())

  server.accept()
  server.addEventListener('message', async ({ data }) => {
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
