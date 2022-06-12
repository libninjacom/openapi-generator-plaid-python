# InstitutionsSearchRequestOptions

An optional object to filter `/institutions/search` results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauth** | **bool, none_type** | Limit results to institutions with or without OAuth login flows. | [optional] 
**include_optional_metadata** | **bool** | When true, return the institution&#39;s homepage URL, logo and primary brand color. | [optional] 
**include_auth_metadata** | **bool, none_type** | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional]  if omitted the server will use the default value of False
**include_payment_initiation_metadata** | **bool, none_type** | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional]  if omitted the server will use the default value of False
**payment_initiation** | [**InstitutionsSearchPaymentInitiationOptions**](InstitutionsSearchPaymentInitiationOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


