# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: {{ version or \"v0.0.1\" }}
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CompanyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_company_by_id(self, company_id, **kwargs):  # noqa: E501
        """Company ID  # noqa: E501

        The Company ID endpoint allows users to search for a company using its canonical Altana ID. The endpoint returns information on the company including the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_by_id(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: A company identifier (required)
        :return: Company
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_by_id_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_by_id_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_by_id_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Company ID  # noqa: E501

        The Company ID endpoint allows users to search for a company using its canonical Altana ID. The endpoint returns information on the company including the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_by_id_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: A company identifier (required)
        :return: Company
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['company_id'] = params['company_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/id/{company_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Company',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_edges(self, company_id, **kwargs):  # noqa: E501
        """Edges  # noqa: E501

        The Edges endpoint retrieves the links (i.e., edges) associated with a given company in the knowledge graph. Currently these edges describe trade relationships (\"trading_partners\"), while allowing filtering by recipient (\"receives_from\") or sender (\"sends_to\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_edges(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param list[str] edge_type: A list of edge_type filters
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param str trade_direction: Filter trade-based edges on the direction of the trade
        :param int page: Page number to return from results
        :return: Edges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_edges_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_edges_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_edges_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Edges  # noqa: E501

        The Edges endpoint retrieves the links (i.e., edges) associated with a given company in the knowledge graph. Currently these edges describe trade relationships (\"trading_partners\"), while allowing filtering by recipient (\"receives_from\") or sender (\"sends_to\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_edges_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param list[str] edge_type: A list of edge_type filters
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param str trade_direction: Filter trade-based edges on the direction of the trade
        :param int page: Page number to return from results
        :return: Edges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'edge_type', 'country', 'trade_direction', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_edges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_edges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['company_id'] = params['company_id']  # noqa: E501

        query_params = []
        if 'edge_type' in params:
            query_params.append(('edge_type', params['edge_type']))  # noqa: E501
            collection_formats['edge_type'] = 'pipe'  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
            collection_formats['country'] = 'pipe'  # noqa: E501
        if 'trade_direction' in params:
            query_params.append(('trade_direction', params['trade_direction']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/id/{company_id}/edges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Edges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_facilities(self, company_id, **kwargs):  # noqa: E501
        """Facilities  # noqa: E501

        The Company Facilities endpoint retrieves the facilities associated with a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_facilities(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_facilities_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_facilities_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_facilities_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Facilities  # noqa: E501

        The Company Facilities endpoint retrieves the facilities associated with a given company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_facilities_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_facilities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_facilities`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['company_id'] = params['company_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/id/{company_id}/facilities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facilities',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_products(self, company_id, **kwargs):  # noqa: E501
        """Company Products  # noqa: E501

        The Company Products endpoint retrieves the products that a given company sends or receives.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_products(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param str trade_direction: Filter products based on the direction of the trade
        :param int page: Page number to return from results (0-99)
        :return: Products
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_products_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_products_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_products_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Company Products  # noqa: E501

        The Company Products endpoint retrieves the products that a given company sends or receives.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_products_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param str trade_direction: Filter products based on the direction of the trade
        :param int page: Page number to return from results (0-99)
        :return: Products
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'trade_direction', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_products" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_products`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['company_id'] = params['company_id']  # noqa: E501

        query_params = []
        if 'trade_direction' in params:
            query_params.append(('trade_direction', params['trade_direction']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/id/{company_id}/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Products',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_trading_partners(self, company_id, **kwargs):  # noqa: E501
        """Trading Partners  # noqa: E501

        The Trading Partners endpoint allows you to retrieve a paginated list of companies that buy from or sell to the company in question, along with information about those relationships.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trading_partners(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: TradingPartners
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trading_partners_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trading_partners_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_trading_partners_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Trading Partners  # noqa: E501

        The Trading Partners endpoint allows you to retrieve a paginated list of companies that buy from or sell to the company in question, along with information about those relationships.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trading_partners_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: TradingPartners
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trading_partners" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_trading_partners`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['company_id'] = params['company_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/id/{company_id}/trading-partners', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradingPartners',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def match_company(self, query, **kwargs):  # noqa: E501
        """Company Match  # noqa: E501

        The Company Match Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.match_company(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: A company name (required)
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param str full_address: The full address to search for
        :param list[str] hs2: A list of HS2 product categories to filter by
        :param bool has_restrictions: Filter for companies that have restrictions
        :return: Company
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.match_company_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.match_company_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def match_company_with_http_info(self, query, **kwargs):  # noqa: E501
        """Company Match  # noqa: E501

        The Company Match Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.match_company_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: A company name (required)
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param str full_address: The full address to search for
        :param list[str] hs2: A list of HS2 product categories to filter by
        :param bool has_restrictions: Filter for companies that have restrictions
        :return: Company
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'country', 'full_address', 'hs2', 'has_restrictions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_company" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `match_company`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
            collection_formats['country'] = 'pipe'  # noqa: E501
        if 'full_address' in params:
            query_params.append(('full_address', params['full_address']))  # noqa: E501
        if 'hs2' in params:
            query_params.append(('hs2', params['hs2']))  # noqa: E501
            collection_formats['hs2'] = 'pipe'  # noqa: E501
        if 'has_restrictions' in params:
            query_params.append(('has_restrictions', params['has_restrictions']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/match/{query}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Company',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_company(self, query, **kwargs):  # noqa: E501
        """Company Search  # noqa: E501

        The Company Search endpoint allows users to search for companies by name. The endpoint returns the Altana IDs for companies matching that name, ordered by search relevance, as well as information on the company including: the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_company(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: A company name, variant, identifier, or query term (required)
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param list[str] hs2: A list of HS2 product categories to filter by
        :param bool has_restrictions: Filter for companies that have restrictions
        :param int page: Page number to return from results (0-99)
        :return: Companies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_company_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_company_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_company_with_http_info(self, query, **kwargs):  # noqa: E501
        """Company Search  # noqa: E501

        The Company Search endpoint allows users to search for companies by name. The endpoint returns the Altana IDs for companies matching that name, ordered by search relevance, as well as information on the company including: the products it trades, its industries, its buyers and suppliers, the risks and restrictions (i.e., sanctions, export controls, etc.) associated with the company, and the volume of trade associated with the company (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_company_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: A company name, variant, identifier, or query term (required)
        :param list[str] country: A list of ISO-2 country codes to filter by
        :param list[str] hs2: A list of HS2 product categories to filter by
        :param bool has_restrictions: Filter for companies that have restrictions
        :param int page: Page number to return from results (0-99)
        :return: Companies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'country', 'hs2', 'has_restrictions', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_company" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_company`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
            collection_formats['country'] = 'pipe'  # noqa: E501
        if 'hs2' in params:
            query_params.append(('hs2', params['hs2']))  # noqa: E501
            collection_formats['hs2'] = 'pipe'  # noqa: E501
        if 'has_restrictions' in params:
            query_params.append(('has_restrictions', params['has_restrictions']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/company/search/{query}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Companies',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)