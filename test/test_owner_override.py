"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.address import Address
from openapi_client.model.email import Email
from openapi_client.model.phone_number import PhoneNumber
globals()['Address'] = Address
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
from openapi_client.model.owner_override import OwnerOverride


class TestOwnerOverride(unittest.TestCase):
    """OwnerOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOwnerOverride(self):
        """Test OwnerOverride"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OwnerOverride()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
