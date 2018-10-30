# swagger_client.DisplayApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**display_default_layout**](DisplayApi.md#display_default_layout) | **PUT** /display/defaultlayout/{displayId} | Set Default Layout
[**display_delete**](DisplayApi.md#display_delete) | **DELETE** /display/{displayId} | Display Delete
[**display_edit**](DisplayApi.md#display_edit) | **PUT** /display/{displayId} | Display Edit
[**display_request_screenshot**](DisplayApi.md#display_request_screenshot) | **PUT** /display/requestscreenshot/{displayId} | Request Screen Shot
[**display_search**](DisplayApi.md#display_search) | **GET** /display | Display Search
[**display_toggle_authorise**](DisplayApi.md#display_toggle_authorise) | **PUT** /display/authorise/{displayId} | Toggle authorised
[**display_wake_on_lan**](DisplayApi.md#display_wake_on_lan) | **POST** /display/wol/{displayId} | Issue WOL


# **display_default_layout**
> display_default_layout(display_id, layout_id)

Set Default Layout

Set the default Layout on this Display

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID
layout_id = 56 # int | The Layout ID

try:
    # Set Default Layout
    api_instance.display_default_layout(display_id, layout_id)
except ApiException as e:
    print("Exception when calling DisplayApi->display_default_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 
 **layout_id** | **int**| The Layout ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_delete**
> display_delete(display_id)

Display Delete

Delete a Display

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID

try:
    # Display Delete
    api_instance.display_delete(display_id)
except ApiException as e:
    print("Exception when calling DisplayApi->display_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_edit**
> Display display_edit(display_id, display, default_layout_id, licensed, license, inc_schedule, email_alert, wake_on_lan_enabled, description=description, tags=tags, auditing_until=auditing_until, alert_timeout=alert_timeout, wake_on_lan_time=wake_on_lan_time, broad_cast_address=broad_cast_address, secure_on=secure_on, cidr=cidr, latitude=latitude, longitude=longitude, time_zone=time_zone, display_profile_id=display_profile_id, clear_cached_data=clear_cached_data, rekey_xmr=rekey_xmr)

Display Edit

Edit a Display

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID
display = 'display_example' # str | The Display Name
default_layout_id = 56 # int | A Layout ID representing the Default Layout for this Display.
licensed = 56 # int | Flag indicating whether this display is licensed.
license = 'license_example' # str | The hardwareKey to use as the licence key for this Display
inc_schedule = 56 # int | Flag indicating whether the Default Layout should be included in the Schedule
email_alert = 56 # int | Flag indicating whether the Display generates up/down email alerts.
wake_on_lan_enabled = 56 # int | Flag indicating if Wake On LAN is enabled for this Display
description = 'description_example' # str | A description of the Display (optional)
tags = 'tags_example' # str | A comma separated list of tags for this item (optional)
auditing_until = '2013-10-20T19:20:30+01:00' # datetime | A date this Display records auditing information until. (optional)
alert_timeout = 56 # int | How long in seconds should this display wait before alerting when it hasn't connected. Override for the collection interval. (optional)
wake_on_lan_time = 'wake_on_lan_time_example' # str | A h:i string representing the time that the Display should receive its Wake on LAN command (optional)
broad_cast_address = 'broad_cast_address_example' # str | The BroadCast Address for this Display - used by Wake On LAN (optional)
secure_on = 'secure_on_example' # str | The secure on configuration for this Display (optional)
cidr = 56 # int | The CIDR configuration for this Display (optional)
latitude = 8.14 # float | The Latitude of this Display (optional)
longitude = 8.14 # float | The Longitude of this Display (optional)
time_zone = 'time_zone_example' # str | The timezone for this display, or empty to use the CMS timezone (optional)
display_profile_id = 56 # int | The Display Settings Profile ID (optional)
clear_cached_data = 56 # int | Clear all Cached data for this display (optional)
rekey_xmr = 56 # int | Clear the cached XMR configuration and send a rekey (optional)

try:
    # Display Edit
    api_response = api_instance.display_edit(display_id, display, default_layout_id, licensed, license, inc_schedule, email_alert, wake_on_lan_enabled, description=description, tags=tags, auditing_until=auditing_until, alert_timeout=alert_timeout, wake_on_lan_time=wake_on_lan_time, broad_cast_address=broad_cast_address, secure_on=secure_on, cidr=cidr, latitude=latitude, longitude=longitude, time_zone=time_zone, display_profile_id=display_profile_id, clear_cached_data=clear_cached_data, rekey_xmr=rekey_xmr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 
 **display** | **str**| The Display Name | 
 **default_layout_id** | **int**| A Layout ID representing the Default Layout for this Display. | 
 **licensed** | **int**| Flag indicating whether this display is licensed. | 
 **license** | **str**| The hardwareKey to use as the licence key for this Display | 
 **inc_schedule** | **int**| Flag indicating whether the Default Layout should be included in the Schedule | 
 **email_alert** | **int**| Flag indicating whether the Display generates up/down email alerts. | 
 **wake_on_lan_enabled** | **int**| Flag indicating if Wake On LAN is enabled for this Display | 
 **description** | **str**| A description of the Display | [optional] 
 **tags** | **str**| A comma separated list of tags for this item | [optional] 
 **auditing_until** | **datetime**| A date this Display records auditing information until. | [optional] 
 **alert_timeout** | **int**| How long in seconds should this display wait before alerting when it hasn&#39;t connected. Override for the collection interval. | [optional] 
 **wake_on_lan_time** | **str**| A h:i string representing the time that the Display should receive its Wake on LAN command | [optional] 
 **broad_cast_address** | **str**| The BroadCast Address for this Display - used by Wake On LAN | [optional] 
 **secure_on** | **str**| The secure on configuration for this Display | [optional] 
 **cidr** | **int**| The CIDR configuration for this Display | [optional] 
 **latitude** | **float**| The Latitude of this Display | [optional] 
 **longitude** | **float**| The Longitude of this Display | [optional] 
 **time_zone** | **str**| The timezone for this display, or empty to use the CMS timezone | [optional] 
 **display_profile_id** | **int**| The Display Settings Profile ID | [optional] 
 **clear_cached_data** | **int**| Clear all Cached data for this display | [optional] 
 **rekey_xmr** | **int**| Clear the cached XMR configuration and send a rekey | [optional] 

### Return type

[**Display**](Display.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_request_screenshot**
> Display display_request_screenshot(display_id)

Request Screen Shot

Notify the display that the CMS would like a screen shot to be sent.

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID

try:
    # Request Screen Shot
    api_response = api_instance.display_request_screenshot(display_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_request_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 

### Return type

[**Display**](Display.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_search**
> list[Display] display_search(display_id=display_id, display_group_id=display_group_id, display=display, mac_address=mac_address, hardware_key=hardware_key, client_version=client_version, embed=embed, authorised=authorised, display_profile_id=display_profile_id)

Display Search

Search Displays for this User

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | Filter by Display Id (optional)
display_group_id = 56 # int | Filter by DisplayGroup Id (optional)
display = 'display_example' # str | Filter by Display Name (optional)
mac_address = 'mac_address_example' # str | Filter by Mac Address (optional)
hardware_key = 'hardware_key_example' # str | Filter by Hardware Key (optional)
client_version = 'client_version_example' # str | Filter by Client Version (optional)
embed = 'embed_example' # str | Embed related data, namely displaygroups. A comma separated list of child objects to embed. (optional)
authorised = 56 # int | Filter by authorised flag (optional)
display_profile_id = 56 # int | Filter by Display Profile (optional)

try:
    # Display Search
    api_response = api_instance.display_search(display_id=display_id, display_group_id=display_group_id, display=display, mac_address=mac_address, hardware_key=hardware_key, client_version=client_version, embed=embed, authorised=authorised, display_profile_id=display_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| Filter by Display Id | [optional] 
 **display_group_id** | **int**| Filter by DisplayGroup Id | [optional] 
 **display** | **str**| Filter by Display Name | [optional] 
 **mac_address** | **str**| Filter by Mac Address | [optional] 
 **hardware_key** | **str**| Filter by Hardware Key | [optional] 
 **client_version** | **str**| Filter by Client Version | [optional] 
 **embed** | **str**| Embed related data, namely displaygroups. A comma separated list of child objects to embed. | [optional] 
 **authorised** | **int**| Filter by authorised flag | [optional] 
 **display_profile_id** | **int**| Filter by Display Profile | [optional] 

### Return type

[**list[Display]**](Display.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_toggle_authorise**
> display_toggle_authorise(display_id)

Toggle authorised

Toggle authorised for the Display.

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID

try:
    # Toggle authorised
    api_instance.display_toggle_authorise(display_id)
except ApiException as e:
    print("Exception when calling DisplayApi->display_toggle_authorise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_wake_on_lan**
> display_wake_on_lan(display_id)

Issue WOL

Send a Wake On LAN packet to this Display

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
api_instance = swagger_client.DisplayApi(swagger_client.ApiClient(configuration))
display_id = 56 # int | The Display ID

try:
    # Issue WOL
    api_instance.display_wake_on_lan(display_id)
except ApiException as e:
    print("Exception when calling DisplayApi->display_wake_on_lan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_id** | **int**| The Display ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

