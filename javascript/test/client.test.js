import test from "node:test";
import assert from "node:assert/strict";
import {
  AmazonClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new AmazonClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["amazon"]);
  assert.equal(typeof client["charts"], "function");
  assert.equal(typeof client["amazon"]["charts"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new AmazonClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"});
  assert.match(seen.url, /\/amazon\/charts/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-amazon-js/0.1.1");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new AmazonClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new AmazonClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new AmazonClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new AmazonClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}), CrawloraClientError);
  const down = new AmazonClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new AmazonClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new AmazonClient({ fetch: hanging });
  const pending = aborted.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});
