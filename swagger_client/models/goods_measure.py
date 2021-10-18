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

class GoodsMeasure(object):
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
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, value=None, unit=None):  # noqa: E501
        """GoodsMeasure - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._unit = None
        self.discriminator = None
        self.value = value
        self.unit = unit

    @property
    def value(self):
        """Gets the value of this GoodsMeasure.  # noqa: E501

        Value of the good measurement  # noqa: E501

        :return: The value of this GoodsMeasure.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GoodsMeasure.

        Value of the good measurement  # noqa: E501

        :param value: The value of this GoodsMeasure.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this GoodsMeasure.  # noqa: E501

        Unit of the good measurement (in ANSI standard)  # noqa: E501

        :return: The unit of this GoodsMeasure.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GoodsMeasure.

        Unit of the good measurement (in ANSI standard)  # noqa: E501

        :param unit: The unit of this GoodsMeasure.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if issubclass(GoodsMeasure, dict):
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
        if not isinstance(other, GoodsMeasure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other