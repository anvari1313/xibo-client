# swagger_client.CampaignApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaign_add**](CampaignApi.md#campaign_add) | **POST** /campaign | Add Campaign
[**campaign_assign_layout**](CampaignApi.md#campaign_assign_layout) | **POST** /campaign/layout/assign/{campaignId} | Assign Layouts
[**campaign_delete**](CampaignApi.md#campaign_delete) | **DELETE** /campaign/{campaignId} | Delete Campaign
[**campaign_edit**](CampaignApi.md#campaign_edit) | **PUT** /campaign/{campaignId} | Edit Campaign
[**campaign_search**](CampaignApi.md#campaign_search) | **GET** /campaign | Search Campaigns


# **campaign_add**
> Campaign campaign_add(name)

Add Campaign

Add a Campaign

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
api_instance = swagger_client.CampaignApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name for this Campaign

try:
    # Add Campaign
    api_response = api_instance.campaign_add(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->campaign_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for this Campaign | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_assign_layout**
> campaign_assign_layout(campaign_id, layout_id, unassign_layout_id=unassign_layout_id)

Assign Layouts

Assign Layouts to a Campaign

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
api_instance = swagger_client.CampaignApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | The Campaign ID
layout_id = [swagger_client.LayoutAssignmentArray()] # list[LayoutAssignmentArray] | Array of Layout ID/Display Orders to Assign
unassign_layout_id = [swagger_client.LayoutAssignmentArray()] # list[LayoutAssignmentArray] | Array of Layout ID/Display Orders to unassign (optional)

try:
    # Assign Layouts
    api_instance.campaign_assign_layout(campaign_id, layout_id, unassign_layout_id=unassign_layout_id)
except ApiException as e:
    print("Exception when calling CampaignApi->campaign_assign_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The Campaign ID | 
 **layout_id** | [**list[LayoutAssignmentArray]**](LayoutAssignmentArray.md)| Array of Layout ID/Display Orders to Assign | 
 **unassign_layout_id** | [**list[LayoutAssignmentArray]**](LayoutAssignmentArray.md)| Array of Layout ID/Display Orders to unassign | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_delete**
> campaign_delete(campaign_id)

Delete Campaign

Delete an existing Campaign

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
api_instance = swagger_client.CampaignApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | The Campaign ID to Delete

try:
    # Delete Campaign
    api_instance.campaign_delete(campaign_id)
except ApiException as e:
    print("Exception when calling CampaignApi->campaign_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The Campaign ID to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_edit**
> Campaign campaign_edit(campaign_id, name)

Edit Campaign

Edit an existing Campaign

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
api_instance = swagger_client.CampaignApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | The Campaign ID to Edit
name = 'name_example' # str | Name for this Campaign

try:
    # Edit Campaign
    api_response = api_instance.campaign_edit(campaign_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->campaign_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The Campaign ID to Edit | 
 **name** | **str**| Name for this Campaign | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_search**
> list[Campaign] campaign_search(campaign_id=campaign_id, name=name, tags=tags, has_layouts=has_layouts, is_layout_specific=is_layout_specific, retired=retired, total_duration=total_duration)

Search Campaigns

Search all Campaigns this user has access to

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
api_instance = swagger_client.CampaignApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | Filter by Campaign Id (optional)
name = 'name_example' # str | Filter by Name (optional)
tags = 'tags_example' # str | Filter by Tags (optional)
has_layouts = 56 # int | Filter by has layouts (optional)
is_layout_specific = 56 # int | Filter by whether this Campaign is specific to a Layout or User added (optional)
retired = 56 # int | Filter by retired (optional)
total_duration = 56 # int | Should we total the duration? (optional)

try:
    # Search Campaigns
    api_response = api_instance.campaign_search(campaign_id=campaign_id, name=name, tags=tags, has_layouts=has_layouts, is_layout_specific=is_layout_specific, retired=retired, total_duration=total_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->campaign_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Filter by Campaign Id | [optional] 
 **name** | **str**| Filter by Name | [optional] 
 **tags** | **str**| Filter by Tags | [optional] 
 **has_layouts** | **int**| Filter by has layouts | [optional] 
 **is_layout_specific** | **int**| Filter by whether this Campaign is specific to a Layout or User added | [optional] 
 **retired** | **int**| Filter by retired | [optional] 
 **total_duration** | **int**| Should we total the duration? | [optional] 

### Return type

[**list[Campaign]**](Campaign.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

