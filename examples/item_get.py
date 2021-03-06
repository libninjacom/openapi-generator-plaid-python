"""
Note that this example, and other documentation, is not generated by openapi-generator.

Your engineering team will have to hand write these examples and other documentation.

Or, you can use Libninja!
"""
import asyncio
import os

from openapi_client import ApiClient, Configuration
from openapi_client.api.plaid_api import PlaidApi
from openapi_client.model.item_get_request import ItemGetRequest


def main():
    client = PlaidApi(api_client=ApiClient(configuration=Configuration(api_key={
        'clientId': os.environ['PLAID_PUBLIC_KEY'],
        'plaidVersion': os.environ['PLAID_VERSION'],
        'secret': os.environ['PLAID_SECRET'],
    })))
    res = client.item_get(ItemGetRequest("access-sandbox-b4957595-eae2-4130-9da7-114d14726a62"))
    print(res)


async def async_main():
    client = PlaidApi(api_client=ApiClient(configuration=Configuration(api_key={
        'clientId': os.environ['PLAID_PUBLIC_KEY'],
        'plaidVersion': os.environ['PLAID_VERSION'],
        'secret': os.environ['PLAID_SECRET'],
    })))
    res = await client.item_get(ItemGetRequest("access-sandbox-b4957595-eae2-4130-9da7-114d14726a62"), async_req=True)
    print(res)


if __name__ == "__main__":
    main()
    # asyncio.run(async_main())