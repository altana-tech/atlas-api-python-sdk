# swagger_client.ProductApi

All URIs are relative to */atlas/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_by_id**](ProductApi.md#get_product_by_id) | **GET** /product/id/{product_id} | Product ID
[**get_product_companies**](ProductApi.md#get_product_companies) | **GET** /product/id/{product_id}/companies | Product Companies
[**get_product_facilities**](ProductApi.md#get_product_facilities) | **GET** /product/id/{product_id}/facilities | Product Facilities

# **get_product_by_id**
> Product get_product_by_id(product_id)

Product ID

The Product ID endpoint allows users to search for a product using its canonical Altana ID.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | A product identifier

try:
    # Product ID
    api_response = api_instance.get_product_by_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A product identifier | 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_companies**
> Companies get_product_companies(product_id, trade_direction=trade_direction, page=page)

Product Companies

The Product Companies endpoint retrieves the companies that send or receive a given product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | An Altana Canonical Identifier
trade_direction = 'trade_direction_example' # str | Filter companies based on the direction of the trade (optional)
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Product Companies
    api_response = api_instance.get_product_companies(product_id, trade_direction=trade_direction, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| An Altana Canonical Identifier | 
 **trade_direction** | **str**| Filter companies based on the direction of the trade | [optional] 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**Companies**](Companies.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_facilities**
> Facilities get_product_facilities(product_id, trade_direction=trade_direction, page=page)

Product Facilities

The Product Facilities endpoint retrieves the facilities that send or receive a given product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | An Altana Canonical Identifier
trade_direction = 'trade_direction_example' # str | Filter facilities based on the direction of the trade (optional)
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Product Facilities
    api_response = api_instance.get_product_facilities(product_id, trade_direction=trade_direction, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| An Altana Canonical Identifier | 
 **trade_direction** | **str**| Filter facilities based on the direction of the trade | [optional] 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**Facilities**](Facilities.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

