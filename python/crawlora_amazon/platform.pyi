from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelAmazonSuggestResponseDoc = TypedDict('ModelAmazonSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[str]],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonSearchResponseDoc = TypedDict('ModelAmazonSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAmazonSearchResponseItem]],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonSearchResponseItem = TypedDict('ModelAmazonSearchResponseItem', {
    'asin': NotRequired[str],
    'image': NotRequired[str],
    'is_free_delivery': NotRequired[bool],
    'is_sponsored': NotRequired[bool],
    'link': NotRequired[str],
    'list_price': NotRequired[float],
    'more_choice': NotRequired[str],
    'number_of_bought_in_last_month': NotRequired[int],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelAmazonProductResponseDoc = TypedDict('ModelAmazonProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAmazonProduct],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonProduct = TypedDict('ModelAmazonProduct', {
    'about': NotRequired[str],
    'asin': NotRequired[str],
    'availability': NotRequired[bool],
    'brand_link': NotRequired[str],
    'brand_name': NotRequired[str],
    'customers_say': NotRequired[str],
    'description': NotRequired[str],
    'images': NotRequired[list[str]],
    'is_free_delivery': NotRequired[bool],
    'is_free_return': NotRequired[bool],
    'link': NotRequired[str],
    'low_confidence': NotRequired[bool],
    'number_of_bought_in_last_month': NotRequired[int],
    'overview': NotRequired[dict[str, str]],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'rating_hist': NotRequired[dict[str, float]],
    'review_count': NotRequired[int],
    'review_images': NotRequired[list[ModelAmazonReviewImage]],
    'review_insights': NotRequired[list[ModelAmazonReviewInsight]],
    'reviews': NotRequired[list[ModelAmazonReview]],
    'seller_link': NotRequired[str],
    'seller_name': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelAmazonReview = TypedDict('ModelAmazonReview', {
    'content': NotRequired[str],
    'country': NotRequired[str],
    'helpful_count': NotRequired[int],
    'link': NotRequired[str],
    'rating': NotRequired[float],
    'review_date': NotRequired[str],
    'title': NotRequired[str],
    'user_link': NotRequired[str],
    'user_name': NotRequired[str],
    'verified_purchase': NotRequired[bool],
}, total=False)

ModelAmazonReviewInsight = TypedDict('ModelAmazonReviewInsight', {
    'label': NotRequired[str],
    'mention_percent': NotRequired[int],
    'mentions': NotRequired[int],
    'sentiment': NotRequired[str],
    'summary': NotRequired[str],
}, total=False)

ModelAmazonReviewImage = TypedDict('ModelAmazonReviewImage', {
    'review_id': NotRequired[str],
    'thumbnail': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAmazonChartCategoriesResponseDoc = TypedDict('ModelAmazonChartCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAmazonChartCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonChartCategoriesResponse = TypedDict('ModelAmazonChartCategoriesResponse', {
    'categories': NotRequired[list[ModelAmazonChartCategory]],
    'category': NotRequired[ModelAmazonChartCategory],
    'chart': NotRequired[str],
    'department': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

ModelAmazonChartCategory = TypedDict('ModelAmazonChartCategory', {
    'department': NotRequired[str],
    'link': NotRequired[str],
    'name': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

ModelAmazonChartsResponseDoc = TypedDict('ModelAmazonChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAmazonChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonChartResponse = TypedDict('ModelAmazonChartResponse', {
    'category_name': NotRequired[str],
    'chart': NotRequired[str],
    'department': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'items': NotRequired[list[ModelAmazonChartItem]],
    'node': NotRequired[str],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelAmazonChartItem = TypedDict('ModelAmazonChartItem', {
    'asin': NotRequired[str],
    'image': NotRequired[str],
    'link': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

AmazonChartsResponse = ModelAmazonChartsResponseDoc
AmazonChartsParams = TypedDict('AmazonChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': Required[str],
    'node': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonChartsCategoriesResponse = ModelAmazonChartCategoriesResponseDoc
AmazonChartsCategoriesParams = TypedDict('AmazonChartsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

AmazonProductResponse = ModelAmazonProductResponseDoc
AmazonProductParams = TypedDict('AmazonProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonSearchResponse = ModelAmazonSearchResponseDoc
AmazonSearchParams = TypedDict('AmazonSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSuggestResponse = ModelAmazonSuggestResponseDoc
AmazonSuggestParams = TypedDict('AmazonSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

class AmazonGroup:
    @overload
    def charts(self, **params: Unpack[AmazonChartsStreamParams]) -> BinaryIO: ...
    @overload
    def charts(self, **params: Unpack[AmazonChartsTextResponseParams]) -> str: ...
    @overload
    def charts(self, **params: Unpack[AmazonChartsDefaultParams]) -> AmazonChartsResponse: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesTextResponseParams]) -> str: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesDefaultParams]) -> AmazonChartsCategoriesResponse: ...
    @overload
    def product(self, **params: Unpack[AmazonProductStreamParams]) -> BinaryIO: ...
    @overload
    def product(self, **params: Unpack[AmazonProductTextResponseParams]) -> str: ...
    @overload
    def product(self, **params: Unpack[AmazonProductDefaultParams]) -> AmazonProductResponse: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchDefaultParams]) -> AmazonSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestDefaultParams]) -> AmazonSuggestResponse: ...

OperationId = Literal[
    'amazon-charts',
    'amazon-charts-categories',
    'amazon-product',
    'amazon-search',
    'amazon-suggest',
]

class CrawloraClient:
    amazon: AmazonGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-charts'],
        params: AmazonChartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-charts-categories'],
        params: AmazonChartsCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonChartsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-product'],
        params: AmazonProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-search'],
        params: AmazonSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-suggest'],
        params: AmazonSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-charts'],
        params: AmazonChartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-charts-categories'],
        params: AmazonChartsCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonChartsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-product'],
        params: AmazonProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-search'],
        params: AmazonSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-suggest'],
        params: AmazonSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class AmazonClient(CrawloraClient):
    def __enter__(self) -> AmazonClient: ...
    @overload
    def charts(self, **params: Unpack[AmazonChartsStreamParams]) -> BinaryIO: ...
    @overload
    def charts(self, **params: Unpack[AmazonChartsTextResponseParams]) -> str: ...
    @overload
    def charts(self, **params: Unpack[AmazonChartsDefaultParams]) -> AmazonChartsResponse: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesTextResponseParams]) -> str: ...
    @overload
    def charts_categories(self, **params: Unpack[AmazonChartsCategoriesDefaultParams]) -> AmazonChartsCategoriesResponse: ...
    @overload
    def product(self, **params: Unpack[AmazonProductStreamParams]) -> BinaryIO: ...
    @overload
    def product(self, **params: Unpack[AmazonProductTextResponseParams]) -> str: ...
    @overload
    def product(self, **params: Unpack[AmazonProductDefaultParams]) -> AmazonProductResponse: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AmazonSearchDefaultParams]) -> AmazonSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[AmazonSuggestDefaultParams]) -> AmazonSuggestResponse: ...

class AsyncAmazonClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncAmazonClient: ...
    amazon: _AsyncAmazonGroup
    @overload
    async def charts(self, **params: Unpack[AmazonChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def charts(self, **params: Unpack[AmazonChartsTextResponseParams]) -> str: ...
    @overload
    async def charts(self, **params: Unpack[AmazonChartsDefaultParams]) -> AmazonChartsResponse: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesDefaultParams]) -> AmazonChartsCategoriesResponse: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductStreamParams]) -> BinaryIO: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductTextResponseParams]) -> str: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductDefaultParams]) -> AmazonProductResponse: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchDefaultParams]) -> AmazonSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestDefaultParams]) -> AmazonSuggestResponse: ...

class _AsyncAmazonGroup:
    @overload
    async def charts(self, **params: Unpack[AmazonChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def charts(self, **params: Unpack[AmazonChartsTextResponseParams]) -> str: ...
    @overload
    async def charts(self, **params: Unpack[AmazonChartsDefaultParams]) -> AmazonChartsResponse: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def charts_categories(self, **params: Unpack[AmazonChartsCategoriesDefaultParams]) -> AmazonChartsCategoriesResponse: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductStreamParams]) -> BinaryIO: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductTextResponseParams]) -> str: ...
    @overload
    async def product(self, **params: Unpack[AmazonProductDefaultParams]) -> AmazonProductResponse: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AmazonSearchDefaultParams]) -> AmazonSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[AmazonSuggestDefaultParams]) -> AmazonSuggestResponse: ...

AmazonChartsDefaultParams = TypedDict('AmazonChartsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': Required[str],
    'node': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonChartsTextResponseParams = TypedDict('AmazonChartsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': Required[str],
    'node': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonChartsStreamParams = TypedDict('AmazonChartsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': Required[str],
    'node': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonChartsCategoriesDefaultParams = TypedDict('AmazonChartsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

AmazonChartsCategoriesTextResponseParams = TypedDict('AmazonChartsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

AmazonChartsCategoriesStreamParams = TypedDict('AmazonChartsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart': Required[Literal['best_sellers', 'new_releases', 'most_wished_for']],
    'department': NotRequired[str],
    'node': NotRequired[str],
}, total=False)

AmazonProductDefaultParams = TypedDict('AmazonProductDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonProductTextResponseParams = TypedDict('AmazonProductTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonProductStreamParams = TypedDict('AmazonProductStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonSearchDefaultParams = TypedDict('AmazonSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSearchTextResponseParams = TypedDict('AmazonSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSearchStreamParams = TypedDict('AmazonSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSuggestDefaultParams = TypedDict('AmazonSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

AmazonSuggestTextResponseParams = TypedDict('AmazonSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

AmazonSuggestStreamParams = TypedDict('AmazonSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)
