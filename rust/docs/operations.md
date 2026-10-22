# Crawlora Amazon Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amazon | `amazon.charts` | `amazon-charts` | `GET /amazon/charts` | `chart` (query String enum{best_sellers, new_releases, most_wished_for} required)<br>`department` (query String required)<br>`node` (query String)<br>`page` (query i64) | `ApiKeyAuth` | `AmazonChartsResponse` |  |
| amazon | `amazon.charts_categories` | `amazon-charts-categories` | `GET /amazon/charts/categories` | `chart` (query String enum{best_sellers, new_releases, most_wished_for} required)<br>`department` (query String)<br>`node` (query String) | `ApiKeyAuth` | `AmazonChartsCategoriesResponse` |  |
| amazon | `amazon.product` | `amazon-product` | `GET /amazon/product/{asin}` | `asin` (path String required)<br>`language` (query String enum{en_US})<br>`currency` (query String enum{USD}) | `ApiKeyAuth` | `AmazonProductResponse` |  |
| amazon | `amazon.search` | `amazon-search` | `GET /amazon/search` | `k` (query String required)<br>`s` (query String)<br>`page` (query i64) | `ApiKeyAuth` | `AmazonSearchResponse` |  |
| amazon | `amazon.suggest` | `amazon-suggest` | `GET /amazon/suggest/{keyword}` | `keyword` (path String required) | `ApiKeyAuth` | `AmazonSuggestResponse` |  |
