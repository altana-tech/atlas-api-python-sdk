# swagger_client.DefaultApi

All URIs are relative to *https://atlas-api-production-v2.us-east-1.internal.altana.ai/atlas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_types**](DefaultApi.md#get_types) | **GET** /types | 

# **get_types**
> Types get_types()



Get node and edge types of the knowledge graph

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Types**](Types.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

