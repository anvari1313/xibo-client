# swagger_client.CommandApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_add**](CommandApi.md#command_add) | **POST** /command | Command Add
[**command_delete**](CommandApi.md#command_delete) | **DELETE** /command/{commandId} | Delete Command
[**command_edit**](CommandApi.md#command_edit) | **PUT** /command/{commandId} | Edit Command
[**command_search**](CommandApi.md#command_search) | **GET** /command | Command Search


# **command_add**
> Command command_add(command, code, description=description)

Command Add

Add a Command

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
api_instance = swagger_client.CommandApi(swagger_client.ApiClient(configuration))
command = 'command_example' # str | The Command Name
code = 'code_example' # str | A unique code for this command
description = 'description_example' # str | A description for the command (optional)

try:
    # Command Add
    api_response = api_instance.command_add(command, code, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->command_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| The Command Name | 
 **code** | **str**| A unique code for this command | 
 **description** | **str**| A description for the command | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_delete**
> command_delete(command_id)

Delete Command

Delete the provided command

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
api_instance = swagger_client.CommandApi(swagger_client.ApiClient(configuration))
command_id = 56 # int | The Command Id to Delete

try:
    # Delete Command
    api_instance.command_delete(command_id)
except ApiException as e:
    print("Exception when calling CommandApi->command_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**| The Command Id to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_edit**
> Command command_edit(command_id, command, description=description)

Edit Command

Edit the provided command

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
api_instance = swagger_client.CommandApi(swagger_client.ApiClient(configuration))
command_id = 56 # int | The Command Id to Edit
command = 'command_example' # str | The Command Name
description = 'description_example' # str | A description for the command (optional)

try:
    # Edit Command
    api_response = api_instance.command_edit(command_id, command, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->command_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**| The Command Id to Edit | 
 **command** | **str**| The Command Name | 
 **description** | **str**| A description for the command | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_search**
> list[Command] command_search(command_id=command_id, command=command, code=code)

Command Search

Search this users Commands

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
api_instance = swagger_client.CommandApi(swagger_client.ApiClient(configuration))
command_id = 56 # int | Filter by Command Id (optional)
command = 'command_example' # str | Filter by Command Name (optional)
code = 'code_example' # str | Filter by Command Code (optional)

try:
    # Command Search
    api_response = api_instance.command_search(command_id=command_id, command=command, code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->command_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**| Filter by Command Id | [optional] 
 **command** | **str**| Filter by Command Name | [optional] 
 **code** | **str**| Filter by Command Code | [optional] 

### Return type

[**list[Command]**](Command.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

