# TransferIntentCreateRequest

Defines the request schema for `/transfer/intent/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**description** | **str** | A description for the underlying transfer. Maximum of 8 characters. | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**user** | [**TransferUserInRequest**](TransferUserInRequest.md) |  | 
**account_id** | **str, none_type** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | [optional] 
**origination_account_id** | **str, none_type** | Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used. | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


