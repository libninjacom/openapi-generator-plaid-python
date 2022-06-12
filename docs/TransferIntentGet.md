# TransferIntentGet

Represents a transfer intent within Transfer UI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid&#39;s unique identifier for a transfer intent object. | 
**created** | **datetime** | The datetime the transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**status** | **str** | The status of the transfer intent.  - &#x60;PENDING&#x60; – The transfer intent is pending. - &#x60;SUCCEEDED&#x60; – The transfer intent was successfully created. - &#x60;FAILED&#x60; – The transfer intent was unable to be created. | 
**transfer_id** | **str, none_type** | Plaid&#39;s unique identifier for the transfer created through the UI. Returned only if the transfer was successfully created. Null value otherwise. | 
**failure_reason** | [**TransferIntentGetFailureReason**](TransferIntentGetFailureReason.md) |  | 
**authorization_decision** | **str, none_type** |  A decision regarding the proposed transfer.  &#x60;APPROVED&#x60; – The proposed transfer has received the end user&#39;s consent and has been approved for processing. Plaid has also reviewed the proposed transfer and has approved it for processing.   &#x60;PERMITTED&#x60; – Plaid was unable to fetch the information required to approve or decline the proposed transfer. You may proceed with the transfer, but further review is recommended. Plaid is awaiting further instructions from the client.  &#x60;DECLINED&#x60; – Plaid reviewed the proposed transfer and declined processing. Refer to the &#x60;code&#x60; field in the &#x60;decision_rationale&#x60; object for details. Null value otherwise. | 
**authorization_decision_rationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account used for the transfer. | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**description** | **str** | A description for the underlying transfer. Maximum of 8 characters. | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**account_id** | **str, none_type** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


