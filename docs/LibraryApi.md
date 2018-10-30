# swagger_client.LibraryApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**library_add**](LibraryApi.md#library_add) | **POST** /library | Add Media
[**library_delete**](LibraryApi.md#library_delete) | **DELETE** /library/{mediaId} | Delete Media
[**library_download**](LibraryApi.md#library_download) | **GET** /library/download/{mediaId}/{type} | Download Media
[**library_edit**](LibraryApi.md#library_edit) | **PUT** /library/{mediaId} | Edit Media
[**library_search**](LibraryApi.md#library_search) | **GET** /library | Library Search
[**library_tidy**](LibraryApi.md#library_tidy) | **DELETE** /library/tidy | Tidy Library
[**library_usage_layouts_report**](LibraryApi.md#library_usage_layouts_report) | **GET** /library/usage/layouts/{mediaId} | Get Library Item Usage Report for Layouts
[**library_usage_report**](LibraryApi.md#library_usage_report) | **GET** /library/usage/{mediaId} | Get Library Item Usage Report
[**media_tag**](LibraryApi.md#media_tag) | **POST** /library/{mediaId}/tag | Tag Media
[**media_untag**](LibraryApi.md#media_untag) | **POST** /library/{mediaId}/untag | Untag Media


# **library_add**
> library_add(files, name=name, old_media_id=old_media_id, update_in_layouts=update_in_layouts, delete_old_revisions=delete_old_revisions)

Add Media

Add Media to the Library

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
files = '/path/to/file.txt' # file | The Uploaded File
name = 'name_example' # str | Optional Media Name (optional)
old_media_id = 56 # int | Id of an existing media file which should be replaced with the new upload (optional)
update_in_layouts = 56 # int | Flag (0, 1), set to 1 to update this media in all layouts (use with oldMediaId)  (optional)
delete_old_revisions = 56 # int | Flag (0 , 1), to either remove or leave the old file revisions (use with oldMediaId) (optional)

try:
    # Add Media
    api_instance.library_add(files, name=name, old_media_id=old_media_id, update_in_layouts=update_in_layouts, delete_old_revisions=delete_old_revisions)
except ApiException as e:
    print("Exception when calling LibraryApi->library_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **file**| The Uploaded File | 
 **name** | **str**| Optional Media Name | [optional] 
 **old_media_id** | **int**| Id of an existing media file which should be replaced with the new upload | [optional] 
 **update_in_layouts** | **int**| Flag (0, 1), set to 1 to update this media in all layouts (use with oldMediaId)  | [optional] 
 **delete_old_revisions** | **int**| Flag (0 , 1), to either remove or leave the old file revisions (use with oldMediaId) | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_delete**
> library_delete(media_id, force_delete)

Delete Media

Delete Media from the Library

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | The Media ID to Delete
force_delete = 56 # int | If the media item has been used should it be force removed from items that uses it?

try:
    # Delete Media
    api_instance.library_delete(media_id, force_delete)
except ApiException as e:
    print("Exception when calling LibraryApi->library_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| The Media ID to Delete | 
 **force_delete** | **int**| If the media item has been used should it be force removed from items that uses it? | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_download**
> file library_download(media_id, type)

Download Media

Download a Media file from the Library

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | The Media ID to Download
type = 'type_example' # str | The Module Type of the Download

try:
    # Download Media
    api_response = api_instance.library_download(media_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->library_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| The Media ID to Download | 
 **type** | **str**| The Module Type of the Download | 

### Return type

[**file**](file.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_edit**
> Media library_edit(media_id, name, duration, retired, tags=tags, update_in_layouts=update_in_layouts)

Edit Media

Edit a Media Item in the Library

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | The Media ID to Edit
name = 'name_example' # str | Media Item Name
duration = 56 # int | The duration in seconds for this Media Item
retired = 56 # int | Flag indicating if this media is retired
tags = 'tags_example' # str | Comma separated list of Tags (optional)
update_in_layouts = 56 # int | Flag indicating whether to update the duration in all Layouts the Media is assigned to (optional)

try:
    # Edit Media
    api_response = api_instance.library_edit(media_id, name, duration, retired, tags=tags, update_in_layouts=update_in_layouts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->library_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| The Media ID to Edit | 
 **name** | **str**| Media Item Name | 
 **duration** | **int**| The duration in seconds for this Media Item | 
 **retired** | **int**| Flag indicating if this media is retired | 
 **tags** | **str**| Comma separated list of Tags | [optional] 
 **update_in_layouts** | **int**| Flag indicating whether to update the duration in all Layouts the Media is assigned to | [optional] 

### Return type

[**Media**](Media.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_search**
> list[Media] library_search(media_id=media_id, media=media, type=type, owner_id=owner_id, retired=retired, tags=tags, exact_tags=exact_tags, duration=duration, file_size=file_size, owner_user_group_id=owner_user_group_id)

Library Search

Search the Library for this user

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | Filter by Media Id (optional)
media = 'media_example' # str | Filter by Media Name (optional)
type = 'type_example' # str | Filter by Media Type (optional)
owner_id = 56 # int | Filter by Owner Id (optional)
retired = 56 # int | Filter by Retired (optional)
tags = 'tags_example' # str | Filter by Tags - comma seperated (optional)
exact_tags = 56 # int | A flag indicating whether to treat the tags filter as an exact match (optional)
duration = 'duration_example' # str | Filter by Duration - a number or less-than,greater-than,less-than-equal or great-than-equal followed by a | followed by a number (optional)
file_size = 'file_size_example' # str | Filter by File Size - a number or less-than,greater-than,less-than-equal or great-than-equal followed by a | followed by a number (optional)
owner_user_group_id = 56 # int | Filter by users in this UserGroupId (optional)

try:
    # Library Search
    api_response = api_instance.library_search(media_id=media_id, media=media, type=type, owner_id=owner_id, retired=retired, tags=tags, exact_tags=exact_tags, duration=duration, file_size=file_size, owner_user_group_id=owner_user_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->library_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| Filter by Media Id | [optional] 
 **media** | **str**| Filter by Media Name | [optional] 
 **type** | **str**| Filter by Media Type | [optional] 
 **owner_id** | **int**| Filter by Owner Id | [optional] 
 **retired** | **int**| Filter by Retired | [optional] 
 **tags** | **str**| Filter by Tags - comma seperated | [optional] 
 **exact_tags** | **int**| A flag indicating whether to treat the tags filter as an exact match | [optional] 
 **duration** | **str**| Filter by Duration - a number or less-than,greater-than,less-than-equal or great-than-equal followed by a | followed by a number | [optional] 
 **file_size** | **str**| Filter by File Size - a number or less-than,greater-than,less-than-equal or great-than-equal followed by a | followed by a number | [optional] 
 **owner_user_group_id** | **int**| Filter by users in this UserGroupId | [optional] 

### Return type

[**list[Media]**](Media.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_tidy**
> library_tidy(tidy_generic_files=tidy_generic_files)

Tidy Library

Routine tidy of the library, removing unused files.

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
tidy_generic_files = 56 # int | Also delete generic files? (optional)

try:
    # Tidy Library
    api_instance.library_tidy(tidy_generic_files=tidy_generic_files)
except ApiException as e:
    print("Exception when calling LibraryApi->library_tidy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tidy_generic_files** | **int**| Also delete generic files? | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_usage_layouts_report**
> library_usage_layouts_report()

Get Library Item Usage Report for Layouts

Get the records for the library item usage report for Layouts

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))

try:
    # Get Library Item Usage Report for Layouts
    api_instance.library_usage_layouts_report()
except ApiException as e:
    print("Exception when calling LibraryApi->library_usage_layouts_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_usage_report**
> library_usage_report()

Get Library Item Usage Report

Get the records for the library item usage report

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))

try:
    # Get Library Item Usage Report
    api_instance.library_usage_report()
except ApiException as e:
    print("Exception when calling LibraryApi->library_usage_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_tag**
> Media media_tag(media_id, tag)

Tag Media

Tag a Media with one or more tags

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | The Media Id to Tag
tag = ['tag_example'] # list[str] | An array of tags

try:
    # Tag Media
    api_response = api_instance.media_tag(media_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->media_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| The Media Id to Tag | 
 **tag** | [**list[str]**](str.md)| An array of tags | 

### Return type

[**Media**](Media.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_untag**
> Media media_untag(media_id, tag)

Untag Media

Untag a Media with one or more tags

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
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
media_id = 56 # int | The Media Id to Untag
tag = ['tag_example'] # list[str] | An array of tags

try:
    # Untag Media
    api_response = api_instance.media_untag(media_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->media_untag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| The Media Id to Untag | 
 **tag** | [**list[str]**](str.md)| An array of tags | 

### Return type

[**Media**](Media.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

