# TransferAuthorizationProposedTransfer

Details regarding the proposed transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**network** | **str** | The network or rails used for the transfer. | 
**origination_account_id** | **str** | Plaid&#39;s unique identifier for the origination account that was used for this transfer. | 
**iso_currency_code** | **str** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


