"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.account_access import AccountAccess
from openapi_client.model.product_access import ProductAccess
from openapi_client.model.scopes import Scopes
globals()['AccountAccess'] = AccountAccess
globals()['ProductAccess'] = ProductAccess
globals()['Scopes'] = Scopes
from openapi_client.model.scopes_nullable import ScopesNullable


class TestScopesNullable(unittest.TestCase):
    """ScopesNullable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScopesNullable(self):
        """Test ScopesNullable"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScopesNullable()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
