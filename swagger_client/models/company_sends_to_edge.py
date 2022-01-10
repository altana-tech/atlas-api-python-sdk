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

class CompanySendsToEdge(BaseEdge):
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
        'company_sends_to_id': 'str',
        'destination_id': 'str',
        'goods_description': 'str',
        'hs_code_raw': 'str',
        'source_id': 'str',
        'sources': 'list[str]',
        'transaction_date_time': 'datetime'
    }
    if hasattr(BaseEdge, "swagger_types"):
        swagger_types.update(BaseEdge.swagger_types)

    attribute_map = {
        'company_sends_to_id': 'company_sends_to_id',
        'destination_id': 'destination_id',
        'goods_description': 'goods_description',
        'hs_code_raw': 'hs_code_raw',
        'source_id': 'source_id',
        'sources': 'sources',
        'transaction_date_time': 'transaction_date_time'
    }
    if hasattr(BaseEdge, "attribute_map"):
        attribute_map.update(BaseEdge.attribute_map)

    def __init__(self, company_sends_to_id=None, destination_id=None, goods_description=None, hs_code_raw=None, source_id=None, sources=None, transaction_date_time=None, *args, **kwargs):  # noqa: E501
        """CompanySendsToEdge - a model defined in Swagger"""  # noqa: E501
        self._company_sends_to_id = None
        self._destination_id = None
        self._goods_description = None
        self._hs_code_raw = None
        self._source_id = None
        self._sources = None
        self._transaction_date_time = None
        self.discriminator = None
        if company_sends_to_id is not None:
            self.company_sends_to_id = company_sends_to_id
        if destination_id is not None:
            self.destination_id = destination_id
        if goods_description is not None:
            self.goods_description = goods_description
        if hs_code_raw is not None:
            self.hs_code_raw = hs_code_raw
        if source_id is not None:
            self.source_id = source_id
        if sources is not None:
            self.sources = sources
        if transaction_date_time is not None:
            self.transaction_date_time = transaction_date_time
        BaseEdge.__init__(self, *args, **kwargs)

    @property
    def company_sends_to_id(self):
        """Gets the company_sends_to_id of this CompanySendsToEdge.  # noqa: E501

        A unique identifier for a company sends to edge  # noqa: E501

        :return: The company_sends_to_id of this CompanySendsToEdge.  # noqa: E501
        :rtype: str
        """
        return self._company_sends_to_id

    @company_sends_to_id.setter
    def company_sends_to_id(self, company_sends_to_id):
        """Sets the company_sends_to_id of this CompanySendsToEdge.

        A unique identifier for a company sends to edge  # noqa: E501

        :param company_sends_to_id: The company_sends_to_id of this CompanySendsToEdge.  # noqa: E501
        :type: str
        """

        self._company_sends_to_id = company_sends_to_id

    @property
    def destination_id(self):
        """Gets the destination_id of this CompanySendsToEdge.  # noqa: E501

        The company_canon_id of the destination company  # noqa: E501

        :return: The destination_id of this CompanySendsToEdge.  # noqa: E501
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this CompanySendsToEdge.

        The company_canon_id of the destination company  # noqa: E501

        :param destination_id: The destination_id of this CompanySendsToEdge.  # noqa: E501
        :type: str
        """

        self._destination_id = destination_id

    @property
    def goods_description(self):
        """Gets the goods_description of this CompanySendsToEdge.  # noqa: E501

        The goods description of the shipment moving between companies  # noqa: E501

        :return: The goods_description of this CompanySendsToEdge.  # noqa: E501
        :rtype: str
        """
        return self._goods_description

    @goods_description.setter
    def goods_description(self, goods_description):
        """Sets the goods_description of this CompanySendsToEdge.

        The goods description of the shipment moving between companies  # noqa: E501

        :param goods_description: The goods_description of this CompanySendsToEdge.  # noqa: E501
        :type: str
        """

        self._goods_description = goods_description

    @property
    def hs_code_raw(self):
        """Gets the hs_code_raw of this CompanySendsToEdge.  # noqa: E501

        The raw HS classification code of the goods description coming directly from the data source  # noqa: E501

        :return: The hs_code_raw of this CompanySendsToEdge.  # noqa: E501
        :rtype: str
        """
        return self._hs_code_raw

    @hs_code_raw.setter
    def hs_code_raw(self, hs_code_raw):
        """Sets the hs_code_raw of this CompanySendsToEdge.

        The raw HS classification code of the goods description coming directly from the data source  # noqa: E501

        :param hs_code_raw: The hs_code_raw of this CompanySendsToEdge.  # noqa: E501
        :type: str
        """

        self._hs_code_raw = hs_code_raw

    @property
    def source_id(self):
        """Gets the source_id of this CompanySendsToEdge.  # noqa: E501

        The company_canon_id of the source company  # noqa: E501

        :return: The source_id of this CompanySendsToEdge.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CompanySendsToEdge.

        The company_canon_id of the source company  # noqa: E501

        :param source_id: The source_id of this CompanySendsToEdge.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def sources(self):
        """Gets the sources of this CompanySendsToEdge.  # noqa: E501

        A list of data sources for the information  # noqa: E501

        :return: The sources of this CompanySendsToEdge.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this CompanySendsToEdge.

        A list of data sources for the information  # noqa: E501

        :param sources: The sources of this CompanySendsToEdge.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def transaction_date_time(self):
        """Gets the transaction_date_time of this CompanySendsToEdge.  # noqa: E501

        The datetime of the underlying transaction  # noqa: E501

        :return: The transaction_date_time of this CompanySendsToEdge.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date_time

    @transaction_date_time.setter
    def transaction_date_time(self, transaction_date_time):
        """Sets the transaction_date_time of this CompanySendsToEdge.

        The datetime of the underlying transaction  # noqa: E501

        :param transaction_date_time: The transaction_date_time of this CompanySendsToEdge.  # noqa: E501
        :type: datetime
        """

        self._transaction_date_time = transaction_date_time

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
        if issubclass(CompanySendsToEdge, dict):
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
        if not isinstance(other, CompanySendsToEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
