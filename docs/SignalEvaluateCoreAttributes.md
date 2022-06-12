# SignalEvaluateCoreAttributes

The core attributes object contains additional data that can be used to assess the ACH return risk. Examples of data include:  `days_since_first_plaid_connection`: The number of days since the first time the Item was connected to an application via Plaid `plaid_connections_count_7d`: The number of times the Item has been connected to applications via Plaid over the past 7 days `plaid_connections_count_30d`: The number of times the Item has been connected to applications via Plaid over the past 30 days `total_plaid_connections_count`: The number of times the Item has been connected to applications via Plaid `is_savings_or_money_market_account`: Indicates whether the ACH transaction funding account is a savings/money market account  For the full list and detailed documentation of core attributes available, or to request that core attributes not be returned, contact Sales or your Plaid account manager

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unauthorized_transactions_count_7d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited. | [optional] 
**unauthorized_transactions_count_30d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited. | [optional] 
**unauthorized_transactions_count_60d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited. | [optional] 
**unauthorized_transactions_count_90d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited. | [optional] 
**nsf_overdraft_transactions_count_7d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited. | [optional] 
**nsf_overdraft_transactions_count_30d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited. | [optional] 
**nsf_overdraft_transactions_count_60d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited. | [optional] 
**nsf_overdraft_transactions_count_90d** | **int** | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited. | [optional] 
**days_since_first_plaid_connection** | **int, none_type** | The number of days since the first time the Item was connected to an application via Plaid | [optional] 
**plaid_connections_count_7d** | **int, none_type** | The number of times the Item has been connected to applications via Plaid over the past 7 days | [optional] 
**plaid_connections_count_30d** | **int, none_type** | The number of times the Item has been connected to applications via Plaid over the past 30 days | [optional] 
**total_plaid_connections_count** | **int, none_type** | The total number of times the Item has been connected to applications via Plaid | [optional] 
**is_savings_or_money_market_account** | **bool** | Indicates if the ACH transaction funding account is a savings/money market account | [optional] 
**total_credit_transactions_amount_10d** | **float** | The total credit (inflow) transaction amount over the past 10 days from the account that will be debited | [optional] 
**total_debit_transactions_amount_10d** | **float** | The total debit (outflow) transaction amount over the past 10 days from the account that will be debited | [optional] 
**p50_credit_transactions_amount_28d** | **float, none_type** | The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited | [optional] 
**p50_debit_transactions_amount_28d** | **float, none_type** | The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited | [optional] 
**p95_credit_transactions_amount_28d** | **float, none_type** | The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited | [optional] 
**p95_debit_transactions_amount_28d** | **float, none_type** | The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited | [optional] 
**days_with_negative_balance_count_90d** | **int, none_type** | The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance | [optional] 
**p90_eod_balance_30d** | **float, none_type** | The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited | [optional] 
**p90_eod_balance_60d** | **float, none_type** | The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited | [optional] 
**p90_eod_balance_90d** | **float, none_type** | The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited | [optional] 
**p10_eod_balance_30d** | **float, none_type** | The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited | [optional] 
**p10_eod_balance_60d** | **float, none_type** | The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited | [optional] 
**p10_eod_balance_90d** | **float, none_type** | The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited | [optional] 
**available_balance** | **float, none_type** | Available balance, as of the &#x60;balance_last_updated&#x60; time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account. | [optional] 
**current_balance** | **float, none_type** | Current balance, as of the &#x60;balance_last_updated&#x60; time. The current balance is the total amount of funds in the account. | [optional] 
**balance_last_updated** | **datetime, none_type** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated. | [optional] 
**phone_change_count_28d** | **int, none_type** | The number of times the account&#39;s phone numbers on file have changed over the past 28 days | [optional] 
**phone_change_count_90d** | **int, none_type** | The number of times the account&#39;s phone numbers on file have changed over the past 90 days | [optional] 
**email_change_count_28d** | **int, none_type** | The number of times the account&#39;s email addresses on file have changed over the past 28 days | [optional] 
**email_change_count_90d** | **int, none_type** | The number of times the account&#39;s email addresses on file have changed over the past 90 days | [optional] 
**address_change_count_28d** | **int, none_type** | The number of times the account&#39;s addresses on file have changed over the past 28 days | [optional] 
**address_change_count_90d** | **int, none_type** | The number of times the account&#39;s addresses on file have changed over the past 90 days | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


