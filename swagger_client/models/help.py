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


class Help(object):
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
        'help_id': 'int',
        'topic': 'str',
        'category': 'str',
        'link': 'str'
    }

    attribute_map = {
        'help_id': 'helpId',
        'topic': 'topic',
        'category': 'category',
        'link': 'link'
    }

    def __init__(self, help_id=None, topic=None, category=None, link=None):  # noqa: E501
        """Help - a model defined in Swagger"""  # noqa: E501

        self._help_id = None
        self._topic = None
        self._category = None
        self._link = None
        self.discriminator = None

        if help_id is not None:
            self.help_id = help_id
        if topic is not None:
            self.topic = topic
        if category is not None:
            self.category = category
        if link is not None:
            self.link = link

    @property
    def help_id(self):
        """Gets the help_id of this Help.  # noqa: E501

        The ID of this Help Record  # noqa: E501

        :return: The help_id of this Help.  # noqa: E501
        :rtype: int
        """
        return self._help_id

    @help_id.setter
    def help_id(self, help_id):
        """Sets the help_id of this Help.

        The ID of this Help Record  # noqa: E501

        :param help_id: The help_id of this Help.  # noqa: E501
        :type: int
        """

        self._help_id = help_id

    @property
    def topic(self):
        """Gets the topic of this Help.  # noqa: E501

        The topic for this Help Record  # noqa: E501

        :return: The topic of this Help.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this Help.

        The topic for this Help Record  # noqa: E501

        :param topic: The topic of this Help.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def category(self):
        """Gets the category of this Help.  # noqa: E501

        The Category for this Help Record  # noqa: E501

        :return: The category of this Help.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Help.

        The Category for this Help Record  # noqa: E501

        :param category: The category of this Help.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def link(self):
        """Gets the link of this Help.  # noqa: E501

        The Link to the Manual for this Help Record  # noqa: E501

        :return: The link of this Help.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Help.

        The Link to the Manual for this Help Record  # noqa: E501

        :param link: The link of this Help.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if not isinstance(other, Help):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
