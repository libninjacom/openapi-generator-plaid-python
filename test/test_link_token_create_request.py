"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.64.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.country_code import CountryCode
from openapi_client.model.link_token_account_filters import LinkTokenAccountFilters
from openapi_client.model.link_token_create_request_auth import LinkTokenCreateRequestAuth
from openapi_client.model.link_token_create_request_deposit_switch import LinkTokenCreateRequestDepositSwitch
from openapi_client.model.link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
from openapi_client.model.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
from openapi_client.model.link_token_create_request_transfer import LinkTokenCreateRequestTransfer
from openapi_client.model.link_token_create_request_update import LinkTokenCreateRequestUpdate
from openapi_client.model.link_token_create_request_user import LinkTokenCreateRequestUser
from openapi_client.model.link_token_eu_config import LinkTokenEUConfig
from openapi_client.model.products import Products
globals()['CountryCode'] = CountryCode
globals()['LinkTokenAccountFilters'] = LinkTokenAccountFilters
globals()['LinkTokenCreateRequestAuth'] = LinkTokenCreateRequestAuth
globals()['LinkTokenCreateRequestDepositSwitch'] = LinkTokenCreateRequestDepositSwitch
globals()['LinkTokenCreateRequestIncomeVerification'] = LinkTokenCreateRequestIncomeVerification
globals()['LinkTokenCreateRequestPaymentInitiation'] = LinkTokenCreateRequestPaymentInitiation
globals()['LinkTokenCreateRequestTransfer'] = LinkTokenCreateRequestTransfer
globals()['LinkTokenCreateRequestUpdate'] = LinkTokenCreateRequestUpdate
globals()['LinkTokenCreateRequestUser'] = LinkTokenCreateRequestUser
globals()['LinkTokenEUConfig'] = LinkTokenEUConfig
globals()['Products'] = Products
from openapi_client.model.link_token_create_request import LinkTokenCreateRequest


class TestLinkTokenCreateRequest(unittest.TestCase):
    """LinkTokenCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkTokenCreateRequest(self):
        """Test LinkTokenCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkTokenCreateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
