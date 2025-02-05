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


class Module(object):
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
        'module_id': 'int',
        'name': 'str',
        'description': 'str',
        'valid_extensions': 'str',
        'image_uri': 'str',
        'type': 'str',
        'enabled': 'int',
        'region_specific': 'int',
        'preview_enabled': 'int',
        'assignable': 'int',
        'render_as': 'str',
        'default_duration': 'int',
        'settings': 'list[str]',
        'schema_version': 'int',
        '_class': 'str',
        'view_path': 'str',
        'install_name': 'str'
    }

    attribute_map = {
        'module_id': 'moduleId',
        'name': 'name',
        'description': 'description',
        'valid_extensions': 'validExtensions',
        'image_uri': 'imageUri',
        'type': 'type',
        'enabled': 'enabled',
        'region_specific': 'regionSpecific',
        'preview_enabled': 'previewEnabled',
        'assignable': 'assignable',
        'render_as': 'renderAs',
        'default_duration': 'defaultDuration',
        'settings': 'settings',
        'schema_version': 'schemaVersion',
        '_class': 'class',
        'view_path': 'viewPath',
        'install_name': 'installName'
    }

    def __init__(self, module_id=None, name=None, description=None, valid_extensions=None, image_uri=None, type=None, enabled=None, region_specific=None, preview_enabled=None, assignable=None, render_as=None, default_duration=None, settings=None, schema_version=None, _class=None, view_path=None, install_name=None):  # noqa: E501
        """Module - a model defined in Swagger"""  # noqa: E501

        self._module_id = None
        self._name = None
        self._description = None
        self._valid_extensions = None
        self._image_uri = None
        self._type = None
        self._enabled = None
        self._region_specific = None
        self._preview_enabled = None
        self._assignable = None
        self._render_as = None
        self._default_duration = None
        self._settings = None
        self._schema_version = None
        self.__class = None
        self._view_path = None
        self._install_name = None
        self.discriminator = None

        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if valid_extensions is not None:
            self.valid_extensions = valid_extensions
        if image_uri is not None:
            self.image_uri = image_uri
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if region_specific is not None:
            self.region_specific = region_specific
        if preview_enabled is not None:
            self.preview_enabled = preview_enabled
        if assignable is not None:
            self.assignable = assignable
        if render_as is not None:
            self.render_as = render_as
        if default_duration is not None:
            self.default_duration = default_duration
        if settings is not None:
            self.settings = settings
        if schema_version is not None:
            self.schema_version = schema_version
        if _class is not None:
            self._class = _class
        if view_path is not None:
            self.view_path = view_path
        if install_name is not None:
            self.install_name = install_name

    @property
    def module_id(self):
        """Gets the module_id of this Module.  # noqa: E501

        The ID of this Module  # noqa: E501

        :return: The module_id of this Module.  # noqa: E501
        :rtype: int
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this Module.

        The ID of this Module  # noqa: E501

        :param module_id: The module_id of this Module.  # noqa: E501
        :type: int
        """

        self._module_id = module_id

    @property
    def name(self):
        """Gets the name of this Module.  # noqa: E501

        Module Name  # noqa: E501

        :return: The name of this Module.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Module.

        Module Name  # noqa: E501

        :param name: The name of this Module.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Module.  # noqa: E501

        Description of the Module  # noqa: E501

        :return: The description of this Module.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Module.

        Description of the Module  # noqa: E501

        :param description: The description of this Module.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def valid_extensions(self):
        """Gets the valid_extensions of this Module.  # noqa: E501

        A comma separated list of Valid Extensions  # noqa: E501

        :return: The valid_extensions of this Module.  # noqa: E501
        :rtype: str
        """
        return self._valid_extensions

    @valid_extensions.setter
    def valid_extensions(self, valid_extensions):
        """Sets the valid_extensions of this Module.

        A comma separated list of Valid Extensions  # noqa: E501

        :param valid_extensions: The valid_extensions of this Module.  # noqa: E501
        :type: str
        """

        self._valid_extensions = valid_extensions

    @property
    def image_uri(self):
        """Gets the image_uri of this Module.  # noqa: E501

        The file uri of an image to represent this Module  # noqa: E501

        :return: The image_uri of this Module.  # noqa: E501
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """Sets the image_uri of this Module.

        The file uri of an image to represent this Module  # noqa: E501

        :param image_uri: The image_uri of this Module.  # noqa: E501
        :type: str
        """

        self._image_uri = image_uri

    @property
    def type(self):
        """Gets the type of this Module.  # noqa: E501

        The type code for this module  # noqa: E501

        :return: The type of this Module.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Module.

        The type code for this module  # noqa: E501

        :param type: The type of this Module.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this Module.  # noqa: E501

        A flag indicating whether this module is enabled  # noqa: E501

        :return: The enabled of this Module.  # noqa: E501
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Module.

        A flag indicating whether this module is enabled  # noqa: E501

        :param enabled: The enabled of this Module.  # noqa: E501
        :type: int
        """

        self._enabled = enabled

    @property
    def region_specific(self):
        """Gets the region_specific of this Module.  # noqa: E501

        A flag indicating whether this module is specific to a Layout or can be uploaded to the Library  # noqa: E501

        :return: The region_specific of this Module.  # noqa: E501
        :rtype: int
        """
        return self._region_specific

    @region_specific.setter
    def region_specific(self, region_specific):
        """Sets the region_specific of this Module.

        A flag indicating whether this module is specific to a Layout or can be uploaded to the Library  # noqa: E501

        :param region_specific: The region_specific of this Module.  # noqa: E501
        :type: int
        """

        self._region_specific = region_specific

    @property
    def preview_enabled(self):
        """Gets the preview_enabled of this Module.  # noqa: E501

        A flag indicating whether the Layout designer should render a preview of this module  # noqa: E501

        :return: The preview_enabled of this Module.  # noqa: E501
        :rtype: int
        """
        return self._preview_enabled

    @preview_enabled.setter
    def preview_enabled(self, preview_enabled):
        """Sets the preview_enabled of this Module.

        A flag indicating whether the Layout designer should render a preview of this module  # noqa: E501

        :param preview_enabled: The preview_enabled of this Module.  # noqa: E501
        :type: int
        """

        self._preview_enabled = preview_enabled

    @property
    def assignable(self):
        """Gets the assignable of this Module.  # noqa: E501

        A flag indicating whether the module is assignable to a Layout  # noqa: E501

        :return: The assignable of this Module.  # noqa: E501
        :rtype: int
        """
        return self._assignable

    @assignable.setter
    def assignable(self, assignable):
        """Sets the assignable of this Module.

        A flag indicating whether the module is assignable to a Layout  # noqa: E501

        :param assignable: The assignable of this Module.  # noqa: E501
        :type: int
        """

        self._assignable = assignable

    @property
    def render_as(self):
        """Gets the render_as of this Module.  # noqa: E501

        A flag indicating whether the module should be rendered natively by the Player or via the CMS (native|html)  # noqa: E501

        :return: The render_as of this Module.  # noqa: E501
        :rtype: str
        """
        return self._render_as

    @render_as.setter
    def render_as(self, render_as):
        """Sets the render_as of this Module.

        A flag indicating whether the module should be rendered natively by the Player or via the CMS (native|html)  # noqa: E501

        :param render_as: The render_as of this Module.  # noqa: E501
        :type: str
        """

        self._render_as = render_as

    @property
    def default_duration(self):
        """Gets the default_duration of this Module.  # noqa: E501

        The default duration for Widgets of this Module when the user has elected to not set a specific duration.  # noqa: E501

        :return: The default_duration of this Module.  # noqa: E501
        :rtype: int
        """
        return self._default_duration

    @default_duration.setter
    def default_duration(self, default_duration):
        """Sets the default_duration of this Module.

        The default duration for Widgets of this Module when the user has elected to not set a specific duration.  # noqa: E501

        :param default_duration: The default_duration of this Module.  # noqa: E501
        :type: int
        """

        self._default_duration = default_duration

    @property
    def settings(self):
        """Gets the settings of this Module.  # noqa: E501

        An array of additional module specific settings  # noqa: E501

        :return: The settings of this Module.  # noqa: E501
        :rtype: list[str]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Module.

        An array of additional module specific settings  # noqa: E501

        :param settings: The settings of this Module.  # noqa: E501
        :type: list[str]
        """

        self._settings = settings

    @property
    def schema_version(self):
        """Gets the schema_version of this Module.  # noqa: E501

        The schema version of the module  # noqa: E501

        :return: The schema_version of this Module.  # noqa: E501
        :rtype: int
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this Module.

        The schema version of the module  # noqa: E501

        :param schema_version: The schema_version of this Module.  # noqa: E501
        :type: int
        """

        self._schema_version = schema_version

    @property
    def _class(self):
        """Gets the _class of this Module.  # noqa: E501

        Class Name including namespace  # noqa: E501

        :return: The _class of this Module.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Module.

        Class Name including namespace  # noqa: E501

        :param _class: The _class of this Module.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def view_path(self):
        """Gets the view_path of this Module.  # noqa: E501

        The Twig View path for module specific templates  # noqa: E501

        :return: The view_path of this Module.  # noqa: E501
        :rtype: str
        """
        return self._view_path

    @view_path.setter
    def view_path(self, view_path):
        """Sets the view_path of this Module.

        The Twig View path for module specific templates  # noqa: E501

        :param view_path: The view_path of this Module.  # noqa: E501
        :type: str
        """

        self._view_path = view_path

    @property
    def install_name(self):
        """Gets the install_name of this Module.  # noqa: E501

        The original installation name of this module.  # noqa: E501

        :return: The install_name of this Module.  # noqa: E501
        :rtype: str
        """
        return self._install_name

    @install_name.setter
    def install_name(self, install_name):
        """Sets the install_name of this Module.

        The original installation name of this module.  # noqa: E501

        :param install_name: The install_name of this Module.  # noqa: E501
        :type: str
        """

        self._install_name = install_name

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
        if not isinstance(other, Module):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
