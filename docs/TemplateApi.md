# swagger_client.TemplateApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_add_from_layout**](TemplateApi.md#template_add_from_layout) | **POST** /template/{layoutId} | Add a template from a Layout
[**template_search**](TemplateApi.md#template_search) | **GET** /template | Template Search


# **template_add_from_layout**
> Layout template_add_from_layout(layout_id, include_widgets, name, tags=tags, description=description)

Add a template from a Layout

Use the provided layout as a base for a new template

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
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
layout_id = 56 # int | The Layout ID
include_widgets = 56 # int | Flag indicating whether to include the widgets in the Template
name = 'name_example' # str | The Template Name
tags = 'tags_example' # str | Comma separated list of Tags for the template (optional)
description = 'description_example' # str | A description of the Template (optional)

try:
    # Add a template from a Layout
    api_response = api_instance.template_add_from_layout(layout_id, include_widgets, name, tags=tags, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->template_add_from_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| The Layout ID | 
 **include_widgets** | **int**| Flag indicating whether to include the widgets in the Template | 
 **name** | **str**| The Template Name | 
 **tags** | **str**| Comma separated list of Tags for the template | [optional] 
 **description** | **str**| A description of the Template | [optional] 

### Return type

[**Layout**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_search**
> list[Layout] template_search()

Template Search

Search templates this user has access to

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
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))

try:
    # Template Search
    api_response = api_instance.template_search()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->template_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Layout]**](Layout.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

