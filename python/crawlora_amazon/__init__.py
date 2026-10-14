"""Typed Amazon client for the Crawlora hosted API."""

from .platform import AmazonClient, AsyncAmazonClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AmazonClient
AsyncClient = AsyncAmazonClient
__version__ = '0.1.3'
DISPLAY_NAME = 'Amazon'
PLATFORM = 'amazon'
CONTRACT_REVISION = 'sha256:a7066bc4b0b04a10f8eaf089cc2271177472c13e324122f75e182737e7aa0ada'

__all__ = [
    "AmazonClient", "AsyncAmazonClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
