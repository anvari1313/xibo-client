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

from swagger_client.models.tag import Tag  # noqa: F401,E501


class Media(object):
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
        'media_id': 'int',
        'owner_id': 'int',
        'parent_id': 'int',
        'name': 'str',
        'media_type': 'int',
        'stored_as': 'str',
        'file_name': 'str',
        'tags': 'list[Tag]',
        'file_size': 'int',
        'duration': 'int',
        'valid': 'int',
        'module_system_file': 'int',
        'expires': 'int',
        'retired': 'int',
        'is_edited': 'int',
        'md5': 'str',
        'owner': 'str',
        'groups_with_permissions': 'str',
        'released': 'int',
        'api_ref': 'str',
        'created_dt': 'str',
        'modified_dt': 'str'
    }

    attribute_map = {
        'media_id': 'mediaId',
        'owner_id': 'ownerId',
        'parent_id': 'parentId',
        'name': 'name',
        'media_type': 'mediaType',
        'stored_as': 'storedAs',
        'file_name': 'fileName',
        'tags': 'tags',
        'file_size': 'fileSize',
        'duration': 'duration',
        'valid': 'valid',
        'module_system_file': 'moduleSystemFile',
        'expires': 'expires',
        'retired': 'retired',
        'is_edited': 'isEdited',
        'md5': 'md5',
        'owner': 'owner',
        'groups_with_permissions': 'groupsWithPermissions',
        'released': 'released',
        'api_ref': 'apiRef',
        'created_dt': 'createdDt',
        'modified_dt': 'modifiedDt'
    }

    def __init__(self, media_id=None, owner_id=None, parent_id=None, name=None, media_type=None, stored_as=None, file_name=None, tags=None, file_size=None, duration=None, valid=None, module_system_file=None, expires=None, retired=None, is_edited=None, md5=None, owner=None, groups_with_permissions=None, released=None, api_ref=None, created_dt=None, modified_dt=None):  # noqa: E501
        """Media - a model defined in Swagger"""  # noqa: E501

        self._media_id = None
        self._owner_id = None
        self._parent_id = None
        self._name = None
        self._media_type = None
        self._stored_as = None
        self._file_name = None
        self._tags = None
        self._file_size = None
        self._duration = None
        self._valid = None
        self._module_system_file = None
        self._expires = None
        self._retired = None
        self._is_edited = None
        self._md5 = None
        self._owner = None
        self._groups_with_permissions = None
        self._released = None
        self._api_ref = None
        self._created_dt = None
        self._modified_dt = None
        self.discriminator = None

        if media_id is not None:
            self.media_id = media_id
        if owner_id is not None:
            self.owner_id = owner_id
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if media_type is not None:
            self.media_type = media_type
        if stored_as is not None:
            self.stored_as = stored_as
        if file_name is not None:
            self.file_name = file_name
        if tags is not None:
            self.tags = tags
        if file_size is not None:
            self.file_size = file_size
        if duration is not None:
            self.duration = duration
        if valid is not None:
            self.valid = valid
        if module_system_file is not None:
            self.module_system_file = module_system_file
        if expires is not None:
            self.expires = expires
        if retired is not None:
            self.retired = retired
        if is_edited is not None:
            self.is_edited = is_edited
        if md5 is not None:
            self.md5 = md5
        if owner is not None:
            self.owner = owner
        if groups_with_permissions is not None:
            self.groups_with_permissions = groups_with_permissions
        if released is not None:
            self.released = released
        if api_ref is not None:
            self.api_ref = api_ref
        if created_dt is not None:
            self.created_dt = created_dt
        if modified_dt is not None:
            self.modified_dt = modified_dt

    @property
    def media_id(self):
        """Gets the media_id of this Media.  # noqa: E501

        The Media ID  # noqa: E501

        :return: The media_id of this Media.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this Media.

        The Media ID  # noqa: E501

        :param media_id: The media_id of this Media.  # noqa: E501
        :type: int
        """

        self._media_id = media_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Media.  # noqa: E501

        The ID of the User that owns this Media  # noqa: E501

        :return: The owner_id of this Media.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Media.

        The ID of the User that owns this Media  # noqa: E501

        :param owner_id: The owner_id of this Media.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def parent_id(self):
        """Gets the parent_id of this Media.  # noqa: E501

        The Parent ID of this Media if it has been revised  # noqa: E501

        :return: The parent_id of this Media.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Media.

        The Parent ID of this Media if it has been revised  # noqa: E501

        :param parent_id: The parent_id of this Media.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this Media.  # noqa: E501

        The Name of this Media  # noqa: E501

        :return: The name of this Media.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Media.

        The Name of this Media  # noqa: E501

        :param name: The name of this Media.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def media_type(self):
        """Gets the media_type of this Media.  # noqa: E501

        The module type of this Media  # noqa: E501

        :return: The media_type of this Media.  # noqa: E501
        :rtype: int
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Media.

        The module type of this Media  # noqa: E501

        :param media_type: The media_type of this Media.  # noqa: E501
        :type: int
        """

        self._media_type = media_type

    @property
    def stored_as(self):
        """Gets the stored_as of this Media.  # noqa: E501

        The file name of the media as stored in the library  # noqa: E501

        :return: The stored_as of this Media.  # noqa: E501
        :rtype: str
        """
        return self._stored_as

    @stored_as.setter
    def stored_as(self, stored_as):
        """Sets the stored_as of this Media.

        The file name of the media as stored in the library  # noqa: E501

        :param stored_as: The stored_as of this Media.  # noqa: E501
        :type: str
        """

        self._stored_as = stored_as

    @property
    def file_name(self):
        """Gets the file_name of this Media.  # noqa: E501

        The original file name as it was uploaded  # noqa: E501

        :return: The file_name of this Media.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Media.

        The original file name as it was uploaded  # noqa: E501

        :param file_name: The file_name of this Media.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def tags(self):
        """Gets the tags of this Media.  # noqa: E501

        Tags associated with this Media  # noqa: E501

        :return: The tags of this Media.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Media.

        Tags associated with this Media  # noqa: E501

        :param tags: The tags of this Media.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def file_size(self):
        """Gets the file_size of this Media.  # noqa: E501

        The file size in bytes  # noqa: E501

        :return: The file_size of this Media.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this Media.

        The file size in bytes  # noqa: E501

        :param file_size: The file_size of this Media.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def duration(self):
        """Gets the duration of this Media.  # noqa: E501

        The duration to use when assigning this media to a Layout widget  # noqa: E501

        :return: The duration of this Media.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Media.

        The duration to use when assigning this media to a Layout widget  # noqa: E501

        :param duration: The duration of this Media.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def valid(self):
        """Gets the valid of this Media.  # noqa: E501

        Flag indicating whether this media is valid.  # noqa: E501

        :return: The valid of this Media.  # noqa: E501
        :rtype: int
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Media.

        Flag indicating whether this media is valid.  # noqa: E501

        :param valid: The valid of this Media.  # noqa: E501
        :type: int
        """

        self._valid = valid

    @property
    def module_system_file(self):
        """Gets the module_system_file of this Media.  # noqa: E501

        Flag indicating whether this media is a system file or not  # noqa: E501

        :return: The module_system_file of this Media.  # noqa: E501
        :rtype: int
        """
        return self._module_system_file

    @module_system_file.setter
    def module_system_file(self, module_system_file):
        """Sets the module_system_file of this Media.

        Flag indicating whether this media is a system file or not  # noqa: E501

        :param module_system_file: The module_system_file of this Media.  # noqa: E501
        :type: int
        """

        self._module_system_file = module_system_file

    @property
    def expires(self):
        """Gets the expires of this Media.  # noqa: E501

        Timestamp indicating when this media should expire  # noqa: E501

        :return: The expires of this Media.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this Media.

        Timestamp indicating when this media should expire  # noqa: E501

        :param expires: The expires of this Media.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def retired(self):
        """Gets the retired of this Media.  # noqa: E501

        Flag indicating whether this media is retired  # noqa: E501

        :return: The retired of this Media.  # noqa: E501
        :rtype: int
        """
        return self._retired

    @retired.setter
    def retired(self, retired):
        """Sets the retired of this Media.

        Flag indicating whether this media is retired  # noqa: E501

        :param retired: The retired of this Media.  # noqa: E501
        :type: int
        """

        self._retired = retired

    @property
    def is_edited(self):
        """Gets the is_edited of this Media.  # noqa: E501

        Flag indicating whether this media has been edited and replaced with a newer file  # noqa: E501

        :return: The is_edited of this Media.  # noqa: E501
        :rtype: int
        """
        return self._is_edited

    @is_edited.setter
    def is_edited(self, is_edited):
        """Sets the is_edited of this Media.

        Flag indicating whether this media has been edited and replaced with a newer file  # noqa: E501

        :param is_edited: The is_edited of this Media.  # noqa: E501
        :type: int
        """

        self._is_edited = is_edited

    @property
    def md5(self):
        """Gets the md5 of this Media.  # noqa: E501

        A MD5 checksum of the stored media file  # noqa: E501

        :return: The md5 of this Media.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Media.

        A MD5 checksum of the stored media file  # noqa: E501

        :param md5: The md5 of this Media.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def owner(self):
        """Gets the owner of this Media.  # noqa: E501

        The username of the User that owns this media  # noqa: E501

        :return: The owner of this Media.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Media.

        The username of the User that owns this media  # noqa: E501

        :param owner: The owner of this Media.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def groups_with_permissions(self):
        """Gets the groups_with_permissions of this Media.  # noqa: E501

        A comma separated list of groups/users with permissions to this Media  # noqa: E501

        :return: The groups_with_permissions of this Media.  # noqa: E501
        :rtype: str
        """
        return self._groups_with_permissions

    @groups_with_permissions.setter
    def groups_with_permissions(self, groups_with_permissions):
        """Sets the groups_with_permissions of this Media.

        A comma separated list of groups/users with permissions to this Media  # noqa: E501

        :param groups_with_permissions: The groups_with_permissions of this Media.  # noqa: E501
        :type: str
        """

        self._groups_with_permissions = groups_with_permissions

    @property
    def released(self):
        """Gets the released of this Media.  # noqa: E501

        A flag indicating whether this media has been released  # noqa: E501

        :return: The released of this Media.  # noqa: E501
        :rtype: int
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this Media.

        A flag indicating whether this media has been released  # noqa: E501

        :param released: The released of this Media.  # noqa: E501
        :type: int
        """

        self._released = released

    @property
    def api_ref(self):
        """Gets the api_ref of this Media.  # noqa: E501

        An API reference  # noqa: E501

        :return: The api_ref of this Media.  # noqa: E501
        :rtype: str
        """
        return self._api_ref

    @api_ref.setter
    def api_ref(self, api_ref):
        """Sets the api_ref of this Media.

        An API reference  # noqa: E501

        :param api_ref: The api_ref of this Media.  # noqa: E501
        :type: str
        """

        self._api_ref = api_ref

    @property
    def created_dt(self):
        """Gets the created_dt of this Media.  # noqa: E501

        The datetime the Media was created  # noqa: E501

        :return: The created_dt of this Media.  # noqa: E501
        :rtype: str
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Media.

        The datetime the Media was created  # noqa: E501

        :param created_dt: The created_dt of this Media.  # noqa: E501
        :type: str
        """

        self._created_dt = created_dt

    @property
    def modified_dt(self):
        """Gets the modified_dt of this Media.  # noqa: E501

        The datetime the Media was last modified  # noqa: E501

        :return: The modified_dt of this Media.  # noqa: E501
        :rtype: str
        """
        return self._modified_dt

    @modified_dt.setter
    def modified_dt(self, modified_dt):
        """Sets the modified_dt of this Media.

        The datetime the Media was last modified  # noqa: E501

        :param modified_dt: The modified_dt of this Media.  # noqa: E501
        :type: str
        """

        self._modified_dt = modified_dt

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
        if not isinstance(other, Media):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
