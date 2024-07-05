import { ReactComponent as Discordsvg } from './discord.svg'
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

function App() {
  return (
    <div className="max-w-screen-md mx-auto">
      <header className="mb-5 space-y-2 md:flex justify-between">
        <div className="flex">
          <div className="w-12 h-12 mr-2.5 rounded-lg bg-gray-100 overflow-hidden">
            <img src={coffeeheim} alt="Coffeeheim" title="Coffeeheim" />
          </div>
          <h1 className="font-bold text-5xl">Coffeeheim</h1>
          <div>
            <span className="bg-green-600 text-white text-xs py-0.5 px-1 rounded-full">
              24/7
            </span>
          </div>
        </div>
        <Discord />
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
            src="https://www.youtube.com/embed/2RQA8WurZlI?si=f8_YGAiRr0ZrYyMM&amp;controls=0"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
            allowFullScreen
          />
        </div>
      </section>
    </div>
  )
}

export default App
