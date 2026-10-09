# crawlora-amazon

Python client for Crawlora's hosted Amazon API. It calls Crawlora's
service at [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-python-homepage); it does not run a browser or scrape
Amazon locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Amazon or its owners.

## Install

```sh
python -m pip install crawlora-amazon
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_amazon import AmazonClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with AmazonClient(api_key=api_key) as client:
    result_1 = client.search(k='wireless headphones')
    print(result_1)
    result_2 = client.suggest(keyword='wireless headphones')
    print(result_2)
```

The package also exports `Client` as an alias for `AmazonClient`. Operation
methods are available directly in snake_case and through the `amazon`
group. The async package client is `AsyncAmazonClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-amazon/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-amazon/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_amazon import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(k='wireless headphones')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-amazon/blob/main/examples/python.py) for a complete usage example.

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
