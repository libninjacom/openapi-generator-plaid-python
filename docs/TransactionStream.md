# TransactionStream

A grouping of related transactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account to which the stream belongs | 
**stream_id** | **str** | A unique id for the stream | 
**category_id** | **str** | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview). | 
**category** | **[str]** | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview). | 
**description** | **str** | A description of the transaction stream. | 
**first_date** | **date** | The posted date of the earliest transaction in the stream. | 
**last_date** | **date** | The posted date of the latest transaction in the stream. | 
**frequency** | [**RecurringTransactionFrequency**](RecurringTransactionFrequency.md) |  | 
**transaction_ids** | **[str]** | An array of Plaid transaction IDs belonging to the stream, sorted by posted date. | 
**average_amount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**is_active** | **bool** | indicates whether the transaction stream is still live. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


