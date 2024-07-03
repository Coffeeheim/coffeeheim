import { AutoRouter } from 'itty-router'
import html from './index.html'

const router = AutoRouter()

router.get('/', () => {
  return new Response(html, {
    headers: {
      'content-type': 'text/html;charset=UTF-8',
    },
  })
})

router.get('/ws', (req) => {
  if (req.headers.get('Upgrade') !== 'websocket') {
    return new Response('Expected websocket', { status: 400 })
  }

  const [client, websocket] = Object.values(new WebSocketPair())

  websocket.accept()

  websocket.send(JSON.stringify({ connected: true }))

  websocket.addEventListener('message', async ({ data }) => {
    websocket.send(JSON.stringify({ data }))
  })

  websocket.addEventListener('close', async (e) => {
    console.log(e)
  })

  return new Response(null, {
    status: 101,
    webSocket: client,
  })
})

export default { ...router }
