# Crawlora Amazon API client for Ruby (`crawlora-amazon`)

This Ruby gem calls Crawlora's hosted Amazon API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering product search, suggestions, product details, and chart/category discovery; it does not call or scrape Amazon directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-amazon"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/amazon"

client = Crawlora::Amazon::Client.new
result = client.request("amazon-search", JSON.parse("{\"k\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 5 API operations.

```ruby
client = Crawlora::Amazon::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Amazon API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/amazon/charts` | `amazon-charts` | Amazon product charts |
| `GET` | `/amazon/charts/categories` | `amazon-charts-categories` | Amazon chart categories |
| `GET` | `/amazon/product/{asin}` | `amazon-product` | Retrieve Amazon product details |
| `GET` | `/amazon/search` | `amazon-search` | Search Amazon products |
| `GET` | `/amazon/suggest/{keyword}` | `amazon-suggest` | Retrieve Amazon search suggestions |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-amazon) for account setup, the API operation reference, and release history.
