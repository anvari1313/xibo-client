# swagger_client.DisplayGroupApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**display_group_action_change_layout**](DisplayGroupApi.md#display_group_action_change_layout) | **POST** /displaygroup/{displayGroupId}/action/changeLayout | Action: Change Layout
[**display_group_action_clear_stats_and_logs**](DisplayGroupApi.md#display_group_action_clear_stats_and_logs) | **POST** /displaygroup/{displayGroupId}/action/clearStatsAndLogs | Action: Clear Stats and Logs
[**display_group_action_collect_now**](DisplayGroupApi.md#display_group_action_collect_now) | **POST** /displaygroup/{displayGroupId}/action/collectNow | Action: Collect Now
[**display_group_action_command**](DisplayGroupApi.md#display_group_action_command) | **POST** /displaygroup/{displayGroupId}/action/command | Send Command
[**display_group_action_overlay_layout**](DisplayGroupApi.md#display_group_action_overlay_layout) | **POST** /displaygroup/{displayGroupId}/action/overlayLayout | Action: Overlay Layout
[**display_group_action_revert_to_schedule**](DisplayGroupApi.md#display_group_action_revert_to_schedule) | **POST** /displaygroup/{displayGroupId}/action/revertToSchedule | Action: Revert to Schedule
[**display_group_add**](DisplayGroupApi.md#display_group_add) | **POST** /displaygroup | Add a Display Group
[**display_group_delete**](DisplayGroupApi.md#display_group_delete) | **DELETE** /displaygroup/{displayGroupId} | Delete a Display Group
[**display_group_display_assign**](DisplayGroupApi.md#display_group_display_assign) | **POST** /displaygroup/{displayGroupId}/display/assign | Assign one or more Displays to a Display Group
[**display_group_display_group_assign**](DisplayGroupApi.md#display_group_display_group_assign) | **POST** /displaygroup/{displayGroupId}/displayGroup/assign | Assign one or more DisplayGroups to a Display Group
[**display_group_display_group_unassign**](DisplayGroupApi.md#display_group_display_group_unassign) | **POST** /displaygroup/{displayGroupId}/displayGroup/unassign | Unassigns one or more DisplayGroups to a Display Group
[**display_group_display_unassign**](DisplayGroupApi.md#display_group_display_unassign) | **POST** /displaygroup/{displayGroupId}/display/unassign | Unassigns one or more Displays to a Display Group
[**display_group_display_version**](DisplayGroupApi.md#display_group_display_version) | **POST** /displaygroup/{displayGroupId}/version | Set the Version for this Display
[**display_group_edit**](DisplayGroupApi.md#display_group_edit) | **PUT** /displaygroup/{displayGroupId} | Edit a Display Group
[**display_group_layout_unassign**](DisplayGroupApi.md#display_group_layout_unassign) | **POST** /displaygroup/{displayGroupId}/layout/unassign | Unassign one or more Layout items from a Display Group
[**display_group_layouts_assign**](DisplayGroupApi.md#display_group_layouts_assign) | **POST** /displaygroup/{displayGroupId}/layout/assign | Assign one or more Layouts items to a Display Group
[**display_group_media_assign**](DisplayGroupApi.md#display_group_media_assign) | **POST** /displaygroup/{displayGroupId}/media/assign | Assign one or more Media items to a Display Group
[**display_group_media_unassign**](DisplayGroupApi.md#display_group_media_unassign) | **POST** /displaygroup/{displayGroupId}/media/unassign | Unassign one or more Media items from a Display Group
[**display_group_search**](DisplayGroupApi.md#display_group_search) | **GET** /displaygroup | Get Display Groups


# **display_group_action_change_layout**
> display_group_action_change_layout(display_group_id, layout_id, change_mode, duration=duration, download_required=download_required)

Action: Change Layout

Send the change layout action to this DisplayGroup

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group Id
layout_id = 56 # int | The Layout Id
change_mode = 'change_mode_example' # str | Whether to queue or replace with this action
duration = 56 # int | The duration in seconds for this Layout change to remain in effect (optional)
download_required = 56 # int | Flag indicating whether the player should perform a collect before playing the Layout (optional)

try:
    # Action: Change Layout
    api_instance.display_group_action_change_layout(display_group_id, layout_id, change_mode, duration=duration, download_required=download_required)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_change_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group Id | 
 **layout_id** | **int**| The Layout Id | 
 **change_mode** | **str**| Whether to queue or replace with this action | 
 **duration** | **int**| The duration in seconds for this Layout change to remain in effect | [optional] 
 **download_required** | **int**| Flag indicating whether the player should perform a collect before playing the Layout | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_action_clear_stats_and_logs**
> display_group_action_clear_stats_and_logs(display_group_id)

Action: Clear Stats and Logs

Clear all stats and logs on this Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The display group id

try:
    # Action: Clear Stats and Logs
    api_instance.display_group_action_clear_stats_and_logs(display_group_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_clear_stats_and_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The display group id | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_action_collect_now**
> display_group_action_collect_now(display_group_id)

Action: Collect Now

Send the collect now action to this DisplayGroup

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The display group id

try:
    # Action: Collect Now
    api_instance.display_group_action_collect_now(display_group_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_collect_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The display group id | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_action_command**
> display_group_action_command(display_group_id, command_id)

Send Command

Send a predefined command to this Group of Displays

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The display group id
command_id = 56 # int | The Command Id

try:
    # Send Command
    api_instance.display_group_action_command(display_group_id, command_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The display group id | 
 **command_id** | **int**| The Command Id | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_action_overlay_layout**
> display_group_action_overlay_layout(display_group_id, layout_id, duration=duration, download_required=download_required)

Action: Overlay Layout

Send the overlay layout action to this DisplayGroup

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group Id
layout_id = 56 # int | The Layout Id
duration = 56 # int | The duration in seconds for this Overlay to remain in effect (optional)
download_required = 56 # int | Flag indicating whether the player should perform a collect before adding the Overlay (optional)

try:
    # Action: Overlay Layout
    api_instance.display_group_action_overlay_layout(display_group_id, layout_id, duration=duration, download_required=download_required)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_overlay_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group Id | 
 **layout_id** | **int**| The Layout Id | 
 **duration** | **int**| The duration in seconds for this Overlay to remain in effect | [optional] 
 **download_required** | **int**| Flag indicating whether the player should perform a collect before adding the Overlay | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_action_revert_to_schedule**
> display_group_action_revert_to_schedule(display_group_id)

Action: Revert to Schedule

Send the revert to schedule action to this DisplayGroup

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The display group id

try:
    # Action: Revert to Schedule
    api_instance.display_group_action_revert_to_schedule(display_group_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_action_revert_to_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The display group id | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_add**
> DisplayGroup display_group_add(display_group, is_dynamic, description=description, tags=tags, dynamic_content=dynamic_content)

Add a Display Group

Add a new Display Group to the CMS

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group = 'display_group_example' # str | The Display Group Name
is_dynamic = 56 # int | Flag indicating whether this DisplayGroup is Dynamic
description = 'description_example' # str | The Display Group Description (optional)
tags = 'tags_example' # str | A comma separated list of tags for this item (optional)
dynamic_content = 'dynamic_content_example' # str | The filter criteria for this dynamic group. A command separated set of regular expressions to apply (optional)

try:
    # Add a Display Group
    api_response = api_instance.display_group_add(display_group, is_dynamic, description=description, tags=tags, dynamic_content=dynamic_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group** | **str**| The Display Group Name | 
 **is_dynamic** | **int**| Flag indicating whether this DisplayGroup is Dynamic | 
 **description** | **str**| The Display Group Description | [optional] 
 **tags** | **str**| A comma separated list of tags for this item | [optional] 
 **dynamic_content** | **str**| The filter criteria for this dynamic group. A command separated set of regular expressions to apply | [optional] 

### Return type

[**DisplayGroup**](DisplayGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_delete**
> display_group_delete(display_group_id)

Delete a Display Group

Delete an existing Display Group identified by its Id

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The displayGroupId to delete

try:
    # Delete a Display Group
    api_instance.display_group_delete(display_group_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The displayGroupId to delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_display_assign**
> display_group_display_assign(display_group_id, display_id, unassign_display_id=unassign_display_id)

Assign one or more Displays to a Display Group

Adds the provided Displays to the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to assign to
display_id = [56] # list[int] | The Display Ids to assign
unassign_display_id = [56] # list[int] | An optional array of Display IDs to unassign (optional)

try:
    # Assign one or more Displays to a Display Group
    api_instance.display_group_display_assign(display_group_id, display_id, unassign_display_id=unassign_display_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_display_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to assign to | 
 **display_id** | [**list[int]**](int.md)| The Display Ids to assign | 
 **unassign_display_id** | [**list[int]**](int.md)| An optional array of Display IDs to unassign | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_display_group_assign**
> display_group_display_group_assign(display_group_id, display_group_id2, unassign_display_group_id=unassign_display_group_id)

Assign one or more DisplayGroups to a Display Group

Adds the provided DisplayGroups to the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to assign to
display_group_id2 = [56] # list[int] | The displayGroup Ids to assign
unassign_display_group_id = [56] # list[int] | An optional array of displayGroup IDs to unassign (optional)

try:
    # Assign one or more DisplayGroups to a Display Group
    api_instance.display_group_display_group_assign(display_group_id, display_group_id2, unassign_display_group_id=unassign_display_group_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_display_group_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to assign to | 
 **display_group_id2** | [**list[int]**](int.md)| The displayGroup Ids to assign | 
 **unassign_display_group_id** | [**list[int]**](int.md)| An optional array of displayGroup IDs to unassign | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_display_group_unassign**
> display_group_display_group_unassign(display_group_id, display_group_id2)

Unassigns one or more DisplayGroups to a Display Group

Removes the provided DisplayGroups from the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to unassign from
display_group_id2 = [56] # list[int] | The DisplayGroup Ids to unassign

try:
    # Unassigns one or more DisplayGroups to a Display Group
    api_instance.display_group_display_group_unassign(display_group_id, display_group_id2)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_display_group_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to unassign from | 
 **display_group_id2** | [**list[int]**](int.md)| The DisplayGroup Ids to unassign | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_display_unassign**
> display_group_display_unassign(display_group_id, display_id)

Unassigns one or more Displays to a Display Group

Removes the provided Displays from the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to unassign from
display_id = [56] # list[int] | The Display Ids to unassign

try:
    # Unassigns one or more Displays to a Display Group
    api_instance.display_group_display_unassign(display_group_id, display_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_display_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to unassign from | 
 **display_id** | [**list[int]**](int.md)| The Display Ids to unassign | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_display_version**
> display_group_display_version(display_group_id, media_id)

Set the Version for this Display

Sets the version instructions on all Displays in the Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group ID
media_id = 56 # int | The Media Id of the Installer File

try:
    # Set the Version for this Display
    api_instance.display_group_display_version(display_group_id, media_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_display_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group ID | 
 **media_id** | **int**| The Media Id of the Installer File | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_edit**
> DisplayGroup display_group_edit(display_group_id, display_group, is_dynamic, description=description, tags=tags, dynamic_criteria=dynamic_criteria)

Edit a Display Group

Edit an existing Display Group identified by its Id

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The displayGroupId to edit.
display_group = 'display_group_example' # str | The Display Group Name
is_dynamic = 56 # int | Flag indicating whether this DisplayGroup is Dynamic
description = 'description_example' # str | The Display Group Description (optional)
tags = 'tags_example' # str | A comma separated list of tags for this item (optional)
dynamic_criteria = 'dynamic_criteria_example' # str | The filter criteria for this dynamic group. A command separated set of regular expressions to apply (optional)

try:
    # Edit a Display Group
    api_response = api_instance.display_group_edit(display_group_id, display_group, is_dynamic, description=description, tags=tags, dynamic_criteria=dynamic_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The displayGroupId to edit. | 
 **display_group** | **str**| The Display Group Name | 
 **is_dynamic** | **int**| Flag indicating whether this DisplayGroup is Dynamic | 
 **description** | **str**| The Display Group Description | [optional] 
 **tags** | **str**| A comma separated list of tags for this item | [optional] 
 **dynamic_criteria** | **str**| The filter criteria for this dynamic group. A command separated set of regular expressions to apply | [optional] 

### Return type

[**DisplayGroup**](DisplayGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_layout_unassign**
> display_group_layout_unassign(display_group_id, layout_id)

Unassign one or more Layout items from a Display Group

Removes the provided from the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to unassign from
layout_id = [56] # list[int] | The Layout Ids to unassign

try:
    # Unassign one or more Layout items from a Display Group
    api_instance.display_group_layout_unassign(display_group_id, layout_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_layout_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to unassign from | 
 **layout_id** | [**list[int]**](int.md)| The Layout Ids to unassign | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_layouts_assign**
> display_group_layouts_assign(display_group_id, layout_id, unassign_layout_id=unassign_layout_id)

Assign one or more Layouts items to a Display Group

Adds the provided Layouts to the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to assign to
layout_id = [56] # list[int] | The Layouts Ids to assign
unassign_layout_id = [56] # list[int] | Optional array of Layouts Id to unassign (optional)

try:
    # Assign one or more Layouts items to a Display Group
    api_instance.display_group_layouts_assign(display_group_id, layout_id, unassign_layout_id=unassign_layout_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_layouts_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to assign to | 
 **layout_id** | [**list[int]**](int.md)| The Layouts Ids to assign | 
 **unassign_layout_id** | [**list[int]**](int.md)| Optional array of Layouts Id to unassign | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_media_assign**
> display_group_media_assign(display_group_id, media_id, unassign_media_id=unassign_media_id)

Assign one or more Media items to a Display Group

Adds the provided Media to the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to assign to
media_id = [56] # list[int] | The Media Ids to assign
unassign_media_id = [56] # list[int] | Optional array of Media Id to unassign (optional)

try:
    # Assign one or more Media items to a Display Group
    api_instance.display_group_media_assign(display_group_id, media_id, unassign_media_id=unassign_media_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_media_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to assign to | 
 **media_id** | [**list[int]**](int.md)| The Media Ids to assign | 
 **unassign_media_id** | [**list[int]**](int.md)| Optional array of Media Id to unassign | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_media_unassign**
> display_group_media_unassign(display_group_id, media_id)

Unassign one or more Media items from a Display Group

Removes the provided from the Display Group

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The Display Group to unassign from
media_id = [56] # list[int] | The Media Ids to unassign

try:
    # Unassign one or more Media items from a Display Group
    api_instance.display_group_media_unassign(display_group_id, media_id)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_media_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The Display Group to unassign from | 
 **media_id** | [**list[int]**](int.md)| The Media Ids to unassign | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_group_search**
> list[DisplayGroup] display_group_search(display_group_id=display_group_id, display_group=display_group, display_id=display_id, nested_display_id=nested_display_id, dynamic_criteria=dynamic_criteria, is_display_specific=is_display_specific, for_schedule=for_schedule)

Get Display Groups

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
api_instance = swagger_client.DisplayGroupApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | Filter by DisplayGroup Id (optional)
display_group = 'display_group_example' # str | Filter by DisplayGroup Name (optional)
display_id = 56 # int | Filter by DisplayGroups containing a specific display (optional)
nested_display_id = 56 # int | Filter by DisplayGroups containing a specific display in there nesting (optional)
dynamic_criteria = 'dynamic_criteria_example' # str | Filter by DisplayGroups containing a specific dynamic criteria (optional)
is_display_specific = 56 # int | Filter by whether the Display Group belongs to a Display or is user created (optional)
for_schedule = 56 # int | Should the list be refined for only those groups the User can Schedule against? (optional)

try:
    # Get Display Groups
    api_response = api_instance.display_group_search(display_group_id=display_group_id, display_group=display_group, display_id=display_id, nested_display_id=nested_display_id, dynamic_criteria=dynamic_criteria, is_display_specific=is_display_specific, for_schedule=for_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayGroupApi->display_group_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| Filter by DisplayGroup Id | [optional] 
 **display_group** | **str**| Filter by DisplayGroup Name | [optional] 
 **display_id** | **int**| Filter by DisplayGroups containing a specific display | [optional] 
 **nested_display_id** | **int**| Filter by DisplayGroups containing a specific display in there nesting | [optional] 
 **dynamic_criteria** | **str**| Filter by DisplayGroups containing a specific dynamic criteria | [optional] 
 **is_display_specific** | **int**| Filter by whether the Display Group belongs to a Display or is user created | [optional] 
 **for_schedule** | **int**| Should the list be refined for only those groups the User can Schedule against? | [optional] 

### Return type

[**list[DisplayGroup]**](DisplayGroup.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

