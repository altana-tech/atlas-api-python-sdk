# coding: utf-8

"""
    Altana Atlas API

    Altana Atlas for Regulatory Risk and Trade Compliance  # noqa: E501

    OpenAPI spec version: {{ version or \"v0.0.1\" }}
    Contact: engineering@altanatech.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Product(object):
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
        'product_canon_id': 'str',
        'name': 'str',
        'hs_codes': 'list[str]',
        'number_records': 'int'
    }

    attribute_map = {
        'product_canon_id': 'product_canon_id',
        'name': 'name',
        'hs_codes': 'hs_codes',
        'number_records': 'number_records'
    }

    def __init__(self, product_canon_id=None, name=None, hs_codes=None, number_records=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501
        self._product_canon_id = None
        self._name = None
        self._hs_codes = None
        self._number_records = None
        self.discriminator = None
        if product_canon_id is not None:
            self.product_canon_id = product_canon_id
        if name is not None:
            self.name = name
        if hs_codes is not None:
            self.hs_codes = hs_codes
        if number_records is not None:
            self.number_records = number_records

    @property
    def product_canon_id(self):
        """Gets the product_canon_id of this Product.  # noqa: E501

        Altana generated, entity resolved UUID representing a product  # noqa: E501

        :return: The product_canon_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_canon_id

    @product_canon_id.setter
    def product_canon_id(self, product_canon_id):
        """Sets the product_canon_id of this Product.

        Altana generated, entity resolved UUID representing a product  # noqa: E501

        :param product_canon_id: The product_canon_id of this Product.  # noqa: E501
        :type: str
        """

        self._product_canon_id = product_canon_id

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501

        The name of the product  # noqa: E501

        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        The name of the product  # noqa: E501

        :param name: The name of this Product.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hs_codes(self):
        """Gets the hs_codes of this Product.  # noqa: E501

        The HS codes associated with the product  # noqa: E501

        :return: The hs_codes of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._hs_codes

    @hs_codes.setter
    def hs_codes(self, hs_codes):
        """Sets the hs_codes of this Product.

        The HS codes associated with the product  # noqa: E501

        :param hs_codes: The hs_codes of this Product.  # noqa: E501
        :type: list[str]
        """

        self._hs_codes = hs_codes

    @property
    def number_records(self):
        """Gets the number_records of this Product.  # noqa: E501

        Number of transaction records associated with the product  # noqa: E501

        :return: The number_records of this Product.  # noqa: E501
        :rtype: int
        """
        return self._number_records

    @number_records.setter
    def number_records(self, number_records):
        """Sets the number_records of this Product.

        Number of transaction records associated with the product  # noqa: E501

        :param number_records: The number_records of this Product.  # noqa: E501
        :type: int
        """

        self._number_records = number_records

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
        if issubclass(Product, dict):
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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
