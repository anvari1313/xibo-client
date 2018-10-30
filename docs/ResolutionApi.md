# swagger_client.ResolutionApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolution_add**](ResolutionApi.md#resolution_add) | **POST** /resolution | Add Resolution
[**resolution_delete**](ResolutionApi.md#resolution_delete) | **DELETE** /resolution/{resolutionId} | Delete Resolution
[**resolution_edit**](ResolutionApi.md#resolution_edit) | **PUT** /resolution/{resolutionId} | Edit Resolution
[**resolution_search**](ResolutionApi.md#resolution_search) | **GET** /resolution | Resolution Search


# **resolution_add**
> Resolution resolution_add(resolution, width, height)

Add Resolution

Add new Resolution

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
api_instance = swagger_client.ResolutionApi(swagger_client.ApiClient(configuration))
resolution = 'resolution_example' # str | A name for the Resolution
width = 56 # int | The Display Width of the Resolution
height = 56 # int | The Display Height of the Resolution

try:
    # Add Resolution
    api_response = api_instance.resolution_add(resolution, width, height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResolutionApi->resolution_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **str**| A name for the Resolution | 
 **width** | **int**| The Display Width of the Resolution | 
 **height** | **int**| The Display Height of the Resolution | 

### Return type

[**Resolution**](Resolution.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolution_delete**
> resolution_delete(resolution_id)

Delete Resolution

Delete Resolution

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
api_instance = swagger_client.ResolutionApi(swagger_client.ApiClient(configuration))
resolution_id = 56 # int | The Resolution ID to Delete

try:
    # Delete Resolution
    api_instance.resolution_delete(resolution_id)
except ApiException as e:
    print("Exception when calling ResolutionApi->resolution_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution_id** | **int**| The Resolution ID to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolution_edit**
> Resolution resolution_edit(resolution_id, resolution, width, height)

Edit Resolution

Edit new Resolution

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
api_instance = swagger_client.ResolutionApi(swagger_client.ApiClient(configuration))
resolution_id = 56 # int | The Resolution ID to Edit
resolution = 'resolution_example' # str | A name for the Resolution
width = 56 # int | The Display Width of the Resolution
height = 56 # int | The Display Height of the Resolution

try:
    # Edit Resolution
    api_response = api_instance.resolution_edit(resolution_id, resolution, width, height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResolutionApi->resolution_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution_id** | **int**| The Resolution ID to Edit | 
 **resolution** | **str**| A name for the Resolution | 
 **width** | **int**| The Display Width of the Resolution | 
 **height** | **int**| The Display Height of the Resolution | 

### Return type

[**Resolution**](Resolution.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolution_search**
> list[Resolution] resolution_search(resolution_id=resolution_id, resolution=resolution, enabled=enabled)

Resolution Search

Search Resolutions this user has access to

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
api_instance = swagger_client.ResolutionApi(swagger_client.ApiClient(configuration))
resolution_id = 56 # int | Filter by Resolution Id (optional)
resolution = 'resolution_example' # str | Filter by Resolution Name (optional)
enabled = 56 # int | Filter by Enabled (optional)

try:
    # Resolution Search
    api_response = api_instance.resolution_search(resolution_id=resolution_id, resolution=resolution, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResolutionApi->resolution_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution_id** | **int**| Filter by Resolution Id | [optional] 
 **resolution** | **str**| Filter by Resolution Name | [optional] 
 **enabled** | **int**| Filter by Enabled | [optional] 

### Return type

[**list[Resolution]**](Resolution.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

