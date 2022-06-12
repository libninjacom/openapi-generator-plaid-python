# InvestmentsTransactionsGetRequestOptions

An optional object to filter `/investments/transactions/get` results. If provided, must be non-`null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | An array of &#x60;account_ids&#x60; to retrieve for the Item. | [optional] 
**count** | **int** | The number of transactions to fetch.  | [optional]  if omitted the server will use the default value of 100
**offset** | **int** | The number of transactions to skip when fetching transaction history | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


