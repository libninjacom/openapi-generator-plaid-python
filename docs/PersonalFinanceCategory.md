# PersonalFinanceCategory

Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases. The field is currently in beta.  The complete category can be generated by concatenating primary and detailed categories.  This feature is currently in beta – to request access, contact transactions-feedback@plaid.com.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | A high level category that communicates the broad category of the transaction. | 
**detailed** | **str** | Provides additional granularity to the primary categorization. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


