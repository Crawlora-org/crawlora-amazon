import os

from crawlora_amazon import AmazonClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with AmazonClient(api_key=api_key) as client:
    search = client.search(k='wireless headphones')
    print('search', search)
    suggest = client.suggest(keyword='wireless headphones')
    print('suggest', suggest)
