# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: v2.0.0-8
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.base_edge import BaseEdge  # noqa: F401,E501

class CompanySendsToSummarizedEdge(BaseEdge):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'company_sends_to_summarized_id': 'str',
        'country_of_destination_summary': 'list[CountryCount]',
        'country_of_origin_summary': 'list[CountryCount]',
        'destination_id': 'str',
        'hs_codes_sent': 'list[HSCodeCount]',
        'number_of_shipments': 'int',
        'source_id': 'str',
        'sources': 'list[str]'
    }
    if hasattr(BaseEdge, "swagger_types"):
        swagger_types.update(BaseEdge.swagger_types)

    attribute_map = {
        'company_sends_to_summarized_id': 'company_sends_to_summarized_id',
        'country_of_destination_summary': 'country_of_destination_summary',
        'country_of_origin_summary': 'country_of_origin_summary',
        'destination_id': 'destination_id',
        'hs_codes_sent': 'hs_codes_sent',
        'number_of_shipments': 'number_of_shipments',
        'source_id': 'source_id',
        'sources': 'sources'
    }
    if hasattr(BaseEdge, "attribute_map"):
        attribute_map.update(BaseEdge.attribute_map)

    def __init__(self, company_sends_to_summarized_id=None, country_of_destination_summary=None, country_of_origin_summary=None, destination_id=None, hs_codes_sent=None, number_of_shipments=None, source_id=None, sources=None, *args, **kwargs):  # noqa: E501
        """CompanySendsToSummarizedEdge - a model defined in Swagger"""  # noqa: E501
        self._company_sends_to_summarized_id = None
        self._country_of_destination_summary = None
        self._country_of_origin_summary = None
        self._destination_id = None
        self._hs_codes_sent = None
        self._number_of_shipments = None
        self._source_id = None
        self._sources = None
        self.discriminator = None
        if company_sends_to_summarized_id is not None:
            self.company_sends_to_summarized_id = company_sends_to_summarized_id
        if country_of_destination_summary is not None:
            self.country_of_destination_summary = country_of_destination_summary
        if country_of_origin_summary is not None:
            self.country_of_origin_summary = country_of_origin_summary
        if destination_id is not None:
            self.destination_id = destination_id
        if hs_codes_sent is not None:
            self.hs_codes_sent = hs_codes_sent
        if number_of_shipments is not None:
            self.number_of_shipments = number_of_shipments
        if source_id is not None:
            self.source_id = source_id
        if sources is not None:
            self.sources = sources
        BaseEdge.__init__(self, *args, **kwargs)

    @property
    def company_sends_to_summarized_id(self):
        """Gets the company_sends_to_summarized_id of this CompanySendsToSummarizedEdge.  # noqa: E501

        A unique identifier for a company sends to summarized edge  # noqa: E501

        :return: The company_sends_to_summarized_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: str
        """
        return self._company_sends_to_summarized_id

    @company_sends_to_summarized_id.setter
    def company_sends_to_summarized_id(self, company_sends_to_summarized_id):
        """Sets the company_sends_to_summarized_id of this CompanySendsToSummarizedEdge.

        A unique identifier for a company sends to summarized edge  # noqa: E501

        :param company_sends_to_summarized_id: The company_sends_to_summarized_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: str
        """

        self._company_sends_to_summarized_id = company_sends_to_summarized_id

    @property
    def country_of_destination_summary(self):
        """Gets the country_of_destination_summary of this CompanySendsToSummarizedEdge.  # noqa: E501

        A list of dictionaries of country of destination ALPHA ISO-2 codes to transaction counts  # noqa: E501

        :return: The country_of_destination_summary of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: list[CountryCount]
        """
        return self._country_of_destination_summary

    @country_of_destination_summary.setter
    def country_of_destination_summary(self, country_of_destination_summary):
        """Sets the country_of_destination_summary of this CompanySendsToSummarizedEdge.

        A list of dictionaries of country of destination ALPHA ISO-2 codes to transaction counts  # noqa: E501

        :param country_of_destination_summary: The country_of_destination_summary of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: list[CountryCount]
        """

        self._country_of_destination_summary = country_of_destination_summary

    @property
    def country_of_origin_summary(self):
        """Gets the country_of_origin_summary of this CompanySendsToSummarizedEdge.  # noqa: E501

        A list of dictionaries of country of origin ALPHA ISO-2 codes to transaction counts  # noqa: E501

        :return: The country_of_origin_summary of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: list[CountryCount]
        """
        return self._country_of_origin_summary

    @country_of_origin_summary.setter
    def country_of_origin_summary(self, country_of_origin_summary):
        """Sets the country_of_origin_summary of this CompanySendsToSummarizedEdge.

        A list of dictionaries of country of origin ALPHA ISO-2 codes to transaction counts  # noqa: E501

        :param country_of_origin_summary: The country_of_origin_summary of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: list[CountryCount]
        """

        self._country_of_origin_summary = country_of_origin_summary

    @property
    def destination_id(self):
        """Gets the destination_id of this CompanySendsToSummarizedEdge.  # noqa: E501

        The company_canon_id of the destination company  # noqa: E501

        :return: The destination_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this CompanySendsToSummarizedEdge.

        The company_canon_id of the destination company  # noqa: E501

        :param destination_id: The destination_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: str
        """

        self._destination_id = destination_id

    @property
    def hs_codes_sent(self):
        """Gets the hs_codes_sent of this CompanySendsToSummarizedEdge.  # noqa: E501

        A list of dictionaries of the HS codes of sent goods to transaction counts  # noqa: E501

        :return: The hs_codes_sent of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: list[HSCodeCount]
        """
        return self._hs_codes_sent

    @hs_codes_sent.setter
    def hs_codes_sent(self, hs_codes_sent):
        """Sets the hs_codes_sent of this CompanySendsToSummarizedEdge.

        A list of dictionaries of the HS codes of sent goods to transaction counts  # noqa: E501

        :param hs_codes_sent: The hs_codes_sent of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: list[HSCodeCount]
        """

        self._hs_codes_sent = hs_codes_sent

    @property
    def number_of_shipments(self):
        """Gets the number_of_shipments of this CompanySendsToSummarizedEdge.  # noqa: E501

        The number of shipments represented by the summarized edge  # noqa: E501

        :return: The number_of_shipments of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: int
        """
        return self._number_of_shipments

    @number_of_shipments.setter
    def number_of_shipments(self, number_of_shipments):
        """Sets the number_of_shipments of this CompanySendsToSummarizedEdge.

        The number of shipments represented by the summarized edge  # noqa: E501

        :param number_of_shipments: The number_of_shipments of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: int
        """

        self._number_of_shipments = number_of_shipments

    @property
    def source_id(self):
        """Gets the source_id of this CompanySendsToSummarizedEdge.  # noqa: E501

        The company_canon_id of the source company  # noqa: E501

        :return: The source_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CompanySendsToSummarizedEdge.

        The company_canon_id of the source company  # noqa: E501

        :param source_id: The source_id of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def sources(self):
        """Gets the sources of this CompanySendsToSummarizedEdge.  # noqa: E501

        A list of data sources for the information  # noqa: E501

        :return: The sources of this CompanySendsToSummarizedEdge.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this CompanySendsToSummarizedEdge.

        A list of data sources for the information  # noqa: E501

        :param sources: The sources of this CompanySendsToSummarizedEdge.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CompanySendsToSummarizedEdge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompanySendsToSummarizedEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
