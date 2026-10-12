# @crawlora-org/amazon — Amazon API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Amazon API.
It exposes 5 API endpoints for product search, suggestions, product details, and chart/category discovery through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-javascript-homepage). It does not run a browser or scrape Amazon locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Amazon or its owners.

## Install

```sh
npm install @crawlora-org/amazon
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { AmazonClient } from "@crawlora-org/amazon";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AmazonClient({ apiKey });
const result1 = await client.search({ k: "wireless headphones" });
console.log(result1);
const result2 = await client.suggest({ keyword: "wireless headphones" });
console.log(result2);
```

The client also exports `Client` as an alias for `AmazonClient`. Operation
methods are available directly in camelCase and through the `amazon`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-amazon/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Amazon API endpoints

This package exposes each route below as a direct method and through the `amazon` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/amazon/charts` | `amazon-charts` | Amazon product charts |
| `GET` | `/amazon/charts/categories` | `amazon-charts-categories` | Amazon chart categories |
| `GET` | `/amazon/product/{asin}` | `amazon-product` | Retrieve Amazon product details |
| `GET` | `/amazon/search` | `amazon-search` | Search Amazon products |
| `GET` | `/amazon/suggest/{keyword}` | `amazon-suggest` | Retrieve Amazon search suggestions |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
