# Crawlora Amazon API client for PHP (`crawlora/amazon`)

This PHP package calls Crawlora's hosted Amazon API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering product search, suggestions, product details, and chart/category discovery. It does not call or scrape Amazon directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/amazon
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Amazon\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("amazon-search", ['k' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 5 API operations.

## Supported Amazon API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/amazon/charts` | `amazon-charts` | Amazon product charts |
| `GET` | `/amazon/charts/categories` | `amazon-charts-categories` | Amazon chart categories |
| `GET` | `/amazon/product/{asin}` | `amazon-product` | Retrieve Amazon product details |
| `GET` | `/amazon/search` | `amazon-search` | Search Amazon products |
| `GET` | `/amazon/suggest/{keyword}` | `amazon-suggest` | Retrieve Amazon search suggestions |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-amazon). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md).
