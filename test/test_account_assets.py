"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.account_assets_all_of import AccountAssetsAllOf
from openapi_client.model.account_balance import AccountBalance
from openapi_client.model.account_base import AccountBase
from openapi_client.model.account_subtype import AccountSubtype
from openapi_client.model.account_type import AccountType
from openapi_client.model.asset_report_transaction import AssetReportTransaction
from openapi_client.model.historical_balance import HistoricalBalance
from openapi_client.model.owner import Owner
globals()['AccountAssetsAllOf'] = AccountAssetsAllOf
globals()['AccountBalance'] = AccountBalance
globals()['AccountBase'] = AccountBase
globals()['AccountSubtype'] = AccountSubtype
globals()['AccountType'] = AccountType
globals()['AssetReportTransaction'] = AssetReportTransaction
globals()['HistoricalBalance'] = HistoricalBalance
globals()['Owner'] = Owner
from openapi_client.model.account_assets import AccountAssets


class TestAccountAssets(unittest.TestCase):
    """AccountAssets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountAssets(self):
        """Test AccountAssets"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountAssets()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()