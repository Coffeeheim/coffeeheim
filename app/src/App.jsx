import { ReactComponent as Discordsvg } from './discord.svg'
import { ReactComponent as Kovisvg } from './kofi.svg'
import coffeeheim from './coffeeheim-512x512.webp'
import Form from './Form'
import Rules from './Rules'

function Discord() {
  return (
    <a
      href="https://discord.gg/7EJpbgFvXd"
      className="inline-flex gap-2 bg-gray-50 hover:bg-gray-100 border rounded-lg p-2"
    >
      <Discordsvg className="h-6" />
      Join us on Discord
    </a>
  )
}

function Kofi() {
  return (
    <a
      href="https://ko-fi.com/coffeeheim"
      className="inline-flex gap-2 bg-red-50 hover:bg-red-100 border border-red-200 rounded-lg p-2"
    >
      <Kovisvg className="fill-red-500 h-6" />
      Donate to the server
    </a>
  )
}

function App() {
  return (
    <div className="max-w-screen-md mx-auto">
      <header className="mb-5 space-y-2 md:flex justify-between">
        <div className="flex">
          <div className="w-12 h-12 mr-2.5 rounded-lg bg-gray-100 overflow-hidden">
            <img src={coffeeheim} alt="Coffeeheim" title="Coffeeheim" />
          </div>
          <h1 className="font-bold text-5xl">Coffeeheim</h1>
        </div>

        <div className="flex gap-2">
          <Discord />
          <Kofi />
        </div>
      </header>

      <section className="space-y-2.5">
        <Rules />
        <Form />
        <div className="space-y-2.5">
          <h3 className="font-semibold text-2xl">
            Check out what our community is up to!
          </h3>
          <iframe
            className="w-full aspect-video"
            src="https://www.youtube.com/embed/IAvt_V4rCa8?si=mxgF3uW9NmHFa0t-&amp;controls=0"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
            allowFullScreen
          />
        </div>
      </section>

      <section className="mt-4 bg-gray-100 px-4 py-2.5 rounded">
        <div className="flex justify-between">
          <span>&copy; {new Date().getFullYear()} Coffeeheim</span>
          <ul className="flex gap-2.5 text-indigo-500">
            <li>
              <a
                href="https://github.com/sergiors/coffeeheim"
                className="underline hover:no-underline"
              >
                GitHub
              </a>
            </li>
            <li>
              <a
                href="https://uptime.coffeeheim.com"
                className="underline hover:no-underline"
              >
                Status
              </a>
            </li>
          </ul>
        </div>
      </section>
    </div>
  )
}

export default App
