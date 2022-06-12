# TransferSweepStatus

The status of the sweep for the transfer. `unswept`: The transfer hasn't been swept yet. `swept`: The transfer was swept to the sweep account. `reverse_swept`: The transfer was reversed, funds were pulled back or pushed back to the sweep account. `null`: The transfer will never be swept (e.g. if the transfer is cancelled or reversed before being swept)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the sweep for the transfer. &#x60;unswept&#x60;: The transfer hasn&#39;t been swept yet. &#x60;swept&#x60;: The transfer was swept to the sweep account. &#x60;reverse_swept&#x60;: The transfer was reversed, funds were pulled back or pushed back to the sweep account. &#x60;null&#x60;: The transfer will never be swept (e.g. if the transfer is cancelled or reversed before being swept) |  must be one of ["null", "unswept", "swept", "reverse_swept", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


