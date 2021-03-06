"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.deductions import Deductions
from openapi_client.model.earnings import Earnings
from openapi_client.model.employee import Employee
from openapi_client.model.employment_details import EmploymentDetails
from openapi_client.model.income_breakdown import IncomeBreakdown
from openapi_client.model.net_pay import NetPay
from openapi_client.model.pay_period_details import PayPeriodDetails
from openapi_client.model.paystub_details import PaystubDetails
from openapi_client.model.paystub_employer import PaystubEmployer
from openapi_client.model.paystub_verification import PaystubVerification
from openapi_client.model.paystub_ytd_details import PaystubYTDDetails
globals()['Deductions'] = Deductions
globals()['Earnings'] = Earnings
globals()['Employee'] = Employee
globals()['EmploymentDetails'] = EmploymentDetails
globals()['IncomeBreakdown'] = IncomeBreakdown
globals()['NetPay'] = NetPay
globals()['PayPeriodDetails'] = PayPeriodDetails
globals()['PaystubDetails'] = PaystubDetails
globals()['PaystubEmployer'] = PaystubEmployer
globals()['PaystubVerification'] = PaystubVerification
globals()['PaystubYTDDetails'] = PaystubYTDDetails
from openapi_client.model.paystub import Paystub


class TestPaystub(unittest.TestCase):
    """Paystub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaystub(self):
        """Test Paystub"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Paystub()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
