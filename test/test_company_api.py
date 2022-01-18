# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: {{ version or \"v0.0.1\" }}
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.company_api import CompanyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCompanyApi(unittest.TestCase):
    """CompanyApi unit test stubs"""

    def setUp(self):
        self.api = CompanyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_company_by_id(self):
        """Test case for get_company_by_id

        Company ID  # noqa: E501
        """
        pass

    def test_get_company_edges(self):
        """Test case for get_company_edges

        Edges  # noqa: E501
        """
        pass

    def test_get_company_facilities(self):
        """Test case for get_company_facilities

        Facilities  # noqa: E501
        """
        pass

    def test_get_company_products(self):
        """Test case for get_company_products

        Company Products  # noqa: E501
        """
        pass

    def test_get_trading_partners(self):
        """Test case for get_trading_partners

        Trading Partners  # noqa: E501
        """
        pass

    def test_match_company(self):
        """Test case for match_company

        Company Match  # noqa: E501
        """
        pass

    def test_search_company(self):
        """Test case for search_company

        Company Search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()