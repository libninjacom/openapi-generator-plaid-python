# Warning

It is possible for an Asset Report to be returned with missing account owner information. In such cases, the Asset Report will contain warning data in the response, indicating why obtaining the owner information failed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning_type** | **str** | The warning type, which will always be &#x60;ASSET_REPORT_WARNING&#x60; | 
**cause** | [**Cause**](Cause.md) |  | 
**warning_code** | **str** | The warning code identifies a specific kind of warning. Currently, the only possible warning code is &#x60;OWNERS_UNAVAILABLE&#x60;, which indicates that account-owner information is not available. | defaults to "OWNERS_UNAVAILABLE"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


