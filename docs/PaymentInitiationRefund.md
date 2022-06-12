# PaymentInitiationRefund

PaymentInitiationRefund defines a payment initiation refund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_id** | **str** | The ID of the refund. Like all Plaid identifiers, the &#x60;refund_id&#x60; is case sensitive. | 
**amount** | [**PaymentAmount**](PaymentAmount.md) |  | 
**status** | **str** | The status of the refund.  &#x60;PROCESSING&#x60;: The refund is currently being processed. The refund will automatically exit this state when processing is complete.  &#x60;INITIATED&#x60;: The refund has been successfully initiated.  &#x60;EXECUTED&#x60;: Indicates that the refund has been successfully executed.  &#x60;FAILED&#x60;: The refund has failed to be executed. This error is retryable once the root cause is resolved. | 
**last_status_update** | **datetime** | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


