# swagger_client.DayPartApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**day_part_add**](DayPartApi.md#day_part_add) | **POST** /daypart | Daypart Add
[**day_part_add_0**](DayPartApi.md#day_part_add_0) | **PUT** /daypart/{dayPartId} | Daypart Add
[**day_part_delete**](DayPartApi.md#day_part_delete) | **DELETE** /daypart/{dayPartId} | Delete DayPart
[**day_part_search**](DayPartApi.md#day_part_search) | **GET** /daypart | Daypart Search


# **day_part_add**
> DayPart day_part_add(name, start_time, end_time, description=description, exception_days=exception_days, exception_start_times=exception_start_times, exception_end_times=exception_end_times)

Daypart Add

Add a Daypart

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
api_instance = swagger_client.DayPartApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The Daypart Name
start_time = 'start_time_example' # str | The start time for this day part
end_time = 'end_time_example' # str | The end time for this day part
description = 'description_example' # str | A description for the dayPart (optional)
exception_days = ['exception_days_example'] # list[str] | String array of exception days (optional)
exception_start_times = ['exception_start_times_example'] # list[str] | String array of exception start times to match the exception days (optional)
exception_end_times = ['exception_end_times_example'] # list[str] | String array of exception end times to match the exception days (optional)

try:
    # Daypart Add
    api_response = api_instance.day_part_add(name, start_time, end_time, description=description, exception_days=exception_days, exception_start_times=exception_start_times, exception_end_times=exception_end_times)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DayPartApi->day_part_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The Daypart Name | 
 **start_time** | **str**| The start time for this day part | 
 **end_time** | **str**| The end time for this day part | 
 **description** | **str**| A description for the dayPart | [optional] 
 **exception_days** | [**list[str]**](str.md)| String array of exception days | [optional] 
 **exception_start_times** | [**list[str]**](str.md)| String array of exception start times to match the exception days | [optional] 
 **exception_end_times** | [**list[str]**](str.md)| String array of exception end times to match the exception days | [optional] 

### Return type

[**DayPart**](DayPart.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **day_part_add_0**
> DayPart day_part_add_0(day_part_id, name, start_time, end_time, description=description, exception_days=exception_days, exception_start_times=exception_start_times, exception_end_times=exception_end_times)

Daypart Add

Add a Daypart

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
api_instance = swagger_client.DayPartApi(swagger_client.ApiClient(configuration))
day_part_id = 56 # int | The Daypart Id
name = 'name_example' # str | The Daypart Name
start_time = 'start_time_example' # str | The start time for this day part
end_time = 'end_time_example' # str | The end time for this day part
description = 'description_example' # str | A description for the dayPart (optional)
exception_days = ['exception_days_example'] # list[str] | String array of exception days (optional)
exception_start_times = ['exception_start_times_example'] # list[str] | String array of exception start times to match the exception days (optional)
exception_end_times = ['exception_end_times_example'] # list[str] | String array of exception end times to match the exception days (optional)

try:
    # Daypart Add
    api_response = api_instance.day_part_add_0(day_part_id, name, start_time, end_time, description=description, exception_days=exception_days, exception_start_times=exception_start_times, exception_end_times=exception_end_times)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DayPartApi->day_part_add_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day_part_id** | **int**| The Daypart Id | 
 **name** | **str**| The Daypart Name | 
 **start_time** | **str**| The start time for this day part | 
 **end_time** | **str**| The end time for this day part | 
 **description** | **str**| A description for the dayPart | [optional] 
 **exception_days** | [**list[str]**](str.md)| String array of exception days | [optional] 
 **exception_start_times** | [**list[str]**](str.md)| String array of exception start times to match the exception days | [optional] 
 **exception_end_times** | [**list[str]**](str.md)| String array of exception end times to match the exception days | [optional] 

### Return type

[**DayPart**](DayPart.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **day_part_delete**
> day_part_delete(day_part_id)

Delete DayPart

Delete the provided dayPart

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
api_instance = swagger_client.DayPartApi(swagger_client.ApiClient(configuration))
day_part_id = 56 # int | The Daypart Id to Delete

try:
    # Delete DayPart
    api_instance.day_part_delete(day_part_id)
except ApiException as e:
    print("Exception when calling DayPartApi->day_part_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day_part_id** | **int**| The Daypart Id to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **day_part_search**
> list[DayPart] day_part_search(day_part_id=day_part_id, name=name, embed=embed)

Daypart Search

Search dayparts

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
api_instance = swagger_client.DayPartApi(swagger_client.ApiClient(configuration))
day_part_id = 56 # int | The dayPart ID to Search (optional)
name = 'name_example' # str | The name of the dayPart to Search (optional)
embed = 'embed_example' # str | Embed related data such as exceptions (optional)

try:
    # Daypart Search
    api_response = api_instance.day_part_search(day_part_id=day_part_id, name=name, embed=embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DayPartApi->day_part_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day_part_id** | **int**| The dayPart ID to Search | [optional] 
 **name** | **str**| The name of the dayPart to Search | [optional] 
 **embed** | **str**| Embed related data such as exceptions | [optional] 

### Return type

[**list[DayPart]**](DayPart.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

