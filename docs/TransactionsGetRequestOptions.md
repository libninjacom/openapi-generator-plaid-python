# TransactionsGetRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | A list of &#x60;account_ids&#x60; to retrieve for the Item  Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | [optional] 
**count** | **int** | The number of transactions to fetch. | [optional]  if omitted the server will use the default value of 100
**offset** | **int** | The number of transactions to skip. The default value is 0. | [optional]  if omitted the server will use the default value of 0
**include_original_description** | **bool, none_type** | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager. | [optional]  if omitted the server will use the default value of False
**include_personal_finance_category_beta** | **bool** | Include the &#x60;personal_finance_category&#x60; object in the response. This feature is currently in beta – to request access, contact transactions-feedback@plaid.com. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


