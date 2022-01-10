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
from swagger_client.models.base_node import BaseNode  # noqa: F401,E501

class AddressNode(BaseNode):
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
        'address_canon_id': 'str',
        'address_node_name': 'str',
        'bbox_geojson': 'BBoxGeoJson',
        'centroid_geojson': 'CentroidGeoJson'
    }
    if hasattr(BaseNode, "swagger_types"):
        swagger_types.update(BaseNode.swagger_types)

    attribute_map = {
        'address_canon_id': 'address_canon_id',
        'address_node_name': 'address_node_name',
        'bbox_geojson': 'bbox_geojson',
        'centroid_geojson': 'centroid_geojson'
    }
    if hasattr(BaseNode, "attribute_map"):
        attribute_map.update(BaseNode.attribute_map)

    def __init__(self, address_canon_id=None, address_node_name=None, bbox_geojson=None, centroid_geojson=None, *args, **kwargs):  # noqa: E501
        """AddressNode - a model defined in Swagger"""  # noqa: E501
        self._address_canon_id = None
        self._address_node_name = None
        self._bbox_geojson = None
        self._centroid_geojson = None
        self.discriminator = None
        if address_canon_id is not None:
            self.address_canon_id = address_canon_id
        if address_node_name is not None:
            self.address_node_name = address_node_name
        if bbox_geojson is not None:
            self.bbox_geojson = bbox_geojson
        if centroid_geojson is not None:
            self.centroid_geojson = centroid_geojson
        BaseNode.__init__(self, *args, **kwargs)

    @property
    def address_canon_id(self):
        """Gets the address_canon_id of this AddressNode.  # noqa: E501

        A unique identifier for an address node  # noqa: E501

        :return: The address_canon_id of this AddressNode.  # noqa: E501
        :rtype: str
        """
        return self._address_canon_id

    @address_canon_id.setter
    def address_canon_id(self, address_canon_id):
        """Sets the address_canon_id of this AddressNode.

        A unique identifier for an address node  # noqa: E501

        :param address_canon_id: The address_canon_id of this AddressNode.  # noqa: E501
        :type: str
        """

        self._address_canon_id = address_canon_id

    @property
    def address_node_name(self):
        """Gets the address_node_name of this AddressNode.  # noqa: E501

        The canonical address represented by the node  # noqa: E501

        :return: The address_node_name of this AddressNode.  # noqa: E501
        :rtype: str
        """
        return self._address_node_name

    @address_node_name.setter
    def address_node_name(self, address_node_name):
        """Sets the address_node_name of this AddressNode.

        The canonical address represented by the node  # noqa: E501

        :param address_node_name: The address_node_name of this AddressNode.  # noqa: E501
        :type: str
        """

        self._address_node_name = address_node_name

    @property
    def bbox_geojson(self):
        """Gets the bbox_geojson of this AddressNode.  # noqa: E501


        :return: The bbox_geojson of this AddressNode.  # noqa: E501
        :rtype: BBoxGeoJson
        """
        return self._bbox_geojson

    @bbox_geojson.setter
    def bbox_geojson(self, bbox_geojson):
        """Sets the bbox_geojson of this AddressNode.


        :param bbox_geojson: The bbox_geojson of this AddressNode.  # noqa: E501
        :type: BBoxGeoJson
        """

        self._bbox_geojson = bbox_geojson

    @property
    def centroid_geojson(self):
        """Gets the centroid_geojson of this AddressNode.  # noqa: E501


        :return: The centroid_geojson of this AddressNode.  # noqa: E501
        :rtype: CentroidGeoJson
        """
        return self._centroid_geojson

    @centroid_geojson.setter
    def centroid_geojson(self, centroid_geojson):
        """Sets the centroid_geojson of this AddressNode.


        :param centroid_geojson: The centroid_geojson of this AddressNode.  # noqa: E501
        :type: CentroidGeoJson
        """

        self._centroid_geojson = centroid_geojson

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
        if issubclass(AddressNode, dict):
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
        if not isinstance(other, AddressNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
