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


class FacilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_facility_by_id(self, facility_id, **kwargs):  # noqa: E501
        """Facility ID  # noqa: E501

        The Facility ID endpoint allows users to search for a facility using its canonical Altana ID. The endpoint returns information on the facility including the company associated with the facility, the products it trades, its industries, facilities it sends to or receives from, and the volume of trade associated with the facility (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_by_id(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: A facility identifier (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facility_by_id_with_http_info(facility_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facility_by_id_with_http_info(facility_id, **kwargs)  # noqa: E501
            return data

    def get_facility_by_id_with_http_info(self, facility_id, **kwargs):  # noqa: E501
        """Facility ID  # noqa: E501

        The Facility ID endpoint allows users to search for a facility using its canonical Altana ID. The endpoint returns information on the facility including the company associated with the facility, the products it trades, its industries, facilities it sends to or receives from, and the volume of trade associated with the facility (via \"number_records\").  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_by_id_with_http_info(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: A facility identifier (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facility_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facility_id' is set
        if ('facility_id' not in params or
                params['facility_id'] is None):
            raise ValueError("Missing the required parameter `facility_id` when calling `get_facility_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facility_id' in params:
            path_params['facility_id'] = params['facility_id']  # noqa: E501

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
            '/facility/id/{facility_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_facility_products(self, facility_id, **kwargs):  # noqa: E501
        """Facility Products  # noqa: E501

        The Facility Products endpoint retrieves the products that a given facility sends or receives.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_products(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: An Altana Canonical Identifier (required)
        :param str trade_direction: Filter products based on the direction of the trade
        :param int page: Page number to return from results (0-99)
        :return: Products
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facility_products_with_http_info(facility_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facility_products_with_http_info(facility_id, **kwargs)  # noqa: E501
            return data

    def get_facility_products_with_http_info(self, facility_id, **kwargs):  # noqa: E501
        """Facility Products  # noqa: E501

        The Facility Products endpoint retrieves the products that a given facility sends or receives.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_products_with_http_info(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: An Altana Canonical Identifier (required)
        :param str trade_direction: Filter products based on the direction of the trade
        :param int page: Page number to return from results (0-99)
        :return: Products
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facility_id', 'trade_direction', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility_products" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facility_id' is set
        if ('facility_id' not in params or
                params['facility_id'] is None):
            raise ValueError("Missing the required parameter `facility_id` when calling `get_facility_products`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facility_id' in params:
            path_params['facility_id'] = params['facility_id']  # noqa: E501

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
            '/facility/id/{facility_id}/products', 'GET',
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

    def get_facility_trading_partners(self, facility_id, **kwargs):  # noqa: E501
        """Facility Trading Partners  # noqa: E501

        The Trading Partners endpoint allows you to retrieve a paginated list of facilities that send to or receive products from the facility in question, along with information about those relationships.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_trading_partners(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: FacilityTradingPartners
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facility_trading_partners_with_http_info(facility_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facility_trading_partners_with_http_info(facility_id, **kwargs)  # noqa: E501
            return data

    def get_facility_trading_partners_with_http_info(self, facility_id, **kwargs):  # noqa: E501
        """Facility Trading Partners  # noqa: E501

        The Trading Partners endpoint allows you to retrieve a paginated list of facilities that send to or receive products from the facility in question, along with information about those relationships.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_trading_partners_with_http_info(facility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facility_id: An Altana Canonical Identifier (required)
        :param int page: Page number to return from results (0-99)
        :return: FacilityTradingPartners
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facility_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility_trading_partners" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facility_id' is set
        if ('facility_id' not in params or
                params['facility_id'] is None):
            raise ValueError("Missing the required parameter `facility_id` when calling `get_facility_trading_partners`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facility_id' in params:
            path_params['facility_id'] = params['facility_id']  # noqa: E501

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
            '/facility/id/{facility_id}/trading-partners', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FacilityTradingPartners',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def match_facility(self, company_name, full_address, **kwargs):  # noqa: E501
        """Facility Match  # noqa: E501

        Facility Match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.match_facility(company_name, full_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_name: The company name to search for (required)
        :param str full_address: The full address or valid GeoJson Polygon to search for (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.match_facility_with_http_info(company_name, full_address, **kwargs)  # noqa: E501
        else:
            (data) = self.match_facility_with_http_info(company_name, full_address, **kwargs)  # noqa: E501
            return data

    def match_facility_with_http_info(self, company_name, full_address, **kwargs):  # noqa: E501
        """Facility Match  # noqa: E501

        Facility Match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.match_facility_with_http_info(company_name, full_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_name: The company name to search for (required)
        :param str full_address: The full address or valid GeoJson Polygon to search for (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_name', 'full_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_name' is set
        if ('company_name' not in params or
                params['company_name'] is None):
            raise ValueError("Missing the required parameter `company_name` when calling `match_facility`")  # noqa: E501
        # verify the required parameter 'full_address' is set
        if ('full_address' not in params or
                params['full_address'] is None):
            raise ValueError("Missing the required parameter `full_address` when calling `match_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_name' in params:
            query_params.append(('company_name', params['company_name']))  # noqa: E501
        if 'full_address' in params:
            query_params.append(('full_address', params['full_address']))  # noqa: E501

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
            '/facility/match', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_facility(self, full_address, company_name, **kwargs):  # noqa: E501
        """Facility Search  # noqa: E501

        Facility Search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_facility(full_address, company_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str full_address: The full address or valid GeoJson Polygon to search for (required)
        :param str company_name: The company name to search for (required)
        :param int page: The Page number to return from results (0-99)
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_facility_with_http_info(full_address, company_name, **kwargs)  # noqa: E501
        else:
            (data) = self.search_facility_with_http_info(full_address, company_name, **kwargs)  # noqa: E501
            return data

    def search_facility_with_http_info(self, full_address, company_name, **kwargs):  # noqa: E501
        """Facility Search  # noqa: E501

        Facility Search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_facility_with_http_info(full_address, company_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str full_address: The full address or valid GeoJson Polygon to search for (required)
        :param str company_name: The company name to search for (required)
        :param int page: The Page number to return from results (0-99)
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['full_address', 'company_name', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'full_address' is set
        if ('full_address' not in params or
                params['full_address'] is None):
            raise ValueError("Missing the required parameter `full_address` when calling `search_facility`")  # noqa: E501
        # verify the required parameter 'company_name' is set
        if ('company_name' not in params or
                params['company_name'] is None):
            raise ValueError("Missing the required parameter `company_name` when calling `search_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'full_address' in params:
            query_params.append(('full_address', params['full_address']))  # noqa: E501
        if 'company_name' in params:
            query_params.append(('company_name', params['company_name']))  # noqa: E501
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
            '/facility/search', 'GET',
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
