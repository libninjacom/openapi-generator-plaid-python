"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.account_base import AccountBase
from openapi_client.model.item import Item
from openapi_client.model.liabilities_object import LiabilitiesObject
globals()['AccountBase'] = AccountBase
globals()['Item'] = Item
globals()['LiabilitiesObject'] = LiabilitiesObject
from openapi_client.model.liabilities_get_response import LiabilitiesGetResponse


class TestLiabilitiesGetResponse(unittest.TestCase):
    """LiabilitiesGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLiabilitiesGetResponse(self):
        """Test LiabilitiesGetResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LiabilitiesGetResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()