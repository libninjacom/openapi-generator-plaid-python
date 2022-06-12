# InstitutionStatus

The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.  Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_logins** | [**ProductStatus**](ProductStatus.md) |  | 
**transactions_updates** | [**ProductStatus**](ProductStatus.md) |  | 
**auth** | [**ProductStatus**](ProductStatus.md) |  | 
**identity** | [**ProductStatus**](ProductStatus.md) |  | 
**investments_updates** | [**ProductStatus**](ProductStatus.md) |  | 
**liabilities_updates** | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**liabilities** | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**investments** | [**ProductStatus**](ProductStatus.md) |  | [optional] 
**health_incidents** | [**[HealthIncident], none_type**](HealthIncident.md) | Details of recent health incidents associated with the institution. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


