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

class TypesEdgesEdgeName(object):
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
        'destination': 'str',
        'source': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'source': 'source'
    }

    def __init__(self, destination=None, source=None):  # noqa: E501
        """TypesEdgesEdgeName - a model defined in Swagger"""  # noqa: E501
        self._destination = None
        self._source = None
        self.discriminator = None
        if destination is not None:
            self.destination = destination
        if source is not None:
            self.source = source

    @property
    def destination(self):
        """Gets the destination of this TypesEdgesEdgeName.  # noqa: E501


        :return: The destination of this TypesEdgesEdgeName.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this TypesEdgesEdgeName.


        :param destination: The destination of this TypesEdgesEdgeName.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def source(self):
        """Gets the source of this TypesEdgesEdgeName.  # noqa: E501


        :return: The source of this TypesEdgesEdgeName.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TypesEdgesEdgeName.


        :param source: The source of this TypesEdgesEdgeName.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(TypesEdgesEdgeName, dict):
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
        if not isinstance(other, TypesEdgesEdgeName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
