"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.ach_class import ACHClass
from openapi_client.model.transfer_type import TransferType
from openapi_client.model.transfer_user_in_response import TransferUserInResponse
globals()['ACHClass'] = ACHClass
globals()['TransferType'] = TransferType
globals()['TransferUserInResponse'] = TransferUserInResponse
from openapi_client.model.transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer


class TestTransferAuthorizationProposedTransfer(unittest.TestCase):
    """TransferAuthorizationProposedTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransferAuthorizationProposedTransfer(self):
        """Test TransferAuthorizationProposedTransfer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransferAuthorizationProposedTransfer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
