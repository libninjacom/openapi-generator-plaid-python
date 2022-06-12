# SimulatedTransferSweep

A sweep returned from the `/sandbox/transfer/sweep/simulate` endpoint. Can be null if there are no transfers to include in a sweep.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the sweep. | 
**created** | **datetime** | The datetime when the sweep occurred, in RFC 3339 format. | 
**amount** | **str** | Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. \&quot;-10.00\&quot;)  If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep account and Plaid are balanced. | 
**iso_currency_code** | **str** | The currency of the sweep, e.g. \&quot;USD\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


