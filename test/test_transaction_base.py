"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.location import Location
from openapi_client.model.payment_meta import PaymentMeta
globals()['Location'] = Location
globals()['PaymentMeta'] = PaymentMeta
from openapi_client.model.transaction_base import TransactionBase


class TestTransactionBase(unittest.TestCase):
    """TransactionBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionBase(self):
        """Test TransactionBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()