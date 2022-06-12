# WalletTransactionStatus

The status of the transaction.  `INITIATED`: This is the initial state of all transactions. It indicates that the transaction has been initiated and is currently being processed.  `EXECUTED`: The transaction has been successfully executed.  `FAILED`: The transaction failed to process successfully. This is a terminal status.  `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the transaction.  &#x60;INITIATED&#x60;: This is the initial state of all transactions. It indicates that the transaction has been initiated and is currently being processed.  &#x60;EXECUTED&#x60;: The transaction has been successfully executed.  &#x60;FAILED&#x60;: The transaction failed to process successfully. This is a terminal status.  &#x60;BLOCKED&#x60;: The transaction has been blocked for violating compliance rules. This is a terminal status. |  must be one of ["INITIATED", "EXECUTED", "BLOCKED", "FAILED", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


