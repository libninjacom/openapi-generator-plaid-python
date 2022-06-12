# Transfer

Represents a transfer within the Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid’s unique identifier for a transfer. | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | 
**account_id** | **str** | The account ID that should be credited/debited for this transfer. | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**description** | **str** | The description of the transfer. | 
**created** | **datetime** | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**status** | [**TransferStatus**](TransferStatus.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**cancellable** | **bool** | When &#x60;true&#x60;, you can still cancel this transfer. | 
**failure_reason** | [**TransferFailure**](TransferFailure.md) |  | 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**sweep_status** | [**TransferSweepStatus**](TransferSweepStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


