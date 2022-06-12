# PaymentInitiationPaymentCreateRequest

PaymentInitiationPaymentCreateRequest defines the request schema for `/payment_initiation/payment/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | The ID of the recipient the payment is for. | 
**reference** | **str** | A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them). | 
**amount** | [**PaymentAmount**](PaymentAmount.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**schedule** | [**ExternalPaymentScheduleRequest**](ExternalPaymentScheduleRequest.md) |  | [optional] 
**options** | [**ExternalPaymentOptions**](ExternalPaymentOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


