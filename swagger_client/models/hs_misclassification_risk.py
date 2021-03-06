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

class HSMisclassificationRisk(object):
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
        'risk_score': 'float',
        'predicted': 'list[PredictedGoods]',
        'is_declared_hs2_equal_top_1': 'bool',
        'is_declared_hs4_equal_top_1': 'bool',
        'is_declared_hs6_equal_top_1': 'bool',
        'is_declared_hs_equal_top_1': 'bool',
        'is_declared_hs_in_top_3': 'bool',
        'is_declared_hs_in_top_5': 'bool',
        'is_tariff_diff_btw_declared_and_top_1': 'bool',
        'top_predicted_confidence': 'float',
        'mean_predicted_confidence': 'float'
    }

    attribute_map = {
        'risk_type': 'risk_type',
        'risk_score': 'risk_score',
        'predicted': 'predicted',
        'is_declared_hs2_equal_top_1': 'is_declared_hs2_equal_top_1',
        'is_declared_hs4_equal_top_1': 'is_declared_hs4_equal_top_1',
        'is_declared_hs6_equal_top_1': 'is_declared_hs6_equal_top_1',
        'is_declared_hs_equal_top_1': 'is_declared_hs_equal_top_1',
        'is_declared_hs_in_top_3': 'is_declared_hs_in_top_3',
        'is_declared_hs_in_top_5': 'is_declared_hs_in_top_5',
        'is_tariff_diff_btw_declared_and_top_1': 'is_tariff_diff_btw_declared_and_top_1',
        'top_predicted_confidence': 'top_predicted_confidence',
        'mean_predicted_confidence': 'mean_predicted_confidence'
    }

    def __init__(self, risk_type=None, risk_score=None, predicted=None, is_declared_hs2_equal_top_1=None, is_declared_hs4_equal_top_1=None, is_declared_hs6_equal_top_1=None, is_declared_hs_equal_top_1=None, is_declared_hs_in_top_3=None, is_declared_hs_in_top_5=None, is_tariff_diff_btw_declared_and_top_1=None, top_predicted_confidence=None, mean_predicted_confidence=None):  # noqa: E501
        """HSMisclassificationRisk - a model defined in Swagger"""  # noqa: E501
        self._risk_type = None
        self._risk_score = None
        self._predicted = None
        self._is_declared_hs2_equal_top_1 = None
        self._is_declared_hs4_equal_top_1 = None
        self._is_declared_hs6_equal_top_1 = None
        self._is_declared_hs_equal_top_1 = None
        self._is_declared_hs_in_top_3 = None
        self._is_declared_hs_in_top_5 = None
        self._is_tariff_diff_btw_declared_and_top_1 = None
        self._top_predicted_confidence = None
        self._mean_predicted_confidence = None
        self.discriminator = None
        if risk_type is not None:
            self.risk_type = risk_type
        if risk_score is not None:
            self.risk_score = risk_score
        if predicted is not None:
            self.predicted = predicted
        if is_declared_hs2_equal_top_1 is not None:
            self.is_declared_hs2_equal_top_1 = is_declared_hs2_equal_top_1
        if is_declared_hs4_equal_top_1 is not None:
            self.is_declared_hs4_equal_top_1 = is_declared_hs4_equal_top_1
        if is_declared_hs6_equal_top_1 is not None:
            self.is_declared_hs6_equal_top_1 = is_declared_hs6_equal_top_1
        if is_declared_hs_equal_top_1 is not None:
            self.is_declared_hs_equal_top_1 = is_declared_hs_equal_top_1
        if is_declared_hs_in_top_3 is not None:
            self.is_declared_hs_in_top_3 = is_declared_hs_in_top_3
        if is_declared_hs_in_top_5 is not None:
            self.is_declared_hs_in_top_5 = is_declared_hs_in_top_5
        if is_tariff_diff_btw_declared_and_top_1 is not None:
            self.is_tariff_diff_btw_declared_and_top_1 = is_tariff_diff_btw_declared_and_top_1
        if top_predicted_confidence is not None:
            self.top_predicted_confidence = top_predicted_confidence
        if mean_predicted_confidence is not None:
            self.mean_predicted_confidence = mean_predicted_confidence

    @property
    def risk_type(self):
        """Gets the risk_type of this HSMisclassificationRisk.  # noqa: E501


        :return: The risk_type of this HSMisclassificationRisk.  # noqa: E501
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this HSMisclassificationRisk.


        :param risk_type: The risk_type of this HSMisclassificationRisk.  # noqa: E501
        :type: str
        """

        self._risk_type = risk_type

    @property
    def risk_score(self):
        """Gets the risk_score of this HSMisclassificationRisk.  # noqa: E501


        :return: The risk_score of this HSMisclassificationRisk.  # noqa: E501
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this HSMisclassificationRisk.


        :param risk_score: The risk_score of this HSMisclassificationRisk.  # noqa: E501
        :type: float
        """

        self._risk_score = risk_score

    @property
    def predicted(self):
        """Gets the predicted of this HSMisclassificationRisk.  # noqa: E501


        :return: The predicted of this HSMisclassificationRisk.  # noqa: E501
        :rtype: list[PredictedGoods]
        """
        return self._predicted

    @predicted.setter
    def predicted(self, predicted):
        """Sets the predicted of this HSMisclassificationRisk.


        :param predicted: The predicted of this HSMisclassificationRisk.  # noqa: E501
        :type: list[PredictedGoods]
        """

        self._predicted = predicted

    @property
    def is_declared_hs2_equal_top_1(self):
        """Gets the is_declared_hs2_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first two digits (i.e., HS2)  # noqa: E501

        :return: The is_declared_hs2_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs2_equal_top_1

    @is_declared_hs2_equal_top_1.setter
    def is_declared_hs2_equal_top_1(self, is_declared_hs2_equal_top_1):
        """Sets the is_declared_hs2_equal_top_1 of this HSMisclassificationRisk.

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first two digits (i.e., HS2)  # noqa: E501

        :param is_declared_hs2_equal_top_1: The is_declared_hs2_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs2_equal_top_1 = is_declared_hs2_equal_top_1

    @property
    def is_declared_hs4_equal_top_1(self):
        """Gets the is_declared_hs4_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first four digits (i.e., HS4)  # noqa: E501

        :return: The is_declared_hs4_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs4_equal_top_1

    @is_declared_hs4_equal_top_1.setter
    def is_declared_hs4_equal_top_1(self, is_declared_hs4_equal_top_1):
        """Sets the is_declared_hs4_equal_top_1 of this HSMisclassificationRisk.

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first four digits (i.e., HS4)  # noqa: E501

        :param is_declared_hs4_equal_top_1: The is_declared_hs4_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs4_equal_top_1 = is_declared_hs4_equal_top_1

    @property
    def is_declared_hs6_equal_top_1(self):
        """Gets the is_declared_hs6_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first six digits (i.e., HS6)  # noqa: E501

        :return: The is_declared_hs6_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs6_equal_top_1

    @is_declared_hs6_equal_top_1.setter
    def is_declared_hs6_equal_top_1(self, is_declared_hs6_equal_top_1):
        """Sets the is_declared_hs6_equal_top_1 of this HSMisclassificationRisk.

        Returns true if the declared HS code and predicted HS code with the highest confidence have the same first six digits (i.e., HS6)  # noqa: E501

        :param is_declared_hs6_equal_top_1: The is_declared_hs6_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs6_equal_top_1 = is_declared_hs6_equal_top_1

    @property
    def is_declared_hs_equal_top_1(self):
        """Gets the is_declared_hs_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code and predicted HS code with the highest confidence are the same  # noqa: E501

        :return: The is_declared_hs_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs_equal_top_1

    @is_declared_hs_equal_top_1.setter
    def is_declared_hs_equal_top_1(self, is_declared_hs_equal_top_1):
        """Sets the is_declared_hs_equal_top_1 of this HSMisclassificationRisk.

        Returns true if the declared HS code and predicted HS code with the highest confidence are the same  # noqa: E501

        :param is_declared_hs_equal_top_1: The is_declared_hs_equal_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs_equal_top_1 = is_declared_hs_equal_top_1

    @property
    def is_declared_hs_in_top_3(self):
        """Gets the is_declared_hs_in_top_3 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code is one of the top three predicted HS codes, ranked by confidence  # noqa: E501

        :return: The is_declared_hs_in_top_3 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs_in_top_3

    @is_declared_hs_in_top_3.setter
    def is_declared_hs_in_top_3(self, is_declared_hs_in_top_3):
        """Sets the is_declared_hs_in_top_3 of this HSMisclassificationRisk.

        Returns true if the declared HS code is one of the top three predicted HS codes, ranked by confidence  # noqa: E501

        :param is_declared_hs_in_top_3: The is_declared_hs_in_top_3 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs_in_top_3 = is_declared_hs_in_top_3

    @property
    def is_declared_hs_in_top_5(self):
        """Gets the is_declared_hs_in_top_5 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code is one of the top five predicted HS codes, ranked by confidence  # noqa: E501

        :return: The is_declared_hs_in_top_5 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared_hs_in_top_5

    @is_declared_hs_in_top_5.setter
    def is_declared_hs_in_top_5(self, is_declared_hs_in_top_5):
        """Sets the is_declared_hs_in_top_5 of this HSMisclassificationRisk.

        Returns true if the declared HS code is one of the top five predicted HS codes, ranked by confidence  # noqa: E501

        :param is_declared_hs_in_top_5: The is_declared_hs_in_top_5 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_declared_hs_in_top_5 = is_declared_hs_in_top_5

    @property
    def is_tariff_diff_btw_declared_and_top_1(self):
        """Gets the is_tariff_diff_btw_declared_and_top_1 of this HSMisclassificationRisk.  # noqa: E501

        Returns true if the declared HS code and top predicted HS code have different tariff rates associated with them  # noqa: E501

        :return: The is_tariff_diff_btw_declared_and_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_tariff_diff_btw_declared_and_top_1

    @is_tariff_diff_btw_declared_and_top_1.setter
    def is_tariff_diff_btw_declared_and_top_1(self, is_tariff_diff_btw_declared_and_top_1):
        """Sets the is_tariff_diff_btw_declared_and_top_1 of this HSMisclassificationRisk.

        Returns true if the declared HS code and top predicted HS code have different tariff rates associated with them  # noqa: E501

        :param is_tariff_diff_btw_declared_and_top_1: The is_tariff_diff_btw_declared_and_top_1 of this HSMisclassificationRisk.  # noqa: E501
        :type: bool
        """

        self._is_tariff_diff_btw_declared_and_top_1 = is_tariff_diff_btw_declared_and_top_1

    @property
    def top_predicted_confidence(self):
        """Gets the top_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501

        Maximum confidence of all predicted HS codes  # noqa: E501

        :return: The top_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501
        :rtype: float
        """
        return self._top_predicted_confidence

    @top_predicted_confidence.setter
    def top_predicted_confidence(self, top_predicted_confidence):
        """Sets the top_predicted_confidence of this HSMisclassificationRisk.

        Maximum confidence of all predicted HS codes  # noqa: E501

        :param top_predicted_confidence: The top_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501
        :type: float
        """

        self._top_predicted_confidence = top_predicted_confidence

    @property
    def mean_predicted_confidence(self):
        """Gets the mean_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501

        Mean confidence of all predicted HS codes  # noqa: E501

        :return: The mean_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501
        :rtype: float
        """
        return self._mean_predicted_confidence

    @mean_predicted_confidence.setter
    def mean_predicted_confidence(self, mean_predicted_confidence):
        """Sets the mean_predicted_confidence of this HSMisclassificationRisk.

        Mean confidence of all predicted HS codes  # noqa: E501

        :param mean_predicted_confidence: The mean_predicted_confidence of this HSMisclassificationRisk.  # noqa: E501
        :type: float
        """

        self._mean_predicted_confidence = mean_predicted_confidence

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
        if issubclass(HSMisclassificationRisk, dict):
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
        if not isinstance(other, HSMisclassificationRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
