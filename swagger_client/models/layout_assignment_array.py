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


class LayoutAssignmentArray(object):
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
        'layout_id': 'int',
        'display_order': 'int'
    }

    attribute_map = {
        'layout_id': 'layoutId',
        'display_order': 'displayOrder'
    }

    def __init__(self, layout_id=None, display_order=None):  # noqa: E501
        """LayoutAssignmentArray - a model defined in Swagger"""  # noqa: E501

        self._layout_id = None
        self._display_order = None
        self.discriminator = None

        if layout_id is not None:
            self.layout_id = layout_id
        if display_order is not None:
            self.display_order = display_order

    @property
    def layout_id(self):
        """Gets the layout_id of this LayoutAssignmentArray.  # noqa: E501

        Model to use for supplying key/value pairs to arrays  # noqa: E501

        :return: The layout_id of this LayoutAssignmentArray.  # noqa: E501
        :rtype: int
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this LayoutAssignmentArray.

        Model to use for supplying key/value pairs to arrays  # noqa: E501

        :param layout_id: The layout_id of this LayoutAssignmentArray.  # noqa: E501
        :type: int
        """

        self._layout_id = layout_id

    @property
    def display_order(self):
        """Gets the display_order of this LayoutAssignmentArray.  # noqa: E501

        Model to use for supplying key/value pairs to arrays  # noqa: E501

        :return: The display_order of this LayoutAssignmentArray.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this LayoutAssignmentArray.

        Model to use for supplying key/value pairs to arrays  # noqa: E501

        :param display_order: The display_order of this LayoutAssignmentArray.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

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
        if not isinstance(other, LayoutAssignmentArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
