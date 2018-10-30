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

from swagger_client.models.schedule import Schedule  # noqa: F401,E501


class ScheduleCalendarData(object):
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
        'id': 'int',
        'title': 'str',
        'same_day': 'int',
        'event': 'Schedule'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'same_day': 'sameDay',
        'event': 'event'
    }

    def __init__(self, id=None, title=None, same_day=None, event=None):  # noqa: E501
        """ScheduleCalendarData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._same_day = None
        self._event = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if same_day is not None:
            self.same_day = same_day
        if event is not None:
            self.event = event

    @property
    def id(self):
        """Gets the id of this ScheduleCalendarData.  # noqa: E501

        Event ID  # noqa: E501

        :return: The id of this ScheduleCalendarData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduleCalendarData.

        Event ID  # noqa: E501

        :param id: The id of this ScheduleCalendarData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this ScheduleCalendarData.  # noqa: E501

        Event Title  # noqa: E501

        :return: The title of this ScheduleCalendarData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ScheduleCalendarData.

        Event Title  # noqa: E501

        :param title: The title of this ScheduleCalendarData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def same_day(self):
        """Gets the same_day of this ScheduleCalendarData.  # noqa: E501

        Does this event happen only on 1 day  # noqa: E501

        :return: The same_day of this ScheduleCalendarData.  # noqa: E501
        :rtype: int
        """
        return self._same_day

    @same_day.setter
    def same_day(self, same_day):
        """Sets the same_day of this ScheduleCalendarData.

        Does this event happen only on 1 day  # noqa: E501

        :param same_day: The same_day of this ScheduleCalendarData.  # noqa: E501
        :type: int
        """

        self._same_day = same_day

    @property
    def event(self):
        """Gets the event of this ScheduleCalendarData.  # noqa: E501


        :return: The event of this ScheduleCalendarData.  # noqa: E501
        :rtype: Schedule
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this ScheduleCalendarData.


        :param event: The event of this ScheduleCalendarData.  # noqa: E501
        :type: Schedule
        """

        self._event = event

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
        if not isinstance(other, ScheduleCalendarData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
