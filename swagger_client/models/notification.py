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

from swagger_client.models.display_group import DisplayGroup  # noqa: F401,E501
from swagger_client.models.user_group import UserGroup  # noqa: F401,E501


class Notification(object):
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
        'notification_id': 'int',
        'created_dt': 'int',
        'release_dt': 'int',
        'subject': 'str',
        'body': 'str',
        'is_email': 'int',
        'is_interrupt': 'int',
        'is_system': 'int',
        'user_id': 'int',
        'user_groups': 'list[UserGroup]',
        'display_groups': 'list[DisplayGroup]'
    }

    attribute_map = {
        'notification_id': 'notificationId',
        'created_dt': 'createdDt',
        'release_dt': 'releaseDt',
        'subject': 'subject',
        'body': 'body',
        'is_email': 'isEmail',
        'is_interrupt': 'isInterrupt',
        'is_system': 'isSystem',
        'user_id': 'userId',
        'user_groups': 'userGroups',
        'display_groups': 'displayGroups'
    }

    def __init__(self, notification_id=None, created_dt=None, release_dt=None, subject=None, body=None, is_email=None, is_interrupt=None, is_system=None, user_id=None, user_groups=None, display_groups=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._notification_id = None
        self._created_dt = None
        self._release_dt = None
        self._subject = None
        self._body = None
        self._is_email = None
        self._is_interrupt = None
        self._is_system = None
        self._user_id = None
        self._user_groups = None
        self._display_groups = None
        self.discriminator = None

        if notification_id is not None:
            self.notification_id = notification_id
        if created_dt is not None:
            self.created_dt = created_dt
        if release_dt is not None:
            self.release_dt = release_dt
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        if is_email is not None:
            self.is_email = is_email
        if is_interrupt is not None:
            self.is_interrupt = is_interrupt
        if is_system is not None:
            self.is_system = is_system
        if user_id is not None:
            self.user_id = user_id
        if user_groups is not None:
            self.user_groups = user_groups
        if display_groups is not None:
            self.display_groups = display_groups

    @property
    def notification_id(self):
        """Gets the notification_id of this Notification.  # noqa: E501

        The Notifcation ID  # noqa: E501

        :return: The notification_id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this Notification.

        The Notifcation ID  # noqa: E501

        :param notification_id: The notification_id of this Notification.  # noqa: E501
        :type: int
        """

        self._notification_id = notification_id

    @property
    def created_dt(self):
        """Gets the created_dt of this Notification.  # noqa: E501

        Create Date as Unix Timestamp  # noqa: E501

        :return: The created_dt of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Notification.

        Create Date as Unix Timestamp  # noqa: E501

        :param created_dt: The created_dt of this Notification.  # noqa: E501
        :type: int
        """

        self._created_dt = created_dt

    @property
    def release_dt(self):
        """Gets the release_dt of this Notification.  # noqa: E501

        Release Date as Unix Timestamp  # noqa: E501

        :return: The release_dt of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._release_dt

    @release_dt.setter
    def release_dt(self, release_dt):
        """Sets the release_dt of this Notification.

        Release Date as Unix Timestamp  # noqa: E501

        :param release_dt: The release_dt of this Notification.  # noqa: E501
        :type: int
        """

        self._release_dt = release_dt

    @property
    def subject(self):
        """Gets the subject of this Notification.  # noqa: E501

        The subject line  # noqa: E501

        :return: The subject of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Notification.

        The subject line  # noqa: E501

        :param subject: The subject of this Notification.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this Notification.  # noqa: E501

        The HTML body of the notification  # noqa: E501

        :return: The body of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Notification.

        The HTML body of the notification  # noqa: E501

        :param body: The body of this Notification.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def is_email(self):
        """Gets the is_email of this Notification.  # noqa: E501

        Should the notification be emailed  # noqa: E501

        :return: The is_email of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._is_email

    @is_email.setter
    def is_email(self, is_email):
        """Sets the is_email of this Notification.

        Should the notification be emailed  # noqa: E501

        :param is_email: The is_email of this Notification.  # noqa: E501
        :type: int
        """

        self._is_email = is_email

    @property
    def is_interrupt(self):
        """Gets the is_interrupt of this Notification.  # noqa: E501

        Should the notification interrupt the CMS UI on navigate/login  # noqa: E501

        :return: The is_interrupt of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._is_interrupt

    @is_interrupt.setter
    def is_interrupt(self, is_interrupt):
        """Sets the is_interrupt of this Notification.

        Should the notification interrupt the CMS UI on navigate/login  # noqa: E501

        :param is_interrupt: The is_interrupt of this Notification.  # noqa: E501
        :type: int
        """

        self._is_interrupt = is_interrupt

    @property
    def is_system(self):
        """Gets the is_system of this Notification.  # noqa: E501

        Flag for system notification  # noqa: E501

        :return: The is_system of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """Sets the is_system of this Notification.

        Flag for system notification  # noqa: E501

        :param is_system: The is_system of this Notification.  # noqa: E501
        :type: int
        """

        self._is_system = is_system

    @property
    def user_id(self):
        """Gets the user_id of this Notification.  # noqa: E501

        The Owner User Id  # noqa: E501

        :return: The user_id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Notification.

        The Owner User Id  # noqa: E501

        :param user_id: The user_id of this Notification.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_groups(self):
        """Gets the user_groups of this Notification.  # noqa: E501

        User Group Notifications associated with this notification  # noqa: E501

        :return: The user_groups of this Notification.  # noqa: E501
        :rtype: list[UserGroup]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this Notification.

        User Group Notifications associated with this notification  # noqa: E501

        :param user_groups: The user_groups of this Notification.  # noqa: E501
        :type: list[UserGroup]
        """

        self._user_groups = user_groups

    @property
    def display_groups(self):
        """Gets the display_groups of this Notification.  # noqa: E501

        Display Groups associated with this notification  # noqa: E501

        :return: The display_groups of this Notification.  # noqa: E501
        :rtype: list[DisplayGroup]
        """
        return self._display_groups

    @display_groups.setter
    def display_groups(self, display_groups):
        """Sets the display_groups of this Notification.

        Display Groups associated with this notification  # noqa: E501

        :param display_groups: The display_groups of this Notification.  # noqa: E501
        :type: list[DisplayGroup]
        """

        self._display_groups = display_groups

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
