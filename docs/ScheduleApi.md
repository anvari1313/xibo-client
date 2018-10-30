# swagger_client.ScheduleApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_add**](ScheduleApi.md#schedule_add) | **POST** /schedule | Add Schedule Event
[**schedule_calendar_data**](ScheduleApi.md#schedule_calendar_data) | **GET** /schedule/data/events | Generates the calendar that we draw events on
[**schedule_calendar_data_0**](ScheduleApi.md#schedule_calendar_data_0) | **GET** /schedule/{displayGroupId}/events | Event List
[**schedule_delete**](ScheduleApi.md#schedule_delete) | **DELETE** /schedule/{eventId} | Delete Event
[**schedule_edit**](ScheduleApi.md#schedule_edit) | **PUT** /schedule/{eventId} | Edit Schedule Event


# **schedule_add**
> Schedule schedule_add(event_type_id, display_order, is_priority, display_group_ids, from_dt, campaign_id=campaign_id, command_id=command_id, day_part_id=day_part_id, sync_timezone=sync_timezone, to_dt=to_dt, recurrence_type=recurrence_type, recurrence_detail=recurrence_detail, recurrence_range=recurrence_range, recurrence_repeats_on=recurrence_repeats_on)

Add Schedule Event

Add a new scheduled event for a Campaign/Layout to be shown on a Display Group/Display.

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
event_type_id = 56 # int | The Event Type Id to use for this Event. 1=Campaign, 2=Command, 3=Overlay
display_order = 56 # int | The display order for this event. 
is_priority = 56 # int | An integer indicating the priority of this event. Normal events have a priority of 0.
display_group_ids = [56] # list[int] | The Display Group IDs for this event. Display specific Group IDs should be used to schedule on single displays.
from_dt = '2013-10-20T19:20:30+01:00' # datetime | The from date for this event.
campaign_id = 56 # int | The Campaign ID to use for this Event. If a Layout is needed then the Campaign specific ID for that Layout should be used. (optional)
command_id = 56 # int | The Command ID to use for this Event. (optional)
day_part_id = 56 # int | The Day Part for this event. Overrides supported are 0(custom) and 1(always). Defaulted to 0. (optional)
sync_timezone = 56 # int | Should this schedule be synced to the resulting Display timezone? (optional)
to_dt = '2013-10-20T19:20:30+01:00' # datetime | The to date for this event. (optional)
recurrence_type = 'recurrence_type_example' # str | The type of recurrence to apply to this event. (optional)
recurrence_detail = 56 # int | The interval for the recurrence. (optional)
recurrence_range = '2013-10-20T19:20:30+01:00' # datetime | The end date for this events recurrence. (optional)
recurrence_repeats_on = 'recurrence_repeats_on_example' # str | The days of the week that this event repeats - weekly only (optional)

try:
    # Add Schedule Event
    api_response = api_instance.schedule_add(event_type_id, display_order, is_priority, display_group_ids, from_dt, campaign_id=campaign_id, command_id=command_id, day_part_id=day_part_id, sync_timezone=sync_timezone, to_dt=to_dt, recurrence_type=recurrence_type, recurrence_detail=recurrence_detail, recurrence_range=recurrence_range, recurrence_repeats_on=recurrence_repeats_on)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **int**| The Event Type Id to use for this Event. 1&#x3D;Campaign, 2&#x3D;Command, 3&#x3D;Overlay | 
 **display_order** | **int**| The display order for this event.  | 
 **is_priority** | **int**| An integer indicating the priority of this event. Normal events have a priority of 0. | 
 **display_group_ids** | [**list[int]**](int.md)| The Display Group IDs for this event. Display specific Group IDs should be used to schedule on single displays. | 
 **from_dt** | **datetime**| The from date for this event. | 
 **campaign_id** | **int**| The Campaign ID to use for this Event. If a Layout is needed then the Campaign specific ID for that Layout should be used. | [optional] 
 **command_id** | **int**| The Command ID to use for this Event. | [optional] 
 **day_part_id** | **int**| The Day Part for this event. Overrides supported are 0(custom) and 1(always). Defaulted to 0. | [optional] 
 **sync_timezone** | **int**| Should this schedule be synced to the resulting Display timezone? | [optional] 
 **to_dt** | **datetime**| The to date for this event. | [optional] 
 **recurrence_type** | **str**| The type of recurrence to apply to this event. | [optional] 
 **recurrence_detail** | **int**| The interval for the recurrence. | [optional] 
 **recurrence_range** | **datetime**| The end date for this events recurrence. | [optional] 
 **recurrence_repeats_on** | **str**| The days of the week that this event repeats - weekly only | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_calendar_data**
> list[ScheduleCalendarData] schedule_calendar_data(_from, to, display_group_ids=display_group_ids)

Generates the calendar that we draw events on

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
_from = 56 # int | From Date Timestamp in Microseconds
to = 56 # int | To Date Timestamp in Microseconds
display_group_ids = [56] # list[int] | The DisplayGroupIds to return the schedule for. Empty for All. (optional)

try:
    # Generates the calendar that we draw events on
    api_response = api_instance.schedule_calendar_data(_from, to, display_group_ids=display_group_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule_calendar_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| From Date Timestamp in Microseconds | 
 **to** | **int**| To Date Timestamp in Microseconds | 
 **display_group_ids** | [**list[int]**](int.md)| The DisplayGroupIds to return the schedule for. Empty for All. | [optional] 

### Return type

[**list[ScheduleCalendarData]**](ScheduleCalendarData.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_calendar_data_0**
> schedule_calendar_data_0(display_group_id, date)

Event List

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
display_group_id = 56 # int | The DisplayGroupId to return the event list for.
date = 'date_example' # str | Date in Y-m-d H:i:s

try:
    # Event List
    api_instance.schedule_calendar_data_0(display_group_id, date)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule_calendar_data_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_group_id** | **int**| The DisplayGroupId to return the event list for. | 
 **date** | **str**| Date in Y-m-d H:i:s | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_delete**
> schedule_delete(event_id)

Delete Event

Delete a Scheduled Event

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
event_id = 56 # int | The Scheduled Event ID

try:
    # Delete Event
    api_instance.schedule_delete(event_id)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The Scheduled Event ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_edit**
> Schedule schedule_edit(event_id, event_type_id, display_order, is_priority, display_group_ids, from_dt, campaign_id=campaign_id, command_id=command_id, day_part_id=day_part_id, sync_timezone=sync_timezone, to_dt=to_dt, recurrence_type=recurrence_type, recurrence_detail=recurrence_detail, recurrence_range=recurrence_range, recurrence_repeats_on=recurrence_repeats_on)

Edit Schedule Event

Edit a scheduled event for a Campaign/Layout to be shown on a Display Group/Display.

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
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
event_id = 56 # int | The Scheduled Event ID
event_type_id = 56 # int | The Event Type Id to use for this Event. 1=Campaign, 2=Command, 3=Overlay
display_order = 56 # int | The display order for this event. 
is_priority = 56 # int | An integer indicating the priority of this event. Normal events have a priority of 0.
display_group_ids = [56] # list[int] | The Display Group IDs for this event. Display specific Group IDs should be used to schedule on single displays.
from_dt = '2013-10-20T19:20:30+01:00' # datetime | The from date for this event.
campaign_id = 56 # int | The Campaign ID to use for this Event. If a Layout is needed then the Campaign specific ID for that Layout should be used. (optional)
command_id = 56 # int | The Command ID to use for this Event. (optional)
day_part_id = 56 # int | The Day Part for this event. Overrides supported are 0(custom) and 1(always). Defaulted to 0. (optional)
sync_timezone = 56 # int | Should this schedule be synced to the resulting Display timezone? (optional)
to_dt = '2013-10-20T19:20:30+01:00' # datetime | The to date for this event. (optional)
recurrence_type = 'recurrence_type_example' # str | The type of recurrence to apply to this event. (optional)
recurrence_detail = 56 # int | The interval for the recurrence. (optional)
recurrence_range = '2013-10-20T19:20:30+01:00' # datetime | The end date for this events recurrence. (optional)
recurrence_repeats_on = 'recurrence_repeats_on_example' # str | The days of the week that this event repeats - weekly only (optional)

try:
    # Edit Schedule Event
    api_response = api_instance.schedule_edit(event_id, event_type_id, display_order, is_priority, display_group_ids, from_dt, campaign_id=campaign_id, command_id=command_id, day_part_id=day_part_id, sync_timezone=sync_timezone, to_dt=to_dt, recurrence_type=recurrence_type, recurrence_detail=recurrence_detail, recurrence_range=recurrence_range, recurrence_repeats_on=recurrence_repeats_on)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedule_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The Scheduled Event ID | 
 **event_type_id** | **int**| The Event Type Id to use for this Event. 1&#x3D;Campaign, 2&#x3D;Command, 3&#x3D;Overlay | 
 **display_order** | **int**| The display order for this event.  | 
 **is_priority** | **int**| An integer indicating the priority of this event. Normal events have a priority of 0. | 
 **display_group_ids** | [**list[int]**](int.md)| The Display Group IDs for this event. Display specific Group IDs should be used to schedule on single displays. | 
 **from_dt** | **datetime**| The from date for this event. | 
 **campaign_id** | **int**| The Campaign ID to use for this Event. If a Layout is needed then the Campaign specific ID for that Layout should be used. | [optional] 
 **command_id** | **int**| The Command ID to use for this Event. | [optional] 
 **day_part_id** | **int**| The Day Part for this event. Overrides supported are 0(custom) and 1(always). Defaulted to 0. | [optional] 
 **sync_timezone** | **int**| Should this schedule be synced to the resulting Display timezone? | [optional] 
 **to_dt** | **datetime**| The to date for this event. | [optional] 
 **recurrence_type** | **str**| The type of recurrence to apply to this event. | [optional] 
 **recurrence_detail** | **int**| The interval for the recurrence. | [optional] 
 **recurrence_range** | **datetime**| The end date for this events recurrence. | [optional] 
 **recurrence_repeats_on** | **str**| The days of the week that this event repeats - weekly only | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

