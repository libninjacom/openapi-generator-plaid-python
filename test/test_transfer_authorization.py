"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from openapi_client.model.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from openapi_client.model.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from openapi_client.model.transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer
globals()['TransferAuthorizationDecisionRationale'] = TransferAuthorizationDecisionRationale
globals()['TransferAuthorizationGuaranteeDecision'] = TransferAuthorizationGuaranteeDecision
globals()['TransferAuthorizationGuaranteeDecisionRationale'] = TransferAuthorizationGuaranteeDecisionRationale
globals()['TransferAuthorizationProposedTransfer'] = TransferAuthorizationProposedTransfer
from openapi_client.model.transfer_authorization import TransferAuthorization


class TestTransferAuthorization(unittest.TestCase):
    """TransferAuthorization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransferAuthorization(self):
        """Test TransferAuthorization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransferAuthorization()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
