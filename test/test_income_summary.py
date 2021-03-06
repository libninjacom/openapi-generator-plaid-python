"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.employee_income_summary_field_string import EmployeeIncomeSummaryFieldString
from openapi_client.model.employer_income_summary_field_string import EmployerIncomeSummaryFieldString
from openapi_client.model.pay_frequency import PayFrequency
from openapi_client.model.projected_income_summary_field_number import ProjectedIncomeSummaryFieldNumber
from openapi_client.model.transaction_data import TransactionData
from openapi_client.model.ytd_gross_income_summary_field_number import YTDGrossIncomeSummaryFieldNumber
from openapi_client.model.ytd_net_income_summary_field_number import YTDNetIncomeSummaryFieldNumber
globals()['EmployeeIncomeSummaryFieldString'] = EmployeeIncomeSummaryFieldString
globals()['EmployerIncomeSummaryFieldString'] = EmployerIncomeSummaryFieldString
globals()['PayFrequency'] = PayFrequency
globals()['ProjectedIncomeSummaryFieldNumber'] = ProjectedIncomeSummaryFieldNumber
globals()['TransactionData'] = TransactionData
globals()['YTDGrossIncomeSummaryFieldNumber'] = YTDGrossIncomeSummaryFieldNumber
globals()['YTDNetIncomeSummaryFieldNumber'] = YTDNetIncomeSummaryFieldNumber
from openapi_client.model.income_summary import IncomeSummary


class TestIncomeSummary(unittest.TestCase):
    """IncomeSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncomeSummary(self):
        """Test IncomeSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncomeSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
