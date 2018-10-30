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


class DataSet(object):
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
        'data_set_id': 'int',
        'data_set': 'str',
        'description': 'str',
        'user_id': 'int',
        'last_data_edit': 'int',
        'owner': 'str',
        'groups_with_permissions': 'str',
        'code': 'str',
        'is_lookup': 'int',
        'is_remote': 'int',
        'method': 'str',
        'uri': 'str',
        'post_data': 'str',
        'authentication': 'str',
        'username': 'str',
        'password': 'str',
        'refresh_rate': 'int',
        'clear_rate': 'int',
        'runs_after': 'int',
        'last_sync': 'int',
        'last_clear': 'int',
        'data_root': 'str',
        'summarize': 'str',
        'summarize_field': 'str'
    }

    attribute_map = {
        'data_set_id': 'dataSetId',
        'data_set': 'dataSet',
        'description': 'description',
        'user_id': 'userId',
        'last_data_edit': 'lastDataEdit',
        'owner': 'owner',
        'groups_with_permissions': 'groupsWithPermissions',
        'code': 'code',
        'is_lookup': 'isLookup',
        'is_remote': 'isRemote',
        'method': 'method',
        'uri': 'uri',
        'post_data': 'postData',
        'authentication': 'authentication',
        'username': 'username',
        'password': 'password',
        'refresh_rate': 'refreshRate',
        'clear_rate': 'clearRate',
        'runs_after': 'runsAfter',
        'last_sync': 'lastSync',
        'last_clear': 'lastClear',
        'data_root': 'dataRoot',
        'summarize': 'summarize',
        'summarize_field': 'summarizeField'
    }

    def __init__(self, data_set_id=None, data_set=None, description=None, user_id=None, last_data_edit=None, owner=None, groups_with_permissions=None, code=None, is_lookup=None, is_remote=None, method=None, uri=None, post_data=None, authentication=None, username=None, password=None, refresh_rate=None, clear_rate=None, runs_after=None, last_sync=None, last_clear=None, data_root=None, summarize=None, summarize_field=None):  # noqa: E501
        """DataSet - a model defined in Swagger"""  # noqa: E501

        self._data_set_id = None
        self._data_set = None
        self._description = None
        self._user_id = None
        self._last_data_edit = None
        self._owner = None
        self._groups_with_permissions = None
        self._code = None
        self._is_lookup = None
        self._is_remote = None
        self._method = None
        self._uri = None
        self._post_data = None
        self._authentication = None
        self._username = None
        self._password = None
        self._refresh_rate = None
        self._clear_rate = None
        self._runs_after = None
        self._last_sync = None
        self._last_clear = None
        self._data_root = None
        self._summarize = None
        self._summarize_field = None
        self.discriminator = None

        if data_set_id is not None:
            self.data_set_id = data_set_id
        if data_set is not None:
            self.data_set = data_set
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id
        if last_data_edit is not None:
            self.last_data_edit = last_data_edit
        if owner is not None:
            self.owner = owner
        if groups_with_permissions is not None:
            self.groups_with_permissions = groups_with_permissions
        if code is not None:
            self.code = code
        if is_lookup is not None:
            self.is_lookup = is_lookup
        if is_remote is not None:
            self.is_remote = is_remote
        if method is not None:
            self.method = method
        if uri is not None:
            self.uri = uri
        if post_data is not None:
            self.post_data = post_data
        if authentication is not None:
            self.authentication = authentication
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if refresh_rate is not None:
            self.refresh_rate = refresh_rate
        if clear_rate is not None:
            self.clear_rate = clear_rate
        if runs_after is not None:
            self.runs_after = runs_after
        if last_sync is not None:
            self.last_sync = last_sync
        if last_clear is not None:
            self.last_clear = last_clear
        if data_root is not None:
            self.data_root = data_root
        if summarize is not None:
            self.summarize = summarize
        if summarize_field is not None:
            self.summarize_field = summarize_field

    @property
    def data_set_id(self):
        """Gets the data_set_id of this DataSet.  # noqa: E501

        The dataSetId  # noqa: E501

        :return: The data_set_id of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._data_set_id

    @data_set_id.setter
    def data_set_id(self, data_set_id):
        """Sets the data_set_id of this DataSet.

        The dataSetId  # noqa: E501

        :param data_set_id: The data_set_id of this DataSet.  # noqa: E501
        :type: int
        """

        self._data_set_id = data_set_id

    @property
    def data_set(self):
        """Gets the data_set of this DataSet.  # noqa: E501

        The dataSet Name  # noqa: E501

        :return: The data_set of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._data_set

    @data_set.setter
    def data_set(self, data_set):
        """Sets the data_set of this DataSet.

        The dataSet Name  # noqa: E501

        :param data_set: The data_set of this DataSet.  # noqa: E501
        :type: str
        """

        self._data_set = data_set

    @property
    def description(self):
        """Gets the description of this DataSet.  # noqa: E501

        The dataSet description  # noqa: E501

        :return: The description of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataSet.

        The dataSet description  # noqa: E501

        :param description: The description of this DataSet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def user_id(self):
        """Gets the user_id of this DataSet.  # noqa: E501

        The userId of the User that owns this DataSet  # noqa: E501

        :return: The user_id of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DataSet.

        The userId of the User that owns this DataSet  # noqa: E501

        :param user_id: The user_id of this DataSet.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def last_data_edit(self):
        """Gets the last_data_edit of this DataSet.  # noqa: E501

        Timestamp indicating the date/time this DataSet was edited last  # noqa: E501

        :return: The last_data_edit of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._last_data_edit

    @last_data_edit.setter
    def last_data_edit(self, last_data_edit):
        """Sets the last_data_edit of this DataSet.

        Timestamp indicating the date/time this DataSet was edited last  # noqa: E501

        :param last_data_edit: The last_data_edit of this DataSet.  # noqa: E501
        :type: int
        """

        self._last_data_edit = last_data_edit

    @property
    def owner(self):
        """Gets the owner of this DataSet.  # noqa: E501

        The user name of the User that owns this DataSet  # noqa: E501

        :return: The owner of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DataSet.

        The user name of the User that owns this DataSet  # noqa: E501

        :param owner: The owner of this DataSet.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def groups_with_permissions(self):
        """Gets the groups_with_permissions of this DataSet.  # noqa: E501

        A comma separated list of Groups/Users that have permission to this DataSet  # noqa: E501

        :return: The groups_with_permissions of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._groups_with_permissions

    @groups_with_permissions.setter
    def groups_with_permissions(self, groups_with_permissions):
        """Sets the groups_with_permissions of this DataSet.

        A comma separated list of Groups/Users that have permission to this DataSet  # noqa: E501

        :param groups_with_permissions: The groups_with_permissions of this DataSet.  # noqa: E501
        :type: str
        """

        self._groups_with_permissions = groups_with_permissions

    @property
    def code(self):
        """Gets the code of this DataSet.  # noqa: E501

        A code for this Data Set  # noqa: E501

        :return: The code of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DataSet.

        A code for this Data Set  # noqa: E501

        :param code: The code of this DataSet.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def is_lookup(self):
        """Gets the is_lookup of this DataSet.  # noqa: E501

        Flag to indicate whether this DataSet is a lookup table  # noqa: E501

        :return: The is_lookup of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._is_lookup

    @is_lookup.setter
    def is_lookup(self, is_lookup):
        """Sets the is_lookup of this DataSet.

        Flag to indicate whether this DataSet is a lookup table  # noqa: E501

        :param is_lookup: The is_lookup of this DataSet.  # noqa: E501
        :type: int
        """

        self._is_lookup = is_lookup

    @property
    def is_remote(self):
        """Gets the is_remote of this DataSet.  # noqa: E501

        Flag to indicate whether this DataSet is Remote  # noqa: E501

        :return: The is_remote of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._is_remote

    @is_remote.setter
    def is_remote(self, is_remote):
        """Sets the is_remote of this DataSet.

        Flag to indicate whether this DataSet is Remote  # noqa: E501

        :param is_remote: The is_remote of this DataSet.  # noqa: E501
        :type: int
        """

        self._is_remote = is_remote

    @property
    def method(self):
        """Gets the method of this DataSet.  # noqa: E501

        Method to fetch the Data, can be GET or POST  # noqa: E501

        :return: The method of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this DataSet.

        Method to fetch the Data, can be GET or POST  # noqa: E501

        :param method: The method of this DataSet.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def uri(self):
        """Gets the uri of this DataSet.  # noqa: E501

        URI to call to fetch Data from. Replacements are {{DATE}}, {{TIME}} and, in case this is a sequencial used DataSet, {{COL.NAME}} where NAME is a ColumnName from the underlying DataSet.  # noqa: E501

        :return: The uri of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DataSet.

        URI to call to fetch Data from. Replacements are {{DATE}}, {{TIME}} and, in case this is a sequencial used DataSet, {{COL.NAME}} where NAME is a ColumnName from the underlying DataSet.  # noqa: E501

        :param uri: The uri of this DataSet.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def post_data(self):
        """Gets the post_data of this DataSet.  # noqa: E501

        Data to send as POST-Data to the remote host with the same Replacements as in the URI.  # noqa: E501

        :return: The post_data of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._post_data

    @post_data.setter
    def post_data(self, post_data):
        """Sets the post_data of this DataSet.

        Data to send as POST-Data to the remote host with the same Replacements as in the URI.  # noqa: E501

        :param post_data: The post_data of this DataSet.  # noqa: E501
        :type: str
        """

        self._post_data = post_data

    @property
    def authentication(self):
        """Gets the authentication of this DataSet.  # noqa: E501

        Authentication method, can be none, digest, basic  # noqa: E501

        :return: The authentication of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this DataSet.

        Authentication method, can be none, digest, basic  # noqa: E501

        :param authentication: The authentication of this DataSet.  # noqa: E501
        :type: str
        """

        self._authentication = authentication

    @property
    def username(self):
        """Gets the username of this DataSet.  # noqa: E501

        Username to authenticate with  # noqa: E501

        :return: The username of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DataSet.

        Username to authenticate with  # noqa: E501

        :param username: The username of this DataSet.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this DataSet.  # noqa: E501

        Corresponding password  # noqa: E501

        :return: The password of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DataSet.

        Corresponding password  # noqa: E501

        :param password: The password of this DataSet.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def refresh_rate(self):
        """Gets the refresh_rate of this DataSet.  # noqa: E501

        Time in seconds this DataSet should fetch new Datas from the remote host  # noqa: E501

        :return: The refresh_rate of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._refresh_rate

    @refresh_rate.setter
    def refresh_rate(self, refresh_rate):
        """Sets the refresh_rate of this DataSet.

        Time in seconds this DataSet should fetch new Datas from the remote host  # noqa: E501

        :param refresh_rate: The refresh_rate of this DataSet.  # noqa: E501
        :type: int
        """

        self._refresh_rate = refresh_rate

    @property
    def clear_rate(self):
        """Gets the clear_rate of this DataSet.  # noqa: E501

        Time in seconds when this Dataset should be cleared. If here is a lower value than in RefreshRate it will be cleared when the data is refreshed  # noqa: E501

        :return: The clear_rate of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._clear_rate

    @clear_rate.setter
    def clear_rate(self, clear_rate):
        """Sets the clear_rate of this DataSet.

        Time in seconds when this Dataset should be cleared. If here is a lower value than in RefreshRate it will be cleared when the data is refreshed  # noqa: E501

        :param clear_rate: The clear_rate of this DataSet.  # noqa: E501
        :type: int
        """

        self._clear_rate = clear_rate

    @property
    def runs_after(self):
        """Gets the runs_after of this DataSet.  # noqa: E501

        DataSetID of the DataSet which should be fetched and present before the Data from this DataSet are fetched  # noqa: E501

        :return: The runs_after of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._runs_after

    @runs_after.setter
    def runs_after(self, runs_after):
        """Sets the runs_after of this DataSet.

        DataSetID of the DataSet which should be fetched and present before the Data from this DataSet are fetched  # noqa: E501

        :param runs_after: The runs_after of this DataSet.  # noqa: E501
        :type: int
        """

        self._runs_after = runs_after

    @property
    def last_sync(self):
        """Gets the last_sync of this DataSet.  # noqa: E501

        Last Synchronisation Timestamp  # noqa: E501

        :return: The last_sync of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this DataSet.

        Last Synchronisation Timestamp  # noqa: E501

        :param last_sync: The last_sync of this DataSet.  # noqa: E501
        :type: int
        """

        self._last_sync = last_sync

    @property
    def last_clear(self):
        """Gets the last_clear of this DataSet.  # noqa: E501

        Last Clear Timestamp  # noqa: E501

        :return: The last_clear of this DataSet.  # noqa: E501
        :rtype: int
        """
        return self._last_clear

    @last_clear.setter
    def last_clear(self, last_clear):
        """Sets the last_clear of this DataSet.

        Last Clear Timestamp  # noqa: E501

        :param last_clear: The last_clear of this DataSet.  # noqa: E501
        :type: int
        """

        self._last_clear = last_clear

    @property
    def data_root(self):
        """Gets the data_root of this DataSet.  # noqa: E501

        Root-Element form JSON where the data are stored in  # noqa: E501

        :return: The data_root of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._data_root

    @data_root.setter
    def data_root(self, data_root):
        """Sets the data_root of this DataSet.

        Root-Element form JSON where the data are stored in  # noqa: E501

        :param data_root: The data_root of this DataSet.  # noqa: E501
        :type: str
        """

        self._data_root = data_root

    @property
    def summarize(self):
        """Gets the summarize of this DataSet.  # noqa: E501

        Optional function to use for summarize or count unique fields in a remote request  # noqa: E501

        :return: The summarize of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._summarize

    @summarize.setter
    def summarize(self, summarize):
        """Sets the summarize of this DataSet.

        Optional function to use for summarize or count unique fields in a remote request  # noqa: E501

        :param summarize: The summarize of this DataSet.  # noqa: E501
        :type: str
        """

        self._summarize = summarize

    @property
    def summarize_field(self):
        """Gets the summarize_field of this DataSet.  # noqa: E501

        JSON-Element below the Root-Element on which the consolidation should be applied on  # noqa: E501

        :return: The summarize_field of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._summarize_field

    @summarize_field.setter
    def summarize_field(self, summarize_field):
        """Sets the summarize_field of this DataSet.

        JSON-Element below the Root-Element on which the consolidation should be applied on  # noqa: E501

        :param summarize_field: The summarize_field of this DataSet.  # noqa: E501
        :type: str
        """

        self._summarize_field = summarize_field

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
        if not isinstance(other, DataSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
