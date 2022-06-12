# TransferIntentCreate

Represents a transfer intent within Transfer UI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid&#39;s unique identifier for the transfer intent object. | 
**created** | **datetime** | The datetime the transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**status** | **str** | The status of the transfer intent.  - &#x60;PENDING&#x60; – The transfer intent is pending. - &#x60;SUCCEEDED&#x60; – The transfer intent was successfully created. - &#x60;FAILED&#x60; – The transfer intent was unable to be created. | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used. | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**description** | **str** | A description for the underlying transfer. Maximum of 8 characters. | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**account_id** | **str, none_type** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


