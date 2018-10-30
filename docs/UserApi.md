# swagger_client.UserApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_add**](UserApi.md#user_add) | **POST** /user | Add User
[**user_me**](UserApi.md#user_me) | **GET** /user/me | Get Me
[**user_permissions_search**](UserApi.md#user_permissions_search) | **GET** /user/permissions/{entity}/{objectId} | Permission Data
[**user_permissions_set**](UserApi.md#user_permissions_set) | **POST** /user/permissions/{entity}/{objectId} | Permission Set
[**user_pref_edit**](UserApi.md#user_pref_edit) | **POST** /user/pref | Save User Preferences
[**user_pref_get**](UserApi.md#user_pref_get) | **GET** /user/pref | Retrieve User Preferences
[**user_search**](UserApi.md#user_search) | **GET** /user | User Search


# **user_add**
> User user_add(user_name, user_type_id, home_page_id, password, group_id, new_user_wizard, hide_navigation, email=email, library_quota=library_quota, first_name=first_name, last_name=last_name, phone=phone, ref1=ref1, ref2=ref2, ref3=ref3, ref4=ref4, ref5=ref5)

Add User

Add a new User

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_name = 'user_name_example' # str | The User Name
user_type_id = 56 # int | The user type ID
home_page_id = 56 # int | The homepage to use for this User
password = 'password_example' # str | The users password
group_id = 56 # int | The inital user group for this User
new_user_wizard = 56 # int | Flag indicating whether to show the new user guide
hide_navigation = 56 # int | Flag indicating whether to hide the navigation
email = 'email_example' # str | The user email address (optional)
library_quota = 56 # int | The users library quota in kilobytes (optional)
first_name = 'first_name_example' # str | The users first name (optional)
last_name = 'last_name_example' # str | The users last name (optional)
phone = 'phone_example' # str | The users phone number (optional)
ref1 = 'ref1_example' # str | Reference 1 (optional)
ref2 = 'ref2_example' # str | Reference 2 (optional)
ref3 = 'ref3_example' # str | Reference 3 (optional)
ref4 = 'ref4_example' # str | Reference 4 (optional)
ref5 = 'ref5_example' # str | Reference 5 (optional)

try:
    # Add User
    api_response = api_instance.user_add(user_name, user_type_id, home_page_id, password, group_id, new_user_wizard, hide_navigation, email=email, library_quota=library_quota, first_name=first_name, last_name=last_name, phone=phone, ref1=ref1, ref2=ref2, ref3=ref3, ref4=ref4, ref5=ref5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| The User Name | 
 **user_type_id** | **int**| The user type ID | 
 **home_page_id** | **int**| The homepage to use for this User | 
 **password** | **str**| The users password | 
 **group_id** | **int**| The inital user group for this User | 
 **new_user_wizard** | **int**| Flag indicating whether to show the new user guide | 
 **hide_navigation** | **int**| Flag indicating whether to hide the navigation | 
 **email** | **str**| The user email address | [optional] 
 **library_quota** | **int**| The users library quota in kilobytes | [optional] 
 **first_name** | **str**| The users first name | [optional] 
 **last_name** | **str**| The users last name | [optional] 
 **phone** | **str**| The users phone number | [optional] 
 **ref1** | **str**| Reference 1 | [optional] 
 **ref2** | **str**| Reference 2 | [optional] 
 **ref3** | **str**| Reference 3 | [optional] 
 **ref4** | **str**| Reference 4 | [optional] 
 **ref5** | **str**| Reference 5 | [optional] 

### Return type

[**User**](User.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me**
> User user_me()

Get Me

Get my details

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get Me
    api_response = api_instance.user_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_permissions_search**
> list[Permission] user_permissions_search(entity, object_id)

Permission Data

Permission data for the Entity and Object Provided.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The Entity
object_id = 56 # int | The ID of the Object to return permissions for

try:
    # Permission Data
    api_response = api_instance.user_permissions_search(entity, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_permissions_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The Entity | 
 **object_id** | **int**| The ID of the Object to return permissions for | 

### Return type

[**list[Permission]**](Permission.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_permissions_set**
> user_permissions_set(entity, object_id, group_ids, owner_id=owner_id)

Permission Set

Set Permissions to users/groups for the provided entity.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The Entity
object_id = 56 # int | The ID of the Object to set permissions on
group_ids = ['group_ids_example'] # list[str] | Array of permissions with groupId as the key
owner_id = 56 # int | Change the owner of this item. Leave empty to keep the current owner (optional)

try:
    # Permission Set
    api_instance.user_permissions_set(entity, object_id, group_ids, owner_id=owner_id)
except ApiException as e:
    print("Exception when calling UserApi->user_permissions_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The Entity | 
 **object_id** | **int**| The ID of the Object to set permissions on | 
 **group_ids** | [**list[str]**](str.md)| Array of permissions with groupId as the key | 
 **owner_id** | **int**| Change the owner of this item. Leave empty to keep the current owner | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_pref_edit**
> user_pref_edit(preference)

Save User Preferences

Save User preferences for non-state information, such as Layout designer zoom levels

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
preference = [swagger_client.UserOption()] # list[UserOption] | 

try:
    # Save User Preferences
    api_instance.user_pref_edit(preference)
except ApiException as e:
    print("Exception when calling UserApi->user_pref_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preference** | [**list[UserOption]**](UserOption.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_pref_get**
> list[UserOption] user_pref_get(preference=preference)

Retrieve User Preferences

User preferences for non-state information, such as Layout designer zoom levels

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
preference = 'preference_example' # str | An optional preference (optional)

try:
    # Retrieve User Preferences
    api_response = api_instance.user_pref_get(preference=preference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_pref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preference** | **str**| An optional preference | [optional] 

### Return type

[**list[UserOption]**](UserOption.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search**
> list[User] user_search(user_id=user_id, user_name=user_name, user_type_id=user_type_id, retired=retired)

User Search

Search users

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | Filter by User Id (optional)
user_name = 'user_name_example' # str | Filter by User Name (optional)
user_type_id = 56 # int | Filter by UserType Id (optional)
retired = 56 # int | Filter by Retired (optional)

try:
    # User Search
    api_response = api_instance.user_search(user_id=user_id, user_name=user_name, user_type_id=user_type_id, retired=retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Filter by User Id | [optional] 
 **user_name** | **str**| Filter by User Name | [optional] 
 **user_type_id** | **int**| Filter by UserType Id | [optional] 
 **retired** | **int**| Filter by Retired | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

