# swagger_client.TransactionApi

All URIs are relative to */atlas/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_risk**](TransactionApi.md#transaction_risk) | **POST** /transaction/risk | Transaction Risk

# **transaction_risk**
> TransactionRisk transaction_risk(body=body)

Transaction Risk

The Transaction Risk endpoint takes in details from a shipping transaction (i.e., a customs declaration, manifest, bill of lading, etc.) in a standard json format and returns an array of risks associated with that transaction.  The base risks that Altana returns currently in this endpoint include security risk, narcotics risk, and money laundering risk.  The risks are returned in an array to allow easy extensibility.  More risks calibrated to the country at hand, such as fiscal (tax evasion) risks, supervised models trained on enforcement results, and anomaly detection models, are easily added without breaking integrations.  The minimum required input fields for this endpoint are \"goods_description,\" \"hs_code,\" and the countries of origin and destination (ISO-2 codes).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransactionRecord() # TransactionRecord | Cross-Border Transaction Records (optional)

try:
    # Transaction Risk
    api_response = api_instance.transaction_risk(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->transaction_risk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRecord**](TransactionRecord.md)| Cross-Border Transaction Records | [optional] 

### Return type

[**TransactionRisk**](TransactionRisk.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

