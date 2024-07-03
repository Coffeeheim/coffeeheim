import { Router } from "itty-router";
import html from "./index.html";

const router = Router();

router.get("/", () => {
  return new Response(html, {
    headers: {
      "Content-Type": "text/html;charset=UTF-8",
    },
  });
});

router.all("*", () => {
  return new Response("404, not found!", { status: 404 });
});

addEventListener("fetch", (e) => {
  e.respondWith(router.handle(e.request));
});
