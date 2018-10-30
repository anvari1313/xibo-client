# swagger_client.UsergroupApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_group_add**](UsergroupApi.md#user_group_add) | **POST** /group | UserGroup Add
[**user_group_assign**](UsergroupApi.md#user_group_assign) | **POST** group/members/assign/{userGroupId} | Assign User to User Group
[**user_group_copy**](UsergroupApi.md#user_group_copy) | **POST** /group/{userGroupId}/copy | Copy User Group
[**user_group_delete**](UsergroupApi.md#user_group_delete) | **DELETE** /group/{userGroupId} | Delete User Group
[**user_group_edit**](UsergroupApi.md#user_group_edit) | **PUT** /group/{userGroupId} | UserGroup Edit
[**user_group_search**](UsergroupApi.md#user_group_search) | **GET** /group | UserGroup Search
[**user_group_unassign**](UsergroupApi.md#user_group_unassign) | **POST** group/members/unassign/{userGroupId} | Unassign User from User Group


# **user_group_add**
> list[UserGroup] user_group_add(group, library_quota=library_quota, is_system_notification=is_system_notification, is_display_notification=is_display_notification)

UserGroup Add

Add User Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
group = 'group_example' # str | Name of the User Group
library_quota = 'library_quota_example' # str | The quota that should be applied (KiB). Provide 0 for no quota (optional)
is_system_notification = 56 # int | Flag (0, 1), should members of this Group receive system notifications? (optional)
is_display_notification = 56 # int | Flag (0, 1), should members of this Group receive Display notifications for Displays they have permissions to see (optional)

try:
    # UserGroup Add
    api_response = api_instance.user_group_add(group, library_quota=library_quota, is_system_notification=is_system_notification, is_display_notification=is_display_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Name of the User Group | 
 **library_quota** | **str**| The quota that should be applied (KiB). Provide 0 for no quota | [optional] 
 **is_system_notification** | **int**| Flag (0, 1), should members of this Group receive system notifications? | [optional] 
 **is_display_notification** | **int**| Flag (0, 1), should members of this Group receive Display notifications for Displays they have permissions to see | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_assign**
> list[UserGroup] user_group_assign(user_group_id, user_id)

Assign User to User Group

Assign User to User Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 'user_group_id_example' # str | ID of the user group to which assign the user
user_id = [56] # list[int] | Array of userIDs to assign

try:
    # Assign User to User Group
    api_response = api_instance.user_group_assign(user_group_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group to which assign the user | 
 **user_id** | [**list[int]**](int.md)| Array of userIDs to assign | 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_copy**
> UserGroup user_group_copy(user_group_id, group, copy_members=copy_members)

Copy User Group

Copy an user group, optionally copying the group members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 56 # int | The User Group ID to Copy
group = 'group_example' # str | The Group Name
copy_members = 56 # int | Flag indicating whether to copy group members (optional)

try:
    # Copy User Group
    api_response = api_instance.user_group_copy(user_group_id, group, copy_members=copy_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**| The User Group ID to Copy | 
 **group** | **str**| The Group Name | 
 **copy_members** | **int**| Flag indicating whether to copy group members | [optional] 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_delete**
> user_group_delete(user_group_id)

Delete User Group

Delete User Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 56 # int | The user Group ID to Delete

try:
    # Delete User Group
    api_instance.user_group_delete(user_group_id)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**| The user Group ID to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_edit**
> list[UserGroup] user_group_edit(user_group_id, group, library_quota=library_quota, is_system_notification=is_system_notification, is_display_notification=is_display_notification)

UserGroup Edit

Edit User Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 56 # int | ID of the User Group
group = 'group_example' # str | Name of the User Group
library_quota = 'library_quota_example' # str | The quota that should be applied (KiB). Provide 0 for no quota (optional)
is_system_notification = 56 # int | Flag (0, 1), should members of this Group receive system notifications? (optional)
is_display_notification = 56 # int | Flag (0, 1), should members of this Group receive Display notifications for Displays they have permissions to see (optional)

try:
    # UserGroup Edit
    api_response = api_instance.user_group_edit(user_group_id, group, library_quota=library_quota, is_system_notification=is_system_notification, is_display_notification=is_display_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**| ID of the User Group | 
 **group** | **str**| Name of the User Group | 
 **library_quota** | **str**| The quota that should be applied (KiB). Provide 0 for no quota | [optional] 
 **is_system_notification** | **int**| Flag (0, 1), should members of this Group receive system notifications? | [optional] 
 **is_display_notification** | **int**| Flag (0, 1), should members of this Group receive Display notifications for Displays they have permissions to see | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_search**
> list[UserGroup] user_group_search(user_group_id=user_group_id, user_group=user_group)

UserGroup Search

Search User Groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 56 # int | Filter by UserGroup Id (optional)
user_group = 'user_group_example' # str | Filter by UserGroup Name (optional)

try:
    # UserGroup Search
    api_response = api_instance.user_group_search(user_group_id=user_group_id, user_group=user_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **int**| Filter by UserGroup Id | [optional] 
 **user_group** | **str**| Filter by UserGroup Name | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_unassign**
> list[UserGroup] user_group_unassign(user_group_id, user_id)

Unassign User from User Group

Unassign User from User Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsergroupApi(swagger_client.ApiClient(configuration))
user_group_id = 'user_group_id_example' # str | ID of the user group from which to unassign the user
user_id = [56] # list[int] | Array of userIDs to unassign

try:
    # Unassign User from User Group
    api_response = api_instance.user_group_unassign(user_group_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->user_group_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group from which to unassign the user | 
 **user_id** | [**list[int]**](int.md)| Array of userIDs to unassign | 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

