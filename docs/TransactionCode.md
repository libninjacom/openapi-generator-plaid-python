# TransactionCode

An identifier classifying the transaction type.  This field is only populated for European institutions. For institutions in the US and Canada, this field is set to `null`.  `adjustment:` Bank adjustment  `atm:` Cash deposit or withdrawal via an automated teller machine  `bank charge:` Charge or fee levied by the institution  `bill payment`: Payment of a bill  `cash:` Cash deposit or withdrawal  `cashback:` Cash withdrawal while making a debit card purchase  `cheque:` Document ordering the payment of money to another person or organization  `direct debit:` Automatic withdrawal of funds initiated by a third party at a regular interval  `interest:` Interest earned or incurred  `purchase:` Purchase made with a debit or credit card  `standing order:` Payment instructed by the account holder to a third party at a regular interval  `transfer:` Transfer of money between accounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | An identifier classifying the transaction type.  This field is only populated for European institutions. For institutions in the US and Canada, this field is set to &#x60;null&#x60;.  &#x60;adjustment:&#x60; Bank adjustment  &#x60;atm:&#x60; Cash deposit or withdrawal via an automated teller machine  &#x60;bank charge:&#x60; Charge or fee levied by the institution  &#x60;bill payment&#x60;: Payment of a bill  &#x60;cash:&#x60; Cash deposit or withdrawal  &#x60;cashback:&#x60; Cash withdrawal while making a debit card purchase  &#x60;cheque:&#x60; Document ordering the payment of money to another person or organization  &#x60;direct debit:&#x60; Automatic withdrawal of funds initiated by a third party at a regular interval  &#x60;interest:&#x60; Interest earned or incurred  &#x60;purchase:&#x60; Purchase made with a debit or credit card  &#x60;standing order:&#x60; Payment instructed by the account holder to a third party at a regular interval  &#x60;transfer:&#x60; Transfer of money between accounts |  must be one of ["adjustment", "atm", "bank charge", "bill payment", "cash", "cashback", "cheque", "direct debit", "interest", "purchase", "standing order", "transfer", "null", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


