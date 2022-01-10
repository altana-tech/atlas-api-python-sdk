# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: v2.0.0-8
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EdgeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def describe_edge(self, edge_type, **kwargs):  # noqa: E501
        """describe_edge  # noqa: E501

        Returns a description of the fields  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_edge(edge_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :return: FieldDescriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_edge_with_http_info(edge_type, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_edge_with_http_info(edge_type, **kwargs)  # noqa: E501
            return data

    def describe_edge_with_http_info(self, edge_type, **kwargs):  # noqa: E501
        """describe_edge  # noqa: E501

        Returns a description of the fields  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_edge_with_http_info(edge_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :return: FieldDescriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edge_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_edge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edge_type' is set
        if ('edge_type' not in params or
                params['edge_type'] is None):
            raise ValueError("Missing the required parameter `edge_type` when calling `describe_edge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edge_type' in params:
            path_params['edge_type'] = params['edge_type']  # noqa: E501

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
            '/edge/{edge_type}/describe', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldDescriptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_edge_by_id(self, edge_type, edge_id, **kwargs):  # noqa: E501
        """get_edge_by_id  # noqa: E501

        Get an edge by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edge_by_id(edge_type, edge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :param str edge_id: The ID of the edge (required)
        :return: Edge
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_edge_by_id_with_http_info(edge_type, edge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_edge_by_id_with_http_info(edge_type, edge_id, **kwargs)  # noqa: E501
            return data

    def get_edge_by_id_with_http_info(self, edge_type, edge_id, **kwargs):  # noqa: E501
        """get_edge_by_id  # noqa: E501

        Get an edge by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edge_by_id_with_http_info(edge_type, edge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :param str edge_id: The ID of the edge (required)
        :return: Edge
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edge_type', 'edge_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edge_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edge_type' is set
        if ('edge_type' not in params or
                params['edge_type'] is None):
            raise ValueError("Missing the required parameter `edge_type` when calling `get_edge_by_id`")  # noqa: E501
        # verify the required parameter 'edge_id' is set
        if ('edge_id' not in params or
                params['edge_id'] is None):
            raise ValueError("Missing the required parameter `edge_id` when calling `get_edge_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edge_type' in params:
            path_params['edge_type'] = params['edge_type']  # noqa: E501
        if 'edge_id' in params:
            path_params['edge_id'] = params['edge_id']  # noqa: E501

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
            '/edge/{edge_type}/id/{edge_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Edge',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_edges_by_source_and_destination(self, edge_type, source_id, destination_id, **kwargs):  # noqa: E501
        """get_edges_by_source_and_destination  # noqa: E501

        Get an edge by its source or destination ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edges_by_source_and_destination(edge_type, source_id, destination_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :param str source_id: The source ID of the edge or \"-\" for any source ID (required)
        :param str destination_id: The destination ID of the edge or \"-\" for any destination ID (required)
        :param int page: Page number to return from results
        :return: Edges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_edges_by_source_and_destination_with_http_info(edge_type, source_id, destination_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_edges_by_source_and_destination_with_http_info(edge_type, source_id, destination_id, **kwargs)  # noqa: E501
            return data

    def get_edges_by_source_and_destination_with_http_info(self, edge_type, source_id, destination_id, **kwargs):  # noqa: E501
        """get_edges_by_source_and_destination  # noqa: E501

        Get an edge by its source or destination ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edges_by_source_and_destination_with_http_info(edge_type, source_id, destination_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_type: The type of edge being requested (required)
        :param str source_id: The source ID of the edge or \"-\" for any source ID (required)
        :param str destination_id: The destination ID of the edge or \"-\" for any destination ID (required)
        :param int page: Page number to return from results
        :return: Edges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edge_type', 'source_id', 'destination_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edges_by_source_and_destination" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edge_type' is set
        if ('edge_type' not in params or
                params['edge_type'] is None):
            raise ValueError("Missing the required parameter `edge_type` when calling `get_edges_by_source_and_destination`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_edges_by_source_and_destination`")  # noqa: E501
        # verify the required parameter 'destination_id' is set
        if ('destination_id' not in params or
                params['destination_id'] is None):
            raise ValueError("Missing the required parameter `destination_id` when calling `get_edges_by_source_and_destination`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edge_type' in params:
            path_params['edge_type'] = params['edge_type']  # noqa: E501
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']  # noqa: E501
        if 'destination_id' in params:
            path_params['destination_id'] = params['destination_id']  # noqa: E501

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
            '/edge/{edge_type}/source/{source_id}/destination/{destination_id}', 'GET',
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