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
from openapi_client.model.personal_finance_category import PersonalFinanceCategory
from openapi_client.model.transaction_all_of import TransactionAllOf
from openapi_client.model.transaction_base import TransactionBase
from openapi_client.model.transaction_code import TransactionCode
globals()['Location'] = Location
globals()['PaymentMeta'] = PaymentMeta
globals()['PersonalFinanceCategory'] = PersonalFinanceCategory
globals()['TransactionAllOf'] = TransactionAllOf
globals()['TransactionBase'] = TransactionBase
globals()['TransactionCode'] = TransactionCode
from openapi_client.model.transaction import Transaction


class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransaction(self):
        """Test Transaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Transaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
