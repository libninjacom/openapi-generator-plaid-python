"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.requested_scopes import RequestedScopes
from openapi_client.model.scopes_nullable import ScopesNullable
globals()['RequestedScopes'] = RequestedScopes
globals()['ScopesNullable'] = ScopesNullable
from openapi_client.model.connected_application import ConnectedApplication


class TestConnectedApplication(unittest.TestCase):
    """ConnectedApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnectedApplication(self):
        """Test ConnectedApplication"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConnectedApplication()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
