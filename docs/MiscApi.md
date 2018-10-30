# swagger_client.MiscApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about**](MiscApi.md#about) | **GET** /about | About
[**clock**](MiscApi.md#clock) | **GET** /clock | The current CMS time


# **about**
> dict(str, str) about()

About

Information about this API, such as Version code, etc

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
api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))

try:
    # About
    api_response = api_instance.about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->about: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clock**
> dict(str, str) clock()

The current CMS time

The Time

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
api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))

try:
    # The current CMS time
    api_response = api_instance.clock()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->clock: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

