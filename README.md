# Amazon clients for Crawlora

Official Crawlora client packages for the hosted Amazon API. Access 5 API endpoints covering product search, suggestions, product details, and chart/category discovery from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape Amazon locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Amazon or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/amazon`](javascript/README.md)
- Python: [`crawlora-amazon`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-amazon`](go.mod)
- Ruby: [`crawlora-amazon`](ruby/README.md)
- Java: [`net.crawlora:crawlora-amazon:0.1.3`](java/README.md)
- PHP: [`crawlora/amazon`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 5 selected public Amazon API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/amazon/charts` | `amazon-charts` | Amazon product charts |
| `GET` | `/amazon/charts/categories` | `amazon-charts-categories` | Amazon chart categories |
| `GET` | `/amazon/product/{asin}` | `amazon-product` | Retrieve Amazon product details |
| `GET` | `/amazon/search` | `amazon-search` | Search Amazon products |
| `GET` | `/amazon/suggest/{keyword}` | `amazon-suggest` | Retrieve Amazon search suggestions |

## License

MIT. See [LICENSE](LICENSE).
