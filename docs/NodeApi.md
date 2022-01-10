# swagger_client.NodeApi

All URIs are relative to *https://atlas-api-production-v2.us-east-1.internal.altana.ai/atlas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_node**](NodeApi.md#describe_node) | **GET** /node/{node_type}/describe | 
[**get_node_by_id**](NodeApi.md#get_node_by_id) | **GET** /node/{node_type}/id/{node_id} | 

# **describe_node**
> FieldDescriptions describe_node(node_type)



Returns a description of the fields

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
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))
node_type = 'node_type_example' # str | The type of node being requested

try:
    api_response = api_instance.describe_node(node_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->describe_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| The type of node being requested | 

### Return type

[**FieldDescriptions**](FieldDescriptions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_by_id**
> Node get_node_by_id(node_type, node_id)



Get a node by its ID.

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
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))
node_type = 'node_type_example' # str | The type of node being requested
node_id = 'node_id_example' # str | The ID of the node

try:
    api_response = api_instance.get_node_by_id(node_type, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get_node_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| The type of node being requested | 
 **node_id** | **str**| The ID of the node | 

### Return type

[**Node**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

