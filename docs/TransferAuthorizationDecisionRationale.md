# TransferAuthorizationDecisionRationale

The rationale for Plaid's decision regarding a proposed transfer. Will be null for `approved` decisions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A code representing the rationale for permitting or declining the proposed transfer. Possible values are:  &#x60;NSF&#x60; – Transaction likely to result in a return due to insufficient funds.  &#x60;RISK&#x60; - Transaction is high-risk.  &#x60;MANUALLY_VERIFIED_ITEM&#x60; – Item created via same-day micro deposits, limited information available. Plaid can only offer &#x60;permitted&#x60; as a transaction decision.  &#x60;LOGIN_REQUIRED&#x60; – Unable to collect the account information required for an authorization decision due to Item staleness. Can be rectified using Link update mode.  &#x60;ERROR&#x60; – Unable to collect the account information required for an authorization decision due to an error. | 
**description** | **str** | A human-readable description of the code associated with a permitted transfer or transfer decline. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


