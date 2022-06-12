# WalletTransaction

The transaction details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | A unique ID identifying the transaction | 
**reference** | **str** | A reference for the transaction | 
**amount** | [**WalletTransactionAmount**](WalletTransactionAmount.md) |  | 
**counterparty** | [**WalletTransactionCounterparty**](WalletTransactionCounterparty.md) |  | 
**status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**created_at** | **datetime** | Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**type** | **str** | The type of of the transaction. Currently, only &#x60;\&quot;PAYOUT\&quot;&#x60; is supported. | defaults to "PAYOUT"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


