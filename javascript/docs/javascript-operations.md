# Crawlora Amazon JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amazon | `amazon.charts` | `amazon-charts` | `GET /amazon/charts` | `chart` (query "best_sellers" \| "new_releases" \| "most_wished_for" required)<br>`department` (query string required)<br>`node` (query string)<br>`page` (query number) | `ApiKeyAuth` | `AmazonChartsResponse` |  |
| amazon | `amazon.chartsCategories` | `amazon-charts-categories` | `GET /amazon/charts/categories` | `chart` (query "best_sellers" \| "new_releases" \| "most_wished_for" required)<br>`department` (query string)<br>`node` (query string) | `ApiKeyAuth` | `AmazonChartsCategoriesResponse` |  |
| amazon | `amazon.product` | `amazon-product` | `GET /amazon/product/{asin}` | `asin` (path string required)<br>`language` (query "en_US")<br>`currency` (query "USD") | `ApiKeyAuth` | `AmazonProductResponse` |  |
| amazon | `amazon.search` | `amazon-search` | `GET /amazon/search` | `k` (query string required)<br>`s` (query string)<br>`page` (query number) | `ApiKeyAuth` | `AmazonSearchResponse` |  |
| amazon | `amazon.suggest` | `amazon-suggest` | `GET /amazon/suggest/{keyword}` | `keyword` (path string required) | `ApiKeyAuth` | `AmazonSuggestResponse` |  |
