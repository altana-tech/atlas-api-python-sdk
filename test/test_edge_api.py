# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: v2.0.0-8
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.edge_api import EdgeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEdgeApi(unittest.TestCase):
    """EdgeApi unit test stubs"""

    def setUp(self):
        self.api = EdgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_describe_edge(self):
        """Test case for describe_edge

        """
        pass

    def test_get_edge_by_id(self):
        """Test case for get_edge_by_id

        """
        pass

    def test_get_edges_by_source_and_destination(self):
        """Test case for get_edges_by_source_and_destination

        """
        pass


if __name__ == '__main__':
    unittest.main()