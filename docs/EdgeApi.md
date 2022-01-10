# swagger_client.EdgeApi

All URIs are relative to *https://atlas-api-production-v2.us-east-1.internal.altana.ai/atlas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_edge**](EdgeApi.md#describe_edge) | **GET** /edge/{edge_type}/describe | 
[**get_edge_by_id**](EdgeApi.md#get_edge_by_id) | **GET** /edge/{edge_type}/id/{edge_id} | 
[**get_edges_by_source_and_destination**](EdgeApi.md#get_edges_by_source_and_destination) | **GET** /edge/{edge_type}/source/{source_id}/destination/{destination_id} | 

# **describe_edge**
> FieldDescriptions describe_edge(edge_type)



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
api_instance = swagger_client.EdgeApi(swagger_client.ApiClient(configuration))
edge_type = 'edge_type_example' # str | The type of edge being requested

try:
    api_response = api_instance.describe_edge(edge_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeApi->describe_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| The type of edge being requested | 

### Return type

[**FieldDescriptions**](FieldDescriptions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_by_id**
> Edge get_edge_by_id(edge_type, edge_id)



Get an edge by its ID

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
api_instance = swagger_client.EdgeApi(swagger_client.ApiClient(configuration))
edge_type = 'edge_type_example' # str | The type of edge being requested
edge_id = 'edge_id_example' # str | The ID of the edge

try:
    api_response = api_instance.get_edge_by_id(edge_type, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeApi->get_edge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| The type of edge being requested | 
 **edge_id** | **str**| The ID of the edge | 

### Return type

[**Edge**](Edge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edges_by_source_and_destination**
> Edges get_edges_by_source_and_destination(edge_type, source_id, destination_id, page=page)



Get an edge by its source or destination ID

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
api_instance = swagger_client.EdgeApi(swagger_client.ApiClient(configuration))
edge_type = 'edge_type_example' # str | The type of edge being requested
source_id = 'source_id_example' # str | The source ID of the edge or \"-\" for any source ID
destination_id = 'destination_id_example' # str | The destination ID of the edge or \"-\" for any destination ID
page = 56 # int | Page number to return from results (optional)

try:
    api_response = api_instance.get_edges_by_source_and_destination(edge_type, source_id, destination_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeApi->get_edges_by_source_and_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_type** | **str**| The type of edge being requested | 
 **source_id** | **str**| The source ID of the edge or \&quot;-\&quot; for any source ID | 
 **destination_id** | **str**| The destination ID of the edge or \&quot;-\&quot; for any destination ID | 
 **page** | **int**| Page number to return from results | [optional] 

### Return type

[**Edges**](Edges.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

