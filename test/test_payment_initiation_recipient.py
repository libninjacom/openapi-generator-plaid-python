"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.payment_initiation_address import PaymentInitiationAddress
from openapi_client.model.recipient_bacs_nullable import RecipientBACSNullable
globals()['PaymentInitiationAddress'] = PaymentInitiationAddress
globals()['RecipientBACSNullable'] = RecipientBACSNullable
from openapi_client.model.payment_initiation_recipient import PaymentInitiationRecipient


class TestPaymentInitiationRecipient(unittest.TestCase):
    """PaymentInitiationRecipient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentInitiationRecipient(self):
        """Test PaymentInitiationRecipient"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentInitiationRecipient()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
