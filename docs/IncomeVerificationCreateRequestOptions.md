# IncomeVerificationCreateRequestOptions

Optional arguments for `/income/verification/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_tokens** | **[str]** | An array of access tokens corresponding to the Items that will be cross-referenced with the product data. Plaid will attempt to correlate transaction history from these Items with data from the user&#39;s paystub, such as date and amount. The &#x60;verification&#x60; status of the paystub as returned by &#x60;/income/verification/paystubs/get&#x60; will indicate if the verification status was successful, or, if not, why it failed. If the &#x60;transactions&#x60; product was not initialized for the Items during Link, it will be initialized after this Link session. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


