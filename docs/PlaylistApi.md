# swagger_client.PlaylistApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlist_library_assign**](PlaylistApi.md#playlist_library_assign) | **POST** /playlist/library/assign/{playlistId} | Assign Library Items
[**playlist_order**](PlaylistApi.md#playlist_order) | **POST** /playlist/order/{playlistId} | Order Widgets
[**playlist_search**](PlaylistApi.md#playlist_search) | **GET** /playlist/widget | Playlist Widget Search


# **playlist_library_assign**
> Playlist playlist_library_assign(playlist_id, media, duration=duration, use_duration=use_duration)

Assign Library Items

Assign Media from the Library to this Playlist

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
api_instance = swagger_client.PlaylistApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The Playlist ID to assign to
media = [56] # list[int] | Array of Media IDs to assign
duration = 56 # int | Optional duration for all Media in this assignment to use on the Widget (optional)
use_duration = 56 # int | Optional flag indicating whether to enable the useDuration field (optional)

try:
    # Assign Library Items
    api_response = api_instance.playlist_library_assign(playlist_id, media, duration=duration, use_duration=use_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistApi->playlist_library_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The Playlist ID to assign to | 
 **media** | [**list[int]**](int.md)| Array of Media IDs to assign | 
 **duration** | **int**| Optional duration for all Media in this assignment to use on the Widget | [optional] 
 **use_duration** | **int**| Optional flag indicating whether to enable the useDuration field | [optional] 

### Return type

[**Playlist**](Playlist.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_order**
> Playlist playlist_order(playlist_id, widgets)

Order Widgets

Set the order of widgets in the Playlist

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
api_instance = swagger_client.PlaylistApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The Playlist ID to Order
widgets = [swagger_client.PlaylistWidgetList()] # list[PlaylistWidgetList] | Array of widgetIds and positions - all widgetIds present in the playlist need to be passed in the call with their positions

try:
    # Order Widgets
    api_response = api_instance.playlist_order(playlist_id, widgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistApi->playlist_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The Playlist ID to Order | 
 **widgets** | [**list[PlaylistWidgetList]**](PlaylistWidgetList.md)| Array of widgetIds and positions - all widgetIds present in the playlist need to be passed in the call with their positions | 

### Return type

[**Playlist**](Playlist.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_search**
> list[Widget] playlist_search(playlist_id, widget_id=widget_id)

Playlist Widget Search

Search widgets on a Playlist

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
api_instance = swagger_client.PlaylistApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The Playlist ID to Search
widget_id = 56 # int | The widget ID to Search (optional)

try:
    # Playlist Widget Search
    api_response = api_instance.playlist_search(playlist_id, widget_id=widget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistApi->playlist_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The Playlist ID to Search | 
 **widget_id** | **int**| The widget ID to Search | [optional] 

### Return type

[**list[Widget]**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

