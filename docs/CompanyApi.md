# swagger_client.CompanyApi

All URIs are relative to */atlas/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_by_id**](CompanyApi.md#get_company_by_id) | **GET** /company/id/{company_id} | Company ID
[**get_company_edges**](CompanyApi.md#get_company_edges) | **GET** /company/id/{company_id}/edges | Edges
[**get_company_facilities**](CompanyApi.md#get_company_facilities) | **GET** /company/id/{company_id}/facilities | Facilities
[**get_company_products**](CompanyApi.md#get_company_products) | **GET** /company/id/{company_id}/products | Company Products
[**get_trading_partners**](CompanyApi.md#get_trading_partners) | **GET** /company/id/{company_id}/trading-partners | Trading Partners
[**match_company**](CompanyApi.md#match_company) | **GET** /company/match/{query} | Company Match
[**search_company**](CompanyApi.md#search_company) | **GET** /company/search/{query} | Company Search

# **get_company_by_id**
> Company get_company_by_id(company_id)

Company ID

The Company ID endpoint allows users to search for a company using its canonical Altana ID. The endpoint returns information on the company including the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | A company identifier

try:
    # Company ID
    api_response = api_instance.get_company_by_id(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| A company identifier | 

### Return type

[**Company**](Company.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_edges**
> Edges get_company_edges(company_id, edge_type=edge_type, country=country, trade_direction=trade_direction, page=page)

Edges

The Edges endpoint retrieves the links (i.e., edges) associated with a given company in the knowledge graph. Currently these edges describe trade relationships (\"trading_partners\"), while allowing filtering by recipient (\"receives_from\") or sender (\"sends_to\").

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | An Altana Canonical Identifier
edge_type = ['edge_type_example'] # list[str] | A list of edge_type filters (optional)
country = ['country_example'] # list[str] | A list of ISO-2 country codes to filter by (optional)
trade_direction = 'trade_direction_example' # str | Filter trade-based edges on the direction of the trade (optional)
page = 56 # int | Page number to return from results (optional)

try:
    # Edges
    api_response = api_instance.get_company_edges(company_id, edge_type=edge_type, country=country, trade_direction=trade_direction, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| An Altana Canonical Identifier | 
 **edge_type** | [**list[str]**](str.md)| A list of edge_type filters | [optional] 
 **country** | [**list[str]**](str.md)| A list of ISO-2 country codes to filter by | [optional] 
 **trade_direction** | **str**| Filter trade-based edges on the direction of the trade | [optional] 
 **page** | **int**| Page number to return from results | [optional] 

### Return type

[**Edges**](Edges.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_facilities**
> Facilities get_company_facilities(company_id, page=page)

Facilities

The Company Facilities endpoint retrieves the facilities associated with a given company.

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | An Altana Canonical Identifier
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Facilities
    api_response = api_instance.get_company_facilities(company_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| An Altana Canonical Identifier | 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**Facilities**](Facilities.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_products**
> Products get_company_products(company_id, trade_direction=trade_direction, page=page)

Company Products

The Company Products endpoint retrieves the products that a given company sends or receives.

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | An Altana Canonical Identifier
trade_direction = 'trade_direction_example' # str | Filter products based on the direction of the trade (optional)
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Company Products
    api_response = api_instance.get_company_products(company_id, trade_direction=trade_direction, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| An Altana Canonical Identifier | 
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

# **get_trading_partners**
> TradingPartners get_trading_partners(company_id, page=page)

Trading Partners

The Trading Partners endpoint allows you to retrieve a paginated list of companies that buy from or sell to the company in question, along with information about those relationships.

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | An Altana Canonical Identifier
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Trading Partners
    api_response = api_instance.get_trading_partners(company_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_trading_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| An Altana Canonical Identifier | 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**TradingPartners**](TradingPartners.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_company**
> Company match_company(query, country=country, full_address=full_address, hs2=hs2, has_restrictions=has_restrictions)

Company Match

The Company Match Endpoint.

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | A company name
country = ['country_example'] # list[str] | A list of ISO-2 country codes to filter by (optional)
full_address = 'full_address_example' # str | The full address to search for (optional)
hs2 = ['hs2_example'] # list[str] | A list of HS2 product categories to filter by (optional)
has_restrictions = true # bool | Filter for companies that have restrictions (optional)

try:
    # Company Match
    api_response = api_instance.match_company(query, country=country, full_address=full_address, hs2=hs2, has_restrictions=has_restrictions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->match_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A company name | 
 **country** | [**list[str]**](str.md)| A list of ISO-2 country codes to filter by | [optional] 
 **full_address** | **str**| The full address to search for | [optional] 
 **hs2** | [**list[str]**](str.md)| A list of HS2 product categories to filter by | [optional] 
 **has_restrictions** | **bool**| Filter for companies that have restrictions | [optional] 

### Return type

[**Company**](Company.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_company**
> Companies search_company(query, country=country, hs2=hs2, has_restrictions=has_restrictions, page=page)

Company Search

The Company Search endpoint allows users to search for companies by name. The endpoint returns the Altana IDs for companies matching that name, ordered by search relevance, as well as information on the company including: the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | A company name, variant, identifier, or query term
country = ['country_example'] # list[str] | A list of ISO-2 country codes to filter by (optional)
hs2 = ['hs2_example'] # list[str] | A list of HS2 product categories to filter by (optional)
has_restrictions = true # bool | Filter for companies that have restrictions (optional)
page = 56 # int | Page number to return from results (0-99) (optional)

try:
    # Company Search
    api_response = api_instance.search_company(query, country=country, hs2=hs2, has_restrictions=has_restrictions, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->search_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A company name, variant, identifier, or query term | 
 **country** | [**list[str]**](str.md)| A list of ISO-2 country codes to filter by | [optional] 
 **hs2** | [**list[str]**](str.md)| A list of HS2 product categories to filter by | [optional] 
 **has_restrictions** | **bool**| Filter for companies that have restrictions | [optional] 
 **page** | **int**| Page number to return from results (0-99) | [optional] 

### Return type

[**Companies**](Companies.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

