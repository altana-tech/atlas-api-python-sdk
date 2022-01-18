# swagger_client.FacilityApi

All URIs are relative to */atlas/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facility_by_id**](FacilityApi.md#get_facility_by_id) | **GET** /facility/id/{facility_id} | Facility ID
[**get_facility_products**](FacilityApi.md#get_facility_products) | **GET** /facility/id/{facility_id}/products | Facility Products
[**get_facility_trading_partners**](FacilityApi.md#get_facility_trading_partners) | **GET** /facility/id/{facility_id}/trading-partners | Facility Trading Partners
[**match_facility**](FacilityApi.md#match_facility) | **GET** /facility/match | Facility Match
[**search_facility**](FacilityApi.md#search_facility) | **GET** /facility/search | Facility Search

# **get_facility_by_id**
> Facility get_facility_by_id(facility_id)

Facility ID

The Facility ID endpoint allows users to search for a facility using its canonical Altana ID. The endpoint returns information on the facility including the company associated with the facility, the products it trades, its industries, facilities it sends to or receives from, and the volume of trade associated with the facility (via \"number_records\").

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | A facility identifier

try:
    # Facility ID
    api_response = api_instance.get_facility_by_id(facility_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_facility_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| A facility identifier | 

### Return type

[**Facility**](Facility.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_products**
> Products get_facility_products(facility_id, trade_direction=trade_direction, page=page)

Facility Products

The Facility Products endpoint retrieves the products that a given facility sends or receives.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | An Altana Canonical Identifier
trade_direction = 'trade_direction_example' # str | Filter products based on the direction of the trade (optional)
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Facility Products
    api_response = api_instance.get_facility_products(facility_id, trade_direction=trade_direction, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_facility_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| An Altana Canonical Identifier | 
 **trade_direction** | **str**| Filter products based on the direction of the trade | [optional] 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**Products**](Products.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility_trading_partners**
> FacilityTradingPartners get_facility_trading_partners(facility_id, page=page)

Facility Trading Partners

The Trading Partners endpoint allows you to retrieve a paginated list of facilities that send to or receive products from the facility in question, along with information about those relationships.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
facility_id = 'facility_id_example' # str | An Altana Canonical Identifier
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Facility Trading Partners
    api_response = api_instance.get_facility_trading_partners(facility_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_facility_trading_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility_id** | **str**| An Altana Canonical Identifier | 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**FacilityTradingPartners**](FacilityTradingPartners.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_facility**
> Facility match_facility(company_name, full_address)

Facility Match

Facility Match.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
company_name = 'company_name_example' # str | The company name to search for
full_address = 'full_address_example' # str | The full address or valid GeoJson Polygon to search for

try:
    # Facility Match
    api_response = api_instance.match_facility(company_name, full_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->match_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| The company name to search for | 
 **full_address** | **str**| The full address or valid GeoJson Polygon to search for | 

### Return type

[**Facility**](Facility.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_facility**
> Facilities search_facility(full_address, company_name, page=page)

Facility Search

Facility Search.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
full_address = 'full_address_example' # str | The full address or valid GeoJson Polygon to search for
company_name = 'company_name_example' # str | The company name to search for
page = 56 # int | The Page number to return from results (0-99) (optional)

try:
    # Facility Search
    api_response = api_instance.search_facility(full_address, company_name, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->search_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_address** | **str**| The full address or valid GeoJson Polygon to search for | 
 **company_name** | **str**| The company name to search for | 
 **page** | **int**| The Page number to return from results (0-99) | [optional] 

### Return type

[**Facilities**](Facilities.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

