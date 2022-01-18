# swagger-client
Altana Atlas for Regulatory Risk and Trade Compliance

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.0.136
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/altana-tech/atlas-api-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/altana-tech/atlas-api-python-sdk.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to */atlas/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompanyApi* | [**get_company_by_id**](docs/CompanyApi.md#get_company_by_id) | **GET** /company/id/{company_id} | Company ID
*CompanyApi* | [**get_company_edges**](docs/CompanyApi.md#get_company_edges) | **GET** /company/id/{company_id}/edges | Edges
*CompanyApi* | [**get_company_facilities**](docs/CompanyApi.md#get_company_facilities) | **GET** /company/id/{company_id}/facilities | Facilities
*CompanyApi* | [**get_company_products**](docs/CompanyApi.md#get_company_products) | **GET** /company/id/{company_id}/products | Company Products
*CompanyApi* | [**get_trading_partners**](docs/CompanyApi.md#get_trading_partners) | **GET** /company/id/{company_id}/trading-partners | Trading Partners
*CompanyApi* | [**match_company**](docs/CompanyApi.md#match_company) | **GET** /company/match/{query} | Company Match
*CompanyApi* | [**search_company**](docs/CompanyApi.md#search_company) | **GET** /company/search/{query} | Company Search
*FacilityApi* | [**get_facility_by_id**](docs/FacilityApi.md#get_facility_by_id) | **GET** /facility/id/{facility_id} | Facility ID
*FacilityApi* | [**get_facility_products**](docs/FacilityApi.md#get_facility_products) | **GET** /facility/id/{facility_id}/products | Facility Products
*FacilityApi* | [**get_facility_trading_partners**](docs/FacilityApi.md#get_facility_trading_partners) | **GET** /facility/id/{facility_id}/trading-partners | Facility Trading Partners
*FacilityApi* | [**match_facility**](docs/FacilityApi.md#match_facility) | **GET** /facility/match | Facility Match
*FacilityApi* | [**search_facility**](docs/FacilityApi.md#search_facility) | **GET** /facility/search | Facility Search
*ProductApi* | [**get_product_by_id**](docs/ProductApi.md#get_product_by_id) | **GET** /product/id/{product_id} | Product ID
*ProductApi* | [**get_product_companies**](docs/ProductApi.md#get_product_companies) | **GET** /product/id/{product_id}/companies | Product Companies
*ProductApi* | [**get_product_facilities**](docs/ProductApi.md#get_product_facilities) | **GET** /product/id/{product_id}/facilities | Product Facilities
*TransactionApi* | [**transaction_risk**](docs/TransactionApi.md#transaction_risk) | **POST** /transaction/risk | Transaction Risk

## Documentation For Models

 - [BaseEdge](docs/BaseEdge.md)
 - [BaseRisk](docs/BaseRisk.md)
 - [Companies](docs/Companies.md)
 - [Company](docs/Company.md)
 - [CompanyContext](docs/CompanyContext.md)
 - [Coordinates](docs/Coordinates.md)
 - [DeclaredGoods](docs/DeclaredGoods.md)
 - [Edge](docs/Edge.md)
 - [Edges](docs/Edges.md)
 - [Facilities](docs/Facilities.md)
 - [Facility](docs/Facility.md)
 - [FacilityTradingPartners](docs/FacilityTradingPartners.md)
 - [GeoCoderMetaData](docs/GeoCoderMetaData.md)
 - [GoodsMeasure](docs/GoodsMeasure.md)
 - [HSMisclassificationRisk](docs/HSMisclassificationRisk.md)
 - [InterFacilityEdge](docs/InterFacilityEdge.md)
 - [ModelMetaData](docs/ModelMetaData.md)
 - [OneOfEdge](docs/OneOfEdge.md)
 - [OneOfRisk](docs/OneOfRisk.md)
 - [Party](docs/Party.md)
 - [PredictedGoods](docs/PredictedGoods.md)
 - [Product](docs/Product.md)
 - [Products](docs/Products.md)
 - [Restriction](docs/Restriction.md)
 - [Risk](docs/Risk.md)
 - [Tariff](docs/Tariff.md)
 - [TradeRelationship](docs/TradeRelationship.md)
 - [TradeRoute](docs/TradeRoute.md)
 - [TradingPartnerEdge](docs/TradingPartnerEdge.md)
 - [TradingPartners](docs/TradingPartners.md)
 - [TradingPartnersEdge](docs/TradingPartnersEdge.md)
 - [TransactionRecord](docs/TransactionRecord.md)
 - [TransactionRisk](docs/TransactionRisk.md)

## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## Author

engineering@altanatech.com
