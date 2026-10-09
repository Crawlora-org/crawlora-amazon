# Amazon client usage

The `@crawlora-org/amazon` and `crawlora-amazon` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Amazon locally; Crawlora is independent from and not endorsed by Amazon or its owners.

The package tracks the public API contract revision `sha256:ccae432eea9beb55dab5108c0f607d20edb7b2a7ee7746836139bea73f70e547` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 5 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `amazon` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `charts` / `charts` | `GET /amazon/charts` | `chart` (query, required; values: `best_sellers`, `new_releases`, `most_wished_for`), `department` (query, required), `node` (query, optional), `page` (query, optional) | Amazon product charts |
| `chartsCategories` / `charts_categories` | `GET /amazon/charts/categories` | `chart` (query, required; values: `best_sellers`, `new_releases`, `most_wished_for`), `department` (query, optional), `node` (query, optional) | Amazon chart categories |
| `product` / `product` | `GET /amazon/product/{asin}` | `asin` (path, required), `language` (query, optional; values: `en_US`), `currency` (query, optional; values: `USD`) | Retrieve Amazon product details |
| `search` / `search` | `GET /amazon/search` | `k` (query, required), `s` (query, optional), `page` (query, optional) | Search Amazon products |
| `suggest` / `suggest` | `GET /amazon/suggest/{keyword}` | `keyword` (path, required) | Retrieve Amazon search suggestions |

## Client forms

- JavaScript: import `AmazonClient` (also exported as `Client`) from `@crawlora-org/amazon`; use `new AmazonClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `AmazonClient` (also exported as `Client`) from `crawlora_amazon`; use `with AmazonClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncAmazonClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
