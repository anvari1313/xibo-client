# swagger_client.LayoutApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layout_add**](LayoutApi.md#layout_add) | **POST** /layout | Add a Layout
[**layout_copy**](LayoutApi.md#layout_copy) | **POST** /layout/copy/{layoutId} | Copy Layout
[**layout_delete**](LayoutApi.md#layout_delete) | **DELETE** /layout/{layoutId} | Delete Layout
[**layout_edit**](LayoutApi.md#layout_edit) | **PUT** /layout/{layoutId} | Edit Layout
[**layout_retire**](LayoutApi.md#layout_retire) | **PUT** /layout/retire/{layoutId} | Retire Layout
[**layout_search**](LayoutApi.md#layout_search) | **GET** /layout | Search Layouts
[**layout_status**](LayoutApi.md#layout_status) | **GET** /layout/status/{layoutId} | Layout Status
[**layout_tag**](LayoutApi.md#layout_tag) | **POST** /layout/{layoutId}/tag | Tag Layout
[**layout_untag**](LayoutApi.md#layout_untag) | **POST** /layout/{layoutId}/untag | Untag Layout
[**region_add**](LayoutApi.md#region_add) | **POST** /region/{id} | Add Region
[**region_delete**](LayoutApi.md#region_delete) | **DELETE** /region/{regionId} | Region Delete
[**region_edit**](LayoutApi.md#region_edit) | **PUT** /region/{id} | Edit Region
[**region_position_all**](LayoutApi.md#region_position_all) | **PUT** /region/position/all/{layoutId} | Position Regions


# **layout_add**
> Layout layout_add(name, description=description, layout_id=layout_id, resolution_id=resolution_id)

Add a Layout

Add a new Layout to the CMS

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The layout name
description = 'description_example' # str | The layout description (optional)
layout_id = 56 # int | If the Layout should be created with a Template, provide the ID, otherwise don't provide (optional)
resolution_id = 56 # int | If a Template is not provided, provide the resolutionId for this Layout. (optional)

try:
    # Add a Layout
    api_response = api_instance.layout_add(name, description=description, layout_id=layout_id, resolution_id=resolution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The layout name | 
 **description** | **str**| The layout description | [optional] 
 **layout_id** | **int**| If the Layout should be created with a Template, provide the ID, otherwise don&#39;t provide | [optional] 
 **resolution_id** | **int**| If a Template is not provided, provide the resolutionId for this Layout. | [optional] 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_copy**
> Layout layout_copy(layout_id, name, copy_media_files, description=description)

Copy Layout

Copy a Layout, providing a new name if applicable

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout ID to Copy
name = 'name_example' # str | The name for the new Layout
copy_media_files = 56 # int | Flag indicating whether to make new Copies of all Media Files assigned to the Layout being Copied
description = 'description_example' # str | The Description for the new Layout (optional)

try:
    # Copy Layout
    api_response = api_instance.layout_copy(layout_id, name, copy_media_files, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout ID to Copy | 
 **name** | **str**| The name for the new Layout | 
 **copy_media_files** | **int**| Flag indicating whether to make new Copies of all Media Files assigned to the Layout being Copied | 
 **description** | **str**| The Description for the new Layout | [optional] 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_delete**
> layout_delete(layout_id)

Delete Layout

Delete a Layout

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout ID to Delete

try:
    # Delete Layout
    api_instance.layout_delete(layout_id)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout ID to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_edit**
> Layout layout_edit(layout_id, name, background_color, backgroundz_index, description=description, tags=tags, retired=retired, background_image_id=background_image_id, resolution_id=resolution_id)

Edit Layout

Edit a Layout

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | 
name = 'name_example' # str | The Layout Name
background_color = 'background_color_example' # str | A HEX color to use as the background color of this Layout.
backgroundz_index = 56 # int | The Layer Number to use for the background.
description = 'description_example' # str | The Layout Description (optional)
tags = 'tags_example' # str | A comma separated list of Tags (optional)
retired = 56 # int | A flag indicating whether this Layout is retired. (optional)
background_image_id = 56 # int | A media ID to use as the background image for this Layout. (optional)
resolution_id = 56 # int | The Resolution ID to use on this Layout. (optional)

try:
    # Edit Layout
    api_response = api_instance.layout_edit(layout_id, name, background_color, backgroundz_index, description=description, tags=tags, retired=retired, background_image_id=background_image_id, resolution_id=resolution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**|  | 
 **name** | **str**| The Layout Name | 
 **background_color** | **str**| A HEX color to use as the background color of this Layout. | 
 **backgroundz_index** | **int**| The Layer Number to use for the background. | 
 **description** | **str**| The Layout Description | [optional] 
 **tags** | **str**| A comma separated list of Tags | [optional] 
 **retired** | **int**| A flag indicating whether this Layout is retired. | [optional] 
 **background_image_id** | **int**| A media ID to use as the background image for this Layout. | [optional] 
 **resolution_id** | **int**| The Resolution ID to use on this Layout. | [optional] 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_retire**
> layout_retire(layout_id)

Retire Layout

Retire a Layout so that it isn't available to Schedule. Existing Layouts will still be played

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout ID

try:
    # Retire Layout
    api_instance.layout_retire(layout_id)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_retire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_search**
> list[Layout] layout_search(layout_id=layout_id, layout=layout, user_id=user_id, retired=retired, tags=tags, exact_tags=exact_tags, owner_user_group_id=owner_user_group_id, embed=embed)

Search Layouts

Search for Layouts viewable by this user

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | Filter by Layout Id (optional)
layout = 'layout_example' # str | Filter by partial Layout name (optional)
user_id = 56 # int | Filter by user Id (optional)
retired = 56 # int | Filter by retired flag (optional)
tags = 'tags_example' # str | Filter by Tags (optional)
exact_tags = 56 # int | A flag indicating whether to treat the tags filter as an exact match (optional)
owner_user_group_id = 56 # int | Filter by users in this UserGroupId (optional)
embed = 'embed_example' # str | Embed related data such as regions, playlists, tags, etc (optional)

try:
    # Search Layouts
    api_response = api_instance.layout_search(layout_id=layout_id, layout=layout, user_id=user_id, retired=retired, tags=tags, exact_tags=exact_tags, owner_user_group_id=owner_user_group_id, embed=embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| Filter by Layout Id | [optional] 
 **layout** | **str**| Filter by partial Layout name | [optional] 
 **user_id** | **int**| Filter by user Id | [optional] 
 **retired** | **int**| Filter by retired flag | [optional] 
 **tags** | **str**| Filter by Tags | [optional] 
 **exact_tags** | **int**| A flag indicating whether to treat the tags filter as an exact match | [optional] 
 **owner_user_group_id** | **int**| Filter by users in this UserGroupId | [optional] 
 **embed** | **str**| Embed related data such as regions, playlists, tags, etc | [optional] 

### Return type

[**list[Layout]**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_status**
> Layout layout_status(layout_id)

Layout Status

Calculate the Layout status and return a Layout

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout Id to get the status

try:
    # Layout Status
    api_response = api_instance.layout_status(layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout Id to get the status | 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_tag**
> Layout layout_tag(layout_id, tag)

Tag Layout

Tag a Layout with one or more tags

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout Id to Tag
tag = ['tag_example'] # list[str] | An array of tags

try:
    # Tag Layout
    api_response = api_instance.layout_tag(layout_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout Id to Tag | 
 **tag** | [**list[str]**](str.md)| An array of tags | 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layout_untag**
> Layout layout_untag(layout_id, tag)

Untag Layout

Untag a Layout with one or more tags

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout Id to Untag
tag = ['tag_example'] # list[str] | An array of tags

try:
    # Untag Layout
    api_response = api_instance.layout_untag(layout_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->layout_untag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout Id to Untag | 
 **tag** | [**list[str]**](str.md)| An array of tags | 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_add**
> Region region_add(id, width=width, height=height, top=top, left=left)

Add Region

Add a Region to a Layout

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Layout ID to add the Region to
width = 56 # int | The Width, default 250 (optional)
height = 56 # int | The Height (optional)
top = 56 # int | The Top Coordinate (optional)
left = 56 # int | The Left Coordinate (optional)

try:
    # Add Region
    api_response = api_instance.region_add(id, width=width, height=height, top=top, left=left)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->region_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Layout ID to add the Region to | 
 **width** | **int**| The Width, default 250 | [optional] 
 **height** | **int**| The Height | [optional] 
 **top** | **int**| The Top Coordinate | [optional] 
 **left** | **int**| The Left Coordinate | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_delete**
> region_delete(region_id)

Region Delete

Delete an existing region

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
region_id = 56 # int | The Region ID to Delete

try:
    # Region Delete
    api_instance.region_delete(region_id)
except ApiException as e:
    print("Exception when calling LayoutApi->region_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **int**| The Region ID to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_edit**
> Region region_edit(id, loop, width=width, height=height, top=top, left=left, z_index=z_index, transition_type=transition_type, transition_duration=transition_duration, transition_direction=transition_direction)

Edit Region

Edit Region

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Region ID to Edit
loop = 56 # int | Flag indicating whether this region should loop if there is only 1 media item in the timeline
width = 56 # int | The Width, default 250 (optional)
height = 56 # int | The Height (optional)
top = 56 # int | The Top Coordinate (optional)
left = 56 # int | The Left Coordinate (optional)
z_index = 56 # int | The Layer for this Region (optional)
transition_type = 'transition_type_example' # str | The Transition Type. Must be a valid transition code as returned by /transition (optional)
transition_duration = 56 # int | The transition duration in milliseconds if required by the transition type (optional)
transition_direction = 'transition_direction_example' # str | The transition direction if required by the transition type. (optional)

try:
    # Edit Region
    api_response = api_instance.region_edit(id, loop, width=width, height=height, top=top, left=left, z_index=z_index, transition_type=transition_type, transition_duration=transition_duration, transition_direction=transition_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->region_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Region ID to Edit | 
 **loop** | **int**| Flag indicating whether this region should loop if there is only 1 media item in the timeline | 
 **width** | **int**| The Width, default 250 | [optional] 
 **height** | **int**| The Height | [optional] 
 **top** | **int**| The Top Coordinate | [optional] 
 **left** | **int**| The Left Coordinate | [optional] 
 **z_index** | **int**| The Layer for this Region | [optional] 
 **transition_type** | **str**| The Transition Type. Must be a valid transition code as returned by /transition | [optional] 
 **transition_duration** | **int**| The transition duration in milliseconds if required by the transition type | [optional] 
 **transition_direction** | **str**| The transition direction if required by the transition type. | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_position_all**
> Layout region_position_all(layout_id, regions)

Position Regions

Position all regions for a Layout

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
api_instance = swagger_client.LayoutApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout ID
regions = ['regions_example'] # list[str] | Array of regions and their new positions. Each array element should be json encoded and have regionId, top, left, width and height.

try:
    # Position Regions
    api_response = api_instance.region_position_all(layout_id, regions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayoutApi->region_position_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout ID | 
 **regions** | [**list[str]**](str.md)| Array of regions and their new positions. Each array element should be json encoded and have regionId, top, left, width and height. | 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

