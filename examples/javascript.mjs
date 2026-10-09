import { AmazonClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AmazonClient({ apiKey });

  const search = await client.search({ k: "wireless headphones" });
  console.log("search", search);
  const suggest = await client.suggest({ keyword: "wireless headphones" });
  console.log("suggest", suggest);
