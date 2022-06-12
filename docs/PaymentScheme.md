# PaymentScheme

Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.  `FASTER_PAYMENTS`: Enables payments to move quickly between UK bank accounts. Default value in the UK.  `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.  `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Payment scheme. If not specified - the default in the region will be used (e.g. &#x60;SEPA_CREDIT_TRANSFER&#x60; for EU). Using unsupported values will result in a failed payment.  &#x60;FASTER_PAYMENTS&#x60;: Enables payments to move quickly between UK bank accounts. Default value in the UK.  &#x60;SEPA_CREDIT_TRANSFER&#x60;: The standard payment to a beneficiary within the SEPA area.  &#x60;SEPA_CREDIT_TRANSFER_INSTANT&#x60;: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks. |  must be one of ["null", "FASTER_PAYMENTS", "SEPA_CREDIT_TRANSFER", "SEPA_CREDIT_TRANSFER_INSTANT", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


