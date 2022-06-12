# Holding

A securities holding at an institution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Plaid &#x60;account_id&#x60; associated with the holding. | 
**security_id** | **str** | The Plaid &#x60;security_id&#x60; associated with the holding. | 
**institution_price** | **float** | The last price given by the institution for this security. | 
**institution_price_as_of** | **date, none_type** | The date at which &#x60;institution_price&#x60; was current. | 
**institution_value** | **float** | The value of the holding, as reported by the institution. | 
**cost_basis** | **float, none_type** | The cost basis of the holding. | 
**quantity** | **float** | The total quantity of the asset held, as reported by the financial institution. If the security is an option, &#x60;quantity&#x60; will reflect the total number of options (typically the number of contracts multiplied by 100), not the number of contracts. | 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the holding. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


