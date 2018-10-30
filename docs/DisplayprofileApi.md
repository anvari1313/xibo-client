# swagger_client.DisplayprofileApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**display_profile_add**](DisplayprofileApi.md#display_profile_add) | **POST** /displayprofile | Add Display Profile
[**display_profile_delete**](DisplayprofileApi.md#display_profile_delete) | **DELETE** /displayprofile/{displayProfileId} | Delete Display Profile
[**display_profile_edit**](DisplayprofileApi.md#display_profile_edit) | **PUT** /displayprofile/{displayProfileId} | Edit Display Profile
[**display_profile_search**](DisplayprofileApi.md#display_profile_search) | **GET** /displayprofile | Display Profile Search


# **display_profile_add**
> DisplayProfile display_profile_add(name, type, is_default)

Add Display Profile

Add a Display Profile

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
api_instance = swagger_client.DisplayprofileApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The Name of the Display Profile
type = 'type_example' # str | The Client Type this Profile will apply to
is_default = 56 # int | Flag indicating if this is the default profile for the client type

try:
    # Add Display Profile
    api_response = api_instance.display_profile_add(name, type, is_default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayprofileApi->display_profile_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The Name of the Display Profile | 
 **type** | **str**| The Client Type this Profile will apply to | 
 **is_default** | **int**| Flag indicating if this is the default profile for the client type | 

### Return type

[**DisplayProfile**](DisplayProfile.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_profile_delete**
> display_profile_delete(display_profile_id)

Delete Display Profile

Delete an existing Display Profile

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
api_instance = swagger_client.DisplayprofileApi(swagger_client.ApiClient(configuration))
display_profile_id = 56 # int | The Display Profile ID

try:
    # Delete Display Profile
    api_instance.display_profile_delete(display_profile_id)
except ApiException as e:
    print("Exception when calling DisplayprofileApi->display_profile_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_profile_id** | **int**| The Display Profile ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_profile_edit**
> DisplayProfile display_profile_edit(display_profile_id, name, type, is_default)

Edit Display Profile

Edit a Display Profile

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
api_instance = swagger_client.DisplayprofileApi(swagger_client.ApiClient(configuration))
display_profile_id = 56 # int | The Display Profile ID
name = 'name_example' # str | The Name of the Display Profile
type = 'type_example' # str | The Client Type this Profile will apply to
is_default = 56 # int | Flag indicating if this is the default profile for the client type

try:
    # Edit Display Profile
    api_response = api_instance.display_profile_edit(display_profile_id, name, type, is_default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayprofileApi->display_profile_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_profile_id** | **int**| The Display Profile ID | 
 **name** | **str**| The Name of the Display Profile | 
 **type** | **str**| The Client Type this Profile will apply to | 
 **is_default** | **int**| Flag indicating if this is the default profile for the client type | 

### Return type

[**DisplayProfile**](DisplayProfile.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_profile_search**
> list[DisplayProfile] display_profile_search(display_profile_id=display_profile_id, display_profile=display_profile, type=type)

Display Profile Search

Search this users Display Profiles

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
api_instance = swagger_client.DisplayprofileApi(swagger_client.ApiClient(configuration))
display_profile_id = 56 # int | Filter by DisplayProfile Id (optional)
display_profile = 'display_profile_example' # str | Filter by DisplayProfile Name (optional)
type = 'type_example' # str | Filter by DisplayProfile Type (windows|android) (optional)

try:
    # Display Profile Search
    api_response = api_instance.display_profile_search(display_profile_id=display_profile_id, display_profile=display_profile, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayprofileApi->display_profile_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_profile_id** | **int**| Filter by DisplayProfile Id | [optional] 
 **display_profile** | **str**| Filter by DisplayProfile Name | [optional] 
 **type** | **str**| Filter by DisplayProfile Type (windows|android) | [optional] 

### Return type

[**list[DisplayProfile]**](DisplayProfile.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

