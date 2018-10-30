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

from swagger_client.models.module_widget import ModuleWidget  # noqa: F401,E501
from swagger_client.models.permission import Permission  # noqa: F401,E501
from swagger_client.models.widget_audio import WidgetAudio  # noqa: F401,E501
from swagger_client.models.widget_option import WidgetOption  # noqa: F401,E501


class Widget(object):
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
        'playlist_id': 'int',
        'owner_id': 'int',
        'type': 'str',
        'duration': 'int',
        'display_order': 'int',
        'use_duration': 'int',
        'calculated_duration': 'int',
        'created_dt': 'str',
        'modified_dt': 'str',
        'widget_options': 'list[WidgetOption]',
        'media_ids': 'list[int]',
        'audio': 'list[WidgetAudio]',
        'permissions': 'list[Permission]',
        'module': 'ModuleWidget',
        'playlist': 'str'
    }

    attribute_map = {
        'widget_id': 'widgetId',
        'playlist_id': 'playlistId',
        'owner_id': 'ownerId',
        'type': 'type',
        'duration': 'duration',
        'display_order': 'displayOrder',
        'use_duration': 'useDuration',
        'calculated_duration': 'calculatedDuration',
        'created_dt': 'createdDt',
        'modified_dt': 'modifiedDt',
        'widget_options': 'widgetOptions',
        'media_ids': 'mediaIds',
        'audio': 'audio',
        'permissions': 'permissions',
        'module': 'module',
        'playlist': 'playlist'
    }

    def __init__(self, widget_id=None, playlist_id=None, owner_id=None, type=None, duration=None, display_order=None, use_duration=None, calculated_duration=None, created_dt=None, modified_dt=None, widget_options=None, media_ids=None, audio=None, permissions=None, module=None, playlist=None):  # noqa: E501
        """Widget - a model defined in Swagger"""  # noqa: E501

        self._widget_id = None
        self._playlist_id = None
        self._owner_id = None
        self._type = None
        self._duration = None
        self._display_order = None
        self._use_duration = None
        self._calculated_duration = None
        self._created_dt = None
        self._modified_dt = None
        self._widget_options = None
        self._media_ids = None
        self._audio = None
        self._permissions = None
        self._module = None
        self._playlist = None
        self.discriminator = None

        if widget_id is not None:
            self.widget_id = widget_id
        if playlist_id is not None:
            self.playlist_id = playlist_id
        if owner_id is not None:
            self.owner_id = owner_id
        if type is not None:
            self.type = type
        if duration is not None:
            self.duration = duration
        if display_order is not None:
            self.display_order = display_order
        if use_duration is not None:
            self.use_duration = use_duration
        if calculated_duration is not None:
            self.calculated_duration = calculated_duration
        if created_dt is not None:
            self.created_dt = created_dt
        if modified_dt is not None:
            self.modified_dt = modified_dt
        if widget_options is not None:
            self.widget_options = widget_options
        if media_ids is not None:
            self.media_ids = media_ids
        if audio is not None:
            self.audio = audio
        if permissions is not None:
            self.permissions = permissions
        if module is not None:
            self.module = module
        if playlist is not None:
            self.playlist = playlist

    @property
    def widget_id(self):
        """Gets the widget_id of this Widget.  # noqa: E501

        The Widget ID  # noqa: E501

        :return: The widget_id of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        """Sets the widget_id of this Widget.

        The Widget ID  # noqa: E501

        :param widget_id: The widget_id of this Widget.  # noqa: E501
        :type: int
        """

        self._widget_id = widget_id

    @property
    def playlist_id(self):
        """Gets the playlist_id of this Widget.  # noqa: E501

        The ID of the Playlist this Widget belongs to  # noqa: E501

        :return: The playlist_id of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._playlist_id

    @playlist_id.setter
    def playlist_id(self, playlist_id):
        """Sets the playlist_id of this Widget.

        The ID of the Playlist this Widget belongs to  # noqa: E501

        :param playlist_id: The playlist_id of this Widget.  # noqa: E501
        :type: int
        """

        self._playlist_id = playlist_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Widget.  # noqa: E501

        The ID of the User that owns this Widget  # noqa: E501

        :return: The owner_id of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Widget.

        The ID of the User that owns this Widget  # noqa: E501

        :param owner_id: The owner_id of this Widget.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def type(self):
        """Gets the type of this Widget.  # noqa: E501

        The Module Type Code  # noqa: E501

        :return: The type of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Widget.

        The Module Type Code  # noqa: E501

        :param type: The type of this Widget.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this Widget.  # noqa: E501

        The duration in seconds this widget should be shown  # noqa: E501

        :return: The duration of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Widget.

        The duration in seconds this widget should be shown  # noqa: E501

        :param duration: The duration of this Widget.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def display_order(self):
        """Gets the display_order of this Widget.  # noqa: E501

        The display order of this widget  # noqa: E501

        :return: The display_order of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this Widget.

        The display order of this widget  # noqa: E501

        :param display_order: The display_order of this Widget.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def use_duration(self):
        """Gets the use_duration of this Widget.  # noqa: E501

        Flag indicating if this widget has a duration that should be used  # noqa: E501

        :return: The use_duration of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._use_duration

    @use_duration.setter
    def use_duration(self, use_duration):
        """Sets the use_duration of this Widget.

        Flag indicating if this widget has a duration that should be used  # noqa: E501

        :param use_duration: The use_duration of this Widget.  # noqa: E501
        :type: int
        """

        self._use_duration = use_duration

    @property
    def calculated_duration(self):
        """Gets the calculated_duration of this Widget.  # noqa: E501

        Calculated Duration of this widget after taking into account the useDuration flag  # noqa: E501

        :return: The calculated_duration of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._calculated_duration

    @calculated_duration.setter
    def calculated_duration(self, calculated_duration):
        """Sets the calculated_duration of this Widget.

        Calculated Duration of this widget after taking into account the useDuration flag  # noqa: E501

        :param calculated_duration: The calculated_duration of this Widget.  # noqa: E501
        :type: int
        """

        self._calculated_duration = calculated_duration

    @property
    def created_dt(self):
        """Gets the created_dt of this Widget.  # noqa: E501

        The datetime the Layout was created  # noqa: E501

        :return: The created_dt of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Widget.

        The datetime the Layout was created  # noqa: E501

        :param created_dt: The created_dt of this Widget.  # noqa: E501
        :type: str
        """

        self._created_dt = created_dt

    @property
    def modified_dt(self):
        """Gets the modified_dt of this Widget.  # noqa: E501

        The datetime the Layout was last modified  # noqa: E501

        :return: The modified_dt of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._modified_dt

    @modified_dt.setter
    def modified_dt(self, modified_dt):
        """Sets the modified_dt of this Widget.

        The datetime the Layout was last modified  # noqa: E501

        :param modified_dt: The modified_dt of this Widget.  # noqa: E501
        :type: str
        """

        self._modified_dt = modified_dt

    @property
    def widget_options(self):
        """Gets the widget_options of this Widget.  # noqa: E501

        An array of Widget Options  # noqa: E501

        :return: The widget_options of this Widget.  # noqa: E501
        :rtype: list[WidgetOption]
        """
        return self._widget_options

    @widget_options.setter
    def widget_options(self, widget_options):
        """Sets the widget_options of this Widget.

        An array of Widget Options  # noqa: E501

        :param widget_options: The widget_options of this Widget.  # noqa: E501
        :type: list[WidgetOption]
        """

        self._widget_options = widget_options

    @property
    def media_ids(self):
        """Gets the media_ids of this Widget.  # noqa: E501

        An array of MediaIds this widget is linked to  # noqa: E501

        :return: The media_ids of this Widget.  # noqa: E501
        :rtype: list[int]
        """
        return self._media_ids

    @media_ids.setter
    def media_ids(self, media_ids):
        """Sets the media_ids of this Widget.

        An array of MediaIds this widget is linked to  # noqa: E501

        :param media_ids: The media_ids of this Widget.  # noqa: E501
        :type: list[int]
        """

        self._media_ids = media_ids

    @property
    def audio(self):
        """Gets the audio of this Widget.  # noqa: E501

        An array of Audio MediaIds this widget is linked to  # noqa: E501

        :return: The audio of this Widget.  # noqa: E501
        :rtype: list[WidgetAudio]
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this Widget.

        An array of Audio MediaIds this widget is linked to  # noqa: E501

        :param audio: The audio of this Widget.  # noqa: E501
        :type: list[WidgetAudio]
        """

        self._audio = audio

    @property
    def permissions(self):
        """Gets the permissions of this Widget.  # noqa: E501

        An array of permissions for this widget  # noqa: E501

        :return: The permissions of this Widget.  # noqa: E501
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Widget.

        An array of permissions for this widget  # noqa: E501

        :param permissions: The permissions of this Widget.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions

    @property
    def module(self):
        """Gets the module of this Widget.  # noqa: E501

        The Module Object for this Widget  # noqa: E501

        :return: The module of this Widget.  # noqa: E501
        :rtype: ModuleWidget
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this Widget.

        The Module Object for this Widget  # noqa: E501

        :param module: The module of this Widget.  # noqa: E501
        :type: ModuleWidget
        """

        self._module = module

    @property
    def playlist(self):
        """Gets the playlist of this Widget.  # noqa: E501

        The name of the Playlist this Widget is on  # noqa: E501

        :return: The playlist of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._playlist

    @playlist.setter
    def playlist(self, playlist):
        """Sets the playlist of this Widget.

        The name of the Playlist this Widget is on  # noqa: E501

        :param playlist: The playlist of this Widget.  # noqa: E501
        :type: str
        """

        self._playlist = playlist

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
        if not isinstance(other, Widget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
