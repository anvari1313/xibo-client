# swagger_client.NotificationApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_add**](NotificationApi.md#notification_add) | **POST** /notification | Notification Add
[**notification_delete**](NotificationApi.md#notification_delete) | **DELETE** /notification/{notificationId} | Delete Notification
[**notification_edit**](NotificationApi.md#notification_edit) | **PUT** /notification/{notificationId} | Notification Edit
[**notification_search**](NotificationApi.md#notification_search) | **GET** /notification | Notification Search


# **notification_add**
> Notification notification_add(subject, is_email, is_interrupt, display_group_ids, user_group_ids, body=body, release_dt=release_dt)

Notification Add

Add a Notification

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
subject = 'subject_example' # str | The Subject
is_email = 56 # int | Flag indicating whether this notification should be emailed.
is_interrupt = 56 # int | Flag indication whether this notification should interrupt the web portal nativation/login
display_group_ids = [56] # list[int] | The display group ids to assign this notification to
user_group_ids = [56] # list[int] | The user group ids to assign to this notification
body = 'body_example' # str | The Body (optional)
release_dt = 'release_dt_example' # str | ISO date representing the release date for this notification (optional)

try:
    # Notification Add
    api_response = api_instance.notification_add(subject, is_email, is_interrupt, display_group_ids, user_group_ids, body=body, release_dt=release_dt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| The Subject | 
 **is_email** | **int**| Flag indicating whether this notification should be emailed. | 
 **is_interrupt** | **int**| Flag indication whether this notification should interrupt the web portal nativation/login | 
 **display_group_ids** | [**list[int]**](int.md)| The display group ids to assign this notification to | 
 **user_group_ids** | [**list[int]**](int.md)| The user group ids to assign to this notification | 
 **body** | **str**| The Body | [optional] 
 **release_dt** | **str**| ISO date representing the release date for this notification | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_delete**
> notification_delete(notification_id)

Delete Notification

Delete the provided notification

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_id = 56 # int | The Notification Id to Delete

try:
    # Delete Notification
    api_instance.notification_delete(notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| The Notification Id to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_edit**
> Notification notification_edit(notification_id, subject, release_dt, is_email, is_interrupt, display_group_ids, user_group_ids, body=body)

Notification Edit

Edit a Notification

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_id = 56 # int | The NotificationId
subject = 'subject_example' # str | The Subject
release_dt = 'release_dt_example' # str | ISO date representing the release date for this notification
is_email = 56 # int | Flag indicating whether this notification should be emailed.
is_interrupt = 56 # int | Flag indication whether this notification should interrupt the web portal nativation/login
display_group_ids = [56] # list[int] | The display group ids to assign this notification to
user_group_ids = [56] # list[int] | The user group ids to assign to this notification
body = 'body_example' # str | The Body (optional)

try:
    # Notification Edit
    api_response = api_instance.notification_edit(notification_id, subject, release_dt, is_email, is_interrupt, display_group_ids, user_group_ids, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| The NotificationId | 
 **subject** | **str**| The Subject | 
 **release_dt** | **str**| ISO date representing the release date for this notification | 
 **is_email** | **int**| Flag indicating whether this notification should be emailed. | 
 **is_interrupt** | **int**| Flag indication whether this notification should interrupt the web portal nativation/login | 
 **display_group_ids** | [**list[int]**](int.md)| The display group ids to assign this notification to | 
 **user_group_ids** | [**list[int]**](int.md)| The user group ids to assign to this notification | 
 **body** | **str**| The Body | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_search**
> list[Notification] notification_search(notification_id=notification_id, subject=subject)

Notification Search

Search this users Notifications

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_id = 56 # int | Filter by Notification Id (optional)
subject = 'subject_example' # str | Filter by Subject (optional)

try:
    # Notification Search
    api_response = api_instance.notification_search(notification_id=notification_id, subject=subject)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| Filter by Notification Id | [optional] 
 **subject** | **str**| Filter by Subject | [optional] 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

