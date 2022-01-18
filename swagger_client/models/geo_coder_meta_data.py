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

class GeoCoderMetaData(object):
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
        'geocoder_metadata_bool': 'bool',
        'geo_confidence_in': 'float',
        'geo_confidence_out': 'float',
        'latitude_in': 'float',
        'latitude_out': 'float',
        'longitude_in': 'float',
        'longitude_out': 'float',
        'bbox_geojson_in': 'object',
        'bbox_geojson_out': 'object',
        'geo_level_in': 'str',
        'geo_level_out': 'str',
        'bbox_size_km2_in': 'float',
        'bbox_size_km2_out': 'float',
        'layer_properties_in': 'object',
        'layer_properties_out': 'object'
    }

    attribute_map = {
        'geocoder_metadata_bool': 'geocoder_metadata_bool',
        'geo_confidence_in': 'geo_confidence_in',
        'geo_confidence_out': 'geo_confidence_out',
        'latitude_in': 'latitude_in',
        'latitude_out': 'latitude_out',
        'longitude_in': 'longitude_in',
        'longitude_out': 'longitude_out',
        'bbox_geojson_in': 'bbox_geojson_in',
        'bbox_geojson_out': 'bbox_geojson_out',
        'geo_level_in': 'geo_level_in',
        'geo_level_out': 'geo_level_out',
        'bbox_size_km2_in': 'bbox_size_km2_in',
        'bbox_size_km2_out': 'bbox_size_km2_out',
        'layer_properties_in': 'layer_properties_in',
        'layer_properties_out': 'layer_properties_out'
    }

    def __init__(self, geocoder_metadata_bool=None, geo_confidence_in=None, geo_confidence_out=None, latitude_in=None, latitude_out=None, longitude_in=None, longitude_out=None, bbox_geojson_in=None, bbox_geojson_out=None, geo_level_in=None, geo_level_out=None, bbox_size_km2_in=None, bbox_size_km2_out=None, layer_properties_in=None, layer_properties_out=None):  # noqa: E501
        """GeoCoderMetaData - a model defined in Swagger"""  # noqa: E501
        self._geocoder_metadata_bool = None
        self._geo_confidence_in = None
        self._geo_confidence_out = None
        self._latitude_in = None
        self._latitude_out = None
        self._longitude_in = None
        self._longitude_out = None
        self._bbox_geojson_in = None
        self._bbox_geojson_out = None
        self._geo_level_in = None
        self._geo_level_out = None
        self._bbox_size_km2_in = None
        self._bbox_size_km2_out = None
        self._layer_properties_in = None
        self._layer_properties_out = None
        self.discriminator = None
        if geocoder_metadata_bool is not None:
            self.geocoder_metadata_bool = geocoder_metadata_bool
        if geo_confidence_in is not None:
            self.geo_confidence_in = geo_confidence_in
        if geo_confidence_out is not None:
            self.geo_confidence_out = geo_confidence_out
        if latitude_in is not None:
            self.latitude_in = latitude_in
        if latitude_out is not None:
            self.latitude_out = latitude_out
        if longitude_in is not None:
            self.longitude_in = longitude_in
        if longitude_out is not None:
            self.longitude_out = longitude_out
        if bbox_geojson_in is not None:
            self.bbox_geojson_in = bbox_geojson_in
        if bbox_geojson_out is not None:
            self.bbox_geojson_out = bbox_geojson_out
        if geo_level_in is not None:
            self.geo_level_in = geo_level_in
        if geo_level_out is not None:
            self.geo_level_out = geo_level_out
        if bbox_size_km2_in is not None:
            self.bbox_size_km2_in = bbox_size_km2_in
        if bbox_size_km2_out is not None:
            self.bbox_size_km2_out = bbox_size_km2_out
        if layer_properties_in is not None:
            self.layer_properties_in = layer_properties_in
        if layer_properties_out is not None:
            self.layer_properties_out = layer_properties_out

    @property
    def geocoder_metadata_bool(self):
        """Gets the geocoder_metadata_bool of this GeoCoderMetaData.  # noqa: E501


        :return: The geocoder_metadata_bool of this GeoCoderMetaData.  # noqa: E501
        :rtype: bool
        """
        return self._geocoder_metadata_bool

    @geocoder_metadata_bool.setter
    def geocoder_metadata_bool(self, geocoder_metadata_bool):
        """Sets the geocoder_metadata_bool of this GeoCoderMetaData.


        :param geocoder_metadata_bool: The geocoder_metadata_bool of this GeoCoderMetaData.  # noqa: E501
        :type: bool
        """

        self._geocoder_metadata_bool = geocoder_metadata_bool

    @property
    def geo_confidence_in(self):
        """Gets the geo_confidence_in of this GeoCoderMetaData.  # noqa: E501


        :return: The geo_confidence_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._geo_confidence_in

    @geo_confidence_in.setter
    def geo_confidence_in(self, geo_confidence_in):
        """Sets the geo_confidence_in of this GeoCoderMetaData.


        :param geo_confidence_in: The geo_confidence_in of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._geo_confidence_in = geo_confidence_in

    @property
    def geo_confidence_out(self):
        """Gets the geo_confidence_out of this GeoCoderMetaData.  # noqa: E501


        :return: The geo_confidence_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._geo_confidence_out

    @geo_confidence_out.setter
    def geo_confidence_out(self, geo_confidence_out):
        """Sets the geo_confidence_out of this GeoCoderMetaData.


        :param geo_confidence_out: The geo_confidence_out of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._geo_confidence_out = geo_confidence_out

    @property
    def latitude_in(self):
        """Gets the latitude_in of this GeoCoderMetaData.  # noqa: E501


        :return: The latitude_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._latitude_in

    @latitude_in.setter
    def latitude_in(self, latitude_in):
        """Sets the latitude_in of this GeoCoderMetaData.


        :param latitude_in: The latitude_in of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._latitude_in = latitude_in

    @property
    def latitude_out(self):
        """Gets the latitude_out of this GeoCoderMetaData.  # noqa: E501


        :return: The latitude_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._latitude_out

    @latitude_out.setter
    def latitude_out(self, latitude_out):
        """Sets the latitude_out of this GeoCoderMetaData.


        :param latitude_out: The latitude_out of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._latitude_out = latitude_out

    @property
    def longitude_in(self):
        """Gets the longitude_in of this GeoCoderMetaData.  # noqa: E501


        :return: The longitude_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._longitude_in

    @longitude_in.setter
    def longitude_in(self, longitude_in):
        """Sets the longitude_in of this GeoCoderMetaData.


        :param longitude_in: The longitude_in of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._longitude_in = longitude_in

    @property
    def longitude_out(self):
        """Gets the longitude_out of this GeoCoderMetaData.  # noqa: E501


        :return: The longitude_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._longitude_out

    @longitude_out.setter
    def longitude_out(self, longitude_out):
        """Sets the longitude_out of this GeoCoderMetaData.


        :param longitude_out: The longitude_out of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._longitude_out = longitude_out

    @property
    def bbox_geojson_in(self):
        """Gets the bbox_geojson_in of this GeoCoderMetaData.  # noqa: E501


        :return: The bbox_geojson_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: object
        """
        return self._bbox_geojson_in

    @bbox_geojson_in.setter
    def bbox_geojson_in(self, bbox_geojson_in):
        """Sets the bbox_geojson_in of this GeoCoderMetaData.


        :param bbox_geojson_in: The bbox_geojson_in of this GeoCoderMetaData.  # noqa: E501
        :type: object
        """

        self._bbox_geojson_in = bbox_geojson_in

    @property
    def bbox_geojson_out(self):
        """Gets the bbox_geojson_out of this GeoCoderMetaData.  # noqa: E501


        :return: The bbox_geojson_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: object
        """
        return self._bbox_geojson_out

    @bbox_geojson_out.setter
    def bbox_geojson_out(self, bbox_geojson_out):
        """Sets the bbox_geojson_out of this GeoCoderMetaData.


        :param bbox_geojson_out: The bbox_geojson_out of this GeoCoderMetaData.  # noqa: E501
        :type: object
        """

        self._bbox_geojson_out = bbox_geojson_out

    @property
    def geo_level_in(self):
        """Gets the geo_level_in of this GeoCoderMetaData.  # noqa: E501


        :return: The geo_level_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: str
        """
        return self._geo_level_in

    @geo_level_in.setter
    def geo_level_in(self, geo_level_in):
        """Sets the geo_level_in of this GeoCoderMetaData.


        :param geo_level_in: The geo_level_in of this GeoCoderMetaData.  # noqa: E501
        :type: str
        """

        self._geo_level_in = geo_level_in

    @property
    def geo_level_out(self):
        """Gets the geo_level_out of this GeoCoderMetaData.  # noqa: E501


        :return: The geo_level_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: str
        """
        return self._geo_level_out

    @geo_level_out.setter
    def geo_level_out(self, geo_level_out):
        """Sets the geo_level_out of this GeoCoderMetaData.


        :param geo_level_out: The geo_level_out of this GeoCoderMetaData.  # noqa: E501
        :type: str
        """

        self._geo_level_out = geo_level_out

    @property
    def bbox_size_km2_in(self):
        """Gets the bbox_size_km2_in of this GeoCoderMetaData.  # noqa: E501


        :return: The bbox_size_km2_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._bbox_size_km2_in

    @bbox_size_km2_in.setter
    def bbox_size_km2_in(self, bbox_size_km2_in):
        """Sets the bbox_size_km2_in of this GeoCoderMetaData.


        :param bbox_size_km2_in: The bbox_size_km2_in of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._bbox_size_km2_in = bbox_size_km2_in

    @property
    def bbox_size_km2_out(self):
        """Gets the bbox_size_km2_out of this GeoCoderMetaData.  # noqa: E501


        :return: The bbox_size_km2_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: float
        """
        return self._bbox_size_km2_out

    @bbox_size_km2_out.setter
    def bbox_size_km2_out(self, bbox_size_km2_out):
        """Sets the bbox_size_km2_out of this GeoCoderMetaData.


        :param bbox_size_km2_out: The bbox_size_km2_out of this GeoCoderMetaData.  # noqa: E501
        :type: float
        """

        self._bbox_size_km2_out = bbox_size_km2_out

    @property
    def layer_properties_in(self):
        """Gets the layer_properties_in of this GeoCoderMetaData.  # noqa: E501


        :return: The layer_properties_in of this GeoCoderMetaData.  # noqa: E501
        :rtype: object
        """
        return self._layer_properties_in

    @layer_properties_in.setter
    def layer_properties_in(self, layer_properties_in):
        """Sets the layer_properties_in of this GeoCoderMetaData.


        :param layer_properties_in: The layer_properties_in of this GeoCoderMetaData.  # noqa: E501
        :type: object
        """

        self._layer_properties_in = layer_properties_in

    @property
    def layer_properties_out(self):
        """Gets the layer_properties_out of this GeoCoderMetaData.  # noqa: E501


        :return: The layer_properties_out of this GeoCoderMetaData.  # noqa: E501
        :rtype: object
        """
        return self._layer_properties_out

    @layer_properties_out.setter
    def layer_properties_out(self, layer_properties_out):
        """Sets the layer_properties_out of this GeoCoderMetaData.


        :param layer_properties_out: The layer_properties_out of this GeoCoderMetaData.  # noqa: E501
        :type: object
        """

        self._layer_properties_out = layer_properties_out

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
        if issubclass(GeoCoderMetaData, dict):
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
        if not isinstance(other, GeoCoderMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other