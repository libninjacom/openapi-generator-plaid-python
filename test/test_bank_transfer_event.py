"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.bank_transfer_direction import BankTransferDirection
from openapi_client.model.bank_transfer_event_type import BankTransferEventType
from openapi_client.model.bank_transfer_failure import BankTransferFailure
from openapi_client.model.bank_transfer_type import BankTransferType
globals()['BankTransferDirection'] = BankTransferDirection
globals()['BankTransferEventType'] = BankTransferEventType
globals()['BankTransferFailure'] = BankTransferFailure
globals()['BankTransferType'] = BankTransferType
from openapi_client.model.bank_transfer_event import BankTransferEvent


class TestBankTransferEvent(unittest.TestCase):
    """BankTransferEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBankTransferEvent(self):
        """Test BankTransferEvent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BankTransferEvent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
