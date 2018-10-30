# coding: utf-8

"""
    Xibo API

    Xibo CMS API  # noqa: E501

    OpenAPI spec version: 1.8.0
    Contact: info@xibo.org.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WidgetAudio(object):
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
        'widget_id': 'int',
        'media_id': 'int',
        'volume': 'int',
        'loop': 'int'
    }

    attribute_map = {
        'widget_id': 'widgetId',
        'media_id': 'mediaId',
        'volume': 'volume',
        'loop': 'loop'
    }

    def __init__(self, widget_id=None, media_id=None, volume=None, loop=None):  # noqa: E501
        """WidgetAudio - a model defined in Swagger"""  # noqa: E501

        self._widget_id = None
        self._media_id = None
        self._volume = None
        self._loop = None
        self.discriminator = None

        if widget_id is not None:
            self.widget_id = widget_id
        if media_id is not None:
            self.media_id = media_id
        if volume is not None:
            self.volume = volume
        if loop is not None:
            self.loop = loop

    @property
    def widget_id(self):
        """Gets the widget_id of this WidgetAudio.  # noqa: E501

        The Widget Id  # noqa: E501

        :return: The widget_id of this WidgetAudio.  # noqa: E501
        :rtype: int
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        """Sets the widget_id of this WidgetAudio.

        The Widget Id  # noqa: E501

        :param widget_id: The widget_id of this WidgetAudio.  # noqa: E501
        :type: int
        """

        self._widget_id = widget_id

    @property
    def media_id(self):
        """Gets the media_id of this WidgetAudio.  # noqa: E501

        The Media Id  # noqa: E501

        :return: The media_id of this WidgetAudio.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this WidgetAudio.

        The Media Id  # noqa: E501

        :param media_id: The media_id of this WidgetAudio.  # noqa: E501
        :type: int
        """

        self._media_id = media_id

    @property
    def volume(self):
        """Gets the volume of this WidgetAudio.  # noqa: E501

        The percentage volume  # noqa: E501

        :return: The volume of this WidgetAudio.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this WidgetAudio.

        The percentage volume  # noqa: E501

        :param volume: The volume of this WidgetAudio.  # noqa: E501
        :type: int
        """

        self._volume = volume

    @property
    def loop(self):
        """Gets the loop of this WidgetAudio.  # noqa: E501

        Flag indicating whether to loop  # noqa: E501

        :return: The loop of this WidgetAudio.  # noqa: E501
        :rtype: int
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this WidgetAudio.

        Flag indicating whether to loop  # noqa: E501

        :param loop: The loop of this WidgetAudio.  # noqa: E501
        :type: int
        """

        self._loop = loop

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WidgetAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
