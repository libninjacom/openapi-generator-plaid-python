# TransferCreateRequest

Defines the request schema for `/transfer/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. | 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | 
**authorization_id** | **str** | Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier. | 
**type** | [**TransferType**](TransferType.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**description** | **str** | The transfer description. Maximum of 10 characters. | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**user** | [**TransferUserInRequest**](TransferUserInRequest.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**idempotency_key** | [**TransferCreateIdempotencyKey**](TransferCreateIdempotencyKey.md) |  | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**origination_account_id** | **str, none_type** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank. | [optional] 
**iso_currency_code** | **str** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


