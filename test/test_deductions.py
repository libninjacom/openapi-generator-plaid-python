"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.deductions_breakdown import DeductionsBreakdown
from openapi_client.model.deductions_total import DeductionsTotal
from openapi_client.model.total import Total
globals()['DeductionsBreakdown'] = DeductionsBreakdown
globals()['DeductionsTotal'] = DeductionsTotal
globals()['Total'] = Total
from openapi_client.model.deductions import Deductions


class TestDeductions(unittest.TestCase):
    """Deductions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeductions(self):
        """Test Deductions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Deductions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
