"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.payment_initiation_payment_status import PaymentInitiationPaymentStatus
from openapi_client.model.plaid_error import PlaidError
globals()['PaymentInitiationPaymentStatus'] = PaymentInitiationPaymentStatus
globals()['PlaidError'] = PlaidError
from openapi_client.model.payment_status_update_webhook import PaymentStatusUpdateWebhook


class TestPaymentStatusUpdateWebhook(unittest.TestCase):
    """PaymentStatusUpdateWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentStatusUpdateWebhook(self):
        """Test PaymentStatusUpdateWebhook"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentStatusUpdateWebhook()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
