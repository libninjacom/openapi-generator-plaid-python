# TransferEventType

The type of event that this transfer represents.  `pending`: A new transfer was created; it is in the pending state.  `cancelled`: The transfer was cancelled by the client.  `failed`: The transfer failed, no funds were moved.  `posted`: The transfer has been successfully submitted to the payment network.  `reversed`: A posted transfer was reversed.  `swept`: The transfer was swept to / from the sweep account.  `reverse_swept`: Due to the transfer reversing, funds were pulled from or pushed back to the sweep account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The type of event that this transfer represents.  &#x60;pending&#x60;: A new transfer was created; it is in the pending state.  &#x60;cancelled&#x60;: The transfer was cancelled by the client.  &#x60;failed&#x60;: The transfer failed, no funds were moved.  &#x60;posted&#x60;: The transfer has been successfully submitted to the payment network.  &#x60;reversed&#x60;: A posted transfer was reversed.  &#x60;swept&#x60;: The transfer was swept to / from the sweep account.  &#x60;reverse_swept&#x60;: Due to the transfer reversing, funds were pulled from or pushed back to the sweep account. |  must be one of ["pending", "cancelled", "failed", "posted", "reversed", "swept", "reverse_swept", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


