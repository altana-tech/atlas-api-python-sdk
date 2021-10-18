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

class BaseRisk(object):
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
        'risk_type': 'str',
        'risk_score': 'float'
    }

    attribute_map = {
        'risk_type': 'risk_type',
        'risk_score': 'risk_score'
    }

    def __init__(self, risk_type=None, risk_score=None):  # noqa: E501
        """BaseRisk - a model defined in Swagger"""  # noqa: E501
        self._risk_type = None
        self._risk_score = None
        self.discriminator = None
        if risk_type is not None:
            self.risk_type = risk_type
        if risk_score is not None:
            self.risk_score = risk_score

    @property
    def risk_type(self):
        """Gets the risk_type of this BaseRisk.  # noqa: E501


        :return: The risk_type of this BaseRisk.  # noqa: E501
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this BaseRisk.


        :param risk_type: The risk_type of this BaseRisk.  # noqa: E501
        :type: str
        """

        self._risk_type = risk_type

    @property
    def risk_score(self):
        """Gets the risk_score of this BaseRisk.  # noqa: E501


        :return: The risk_score of this BaseRisk.  # noqa: E501
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this BaseRisk.


        :param risk_score: The risk_score of this BaseRisk.  # noqa: E501
        :type: float
        """

        self._risk_score = risk_score

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
        if issubclass(BaseRisk, dict):
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
        if not isinstance(other, BaseRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
