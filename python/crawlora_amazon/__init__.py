"""Typed Amazon client for the Crawlora hosted API."""

from .platform import AmazonClient, AsyncAmazonClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AmazonClient
AsyncClient = AsyncAmazonClient
__version__ = '0.1.1'
DISPLAY_NAME = 'Amazon'
PLATFORM = 'amazon'
CONTRACT_REVISION = 'sha256:ccae432eea9beb55dab5108c0f607d20edb7b2a7ee7746836139bea73f70e547'

__all__ = [
    "AmazonClient", "AsyncAmazonClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
