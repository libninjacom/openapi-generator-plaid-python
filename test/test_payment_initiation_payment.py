"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.external_payment_refund_details import ExternalPaymentRefundDetails
from openapi_client.model.external_payment_schedule_get import ExternalPaymentScheduleGet
from openapi_client.model.payment_amount import PaymentAmount
from openapi_client.model.payment_initiation_payment_status import PaymentInitiationPaymentStatus
from openapi_client.model.payment_initiation_refund import PaymentInitiationRefund
from openapi_client.model.payment_scheme import PaymentScheme
from openapi_client.model.sender_bacs_nullable import SenderBACSNullable
globals()['ExternalPaymentRefundDetails'] = ExternalPaymentRefundDetails
globals()['ExternalPaymentScheduleGet'] = ExternalPaymentScheduleGet
globals()['PaymentAmount'] = PaymentAmount
globals()['PaymentInitiationPaymentStatus'] = PaymentInitiationPaymentStatus
globals()['PaymentInitiationRefund'] = PaymentInitiationRefund
globals()['PaymentScheme'] = PaymentScheme
globals()['SenderBACSNullable'] = SenderBACSNullable
from openapi_client.model.payment_initiation_payment import PaymentInitiationPayment


class TestPaymentInitiationPayment(unittest.TestCase):
    """PaymentInitiationPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentInitiationPayment(self):
        """Test PaymentInitiationPayment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentInitiationPayment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
