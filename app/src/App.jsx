import { ReactComponent as Discordsvg } from './discord.svg'
import coffeeheim from './coffeeheim-512x512.webp'

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

function Rules() {
  return (
    <div className="space-y-2.5">
      <h2 className="font-semibold text-2xl">Rules</h2>

      <ul className="list-decimal list-inside">
        <li>It's prohibited to destroy constructions; improve them instead.</li>
        <li>Don't steal items from other players; be kind and ask first.</li>
        <li>
          You can use existing characters, but don't bring items from another
          server. Think of it as starting fresh in a new world.
        </li>
        <li>
          If someone asks for help to defeat a creature, the dropped items
          belong to the player who asked for help, even if they did the least
          part.
        </li>
      </ul>
    </div>
  )
}

function Submit() {
  return (
    <form
      action="#"
      className="border bg-gray-50 p-5 space-y-2.5 rounded-md lg:w-2/4"
      method="post"
    >
      <p class="bg-yellow-100 p-2 border border-yellow-400">
        If you would like to join us on Valheim, submit the following form.
      </p>

      <div>
        <label className="space-y-0.5">
          <div>
            Your steamID64, customURL or complete URL
            <span className="text-sm">
              (
              <a
                href="https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC"
                className="text-indigo-600 underline hover:no-underline"
                target="_blank"
                rel="noreferrer"
              >
                ?
              </a>
              )
            </span>
          </div>
          <input
            name="steamid"
            className="border border-gray-400 p-2 rounded w-full"
          />
        </label>
      </div>

      <button className="py-2 px-4 text-white bg-indigo-600 rounded">
        Submit
      </button>
    </form>
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
        <Submit />
        <div className="space-y-2.5">
          <h3 className="font-semibold text-2xl">
            Check out what our community is up to!
          </h3>
          <iframe
            className="w-full aspect-video"
            src="https://www.youtube.com/embed/2RQA8WurZlI?si=f8_YGAiRr0ZrYyMM&amp;controls=0"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          />
        </div>
      </section>
    </div>
  )
}

export default App
