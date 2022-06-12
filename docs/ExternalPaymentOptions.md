# ExternalPaymentOptions

Additional payment options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_refund_details** | **bool, none_type** | When &#x60;true&#x60;, Plaid will attempt to request refund details from the payee&#39;s financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the &#x60;/payment_initiation/payment/get&#x60; response. | [optional] 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the payer&#39;s account. If provided, the end user will be able to send payments only from the specified bank account. | [optional] 
**bacs** | [**PaymentInitiationOptionalRestrictionBacs**](PaymentInitiationOptionalRestrictionBacs.md) |  | [optional] 
**wallet_id** | **str, none_type** | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**scheme** | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


