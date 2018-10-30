# swagger_client.StatisticsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_search**](StatisticsApi.md#stats_search) | **GET** /stats | 


# **stats_search**
> list[StatisticsData] stats_search(type=type, from_dt=from_dt, to_dt=to_dt, display_id=display_id, layout_id=layout_id, media_id=media_id)



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
api_instance = swagger_client.StatisticsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | The type of stat to return. Layout|Media|Widget or All (optional)
from_dt = 'from_dt_example' # str | The start date for the filter. Default = 24 hours ago (optional)
to_dt = 'to_dt_example' # str | The end date for the filter. Default = now. (optional)
display_id = 56 # int | An optional display Id to filter (optional)
layout_id = [56] # list[int] | An optional array of layout Id to filter (optional)
media_id = [56] # list[int] | An optional array of media Id to filter (optional)

try:
    api_response = api_instance.stats_search(type=type, from_dt=from_dt, to_dt=to_dt, display_id=display_id, layout_id=layout_id, media_id=media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->stats_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of stat to return. Layout|Media|Widget or All | [optional] 
 **from_dt** | **str**| The start date for the filter. Default &#x3D; 24 hours ago | [optional] 
 **to_dt** | **str**| The end date for the filter. Default &#x3D; now. | [optional] 
 **display_id** | **int**| An optional display Id to filter | [optional] 
 **layout_id** | [**list[int]**](int.md)| An optional array of layout Id to filter | [optional] 
 **media_id** | [**list[int]**](int.md)| An optional array of media Id to filter | [optional] 

### Return type

[**list[StatisticsData]**](StatisticsData.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

