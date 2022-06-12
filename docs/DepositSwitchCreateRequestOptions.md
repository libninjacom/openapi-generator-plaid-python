# DepositSwitchCreateRequestOptions

Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **str, none_type** | The URL registered to receive webhooks when the status of a deposit switch request has changed.  | [optional] 
**transaction_item_access_tokens** | **[str]** | An array of access tokens corresponding to transaction items to use when attempting to match the user to their Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access to the transactions product. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


