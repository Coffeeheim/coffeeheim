import { AutoRouter } from "itty-router";
import html from "./index.html";

const router = AutoRouter();

router.get("/", () => {
  return new Response(html, {
    headers: {
      "Content-Type": "text/html;charset=UTF-8",
    },
  });
});

export default { ...router };
