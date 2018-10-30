# swagger_client.DatasetApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_set_add**](DatasetApi.md#data_set_add) | **POST** /dataset | Add DataSet
[**data_set_column_add**](DatasetApi.md#data_set_column_add) | **POST** /dataset/{dataSetId}/column | Add Column
[**data_set_column_delete**](DatasetApi.md#data_set_column_delete) | **DELETE** /dataset/{dataSetId}/column/{dataSetColumnId} | Delete Column
[**data_set_column_edit**](DatasetApi.md#data_set_column_edit) | **PUT** /dataset/{dataSetId}/column/{dataSetColumnId} | Edit Column
[**data_set_column_search**](DatasetApi.md#data_set_column_search) | **GET** /dataset/{dataSetId}/column | Search Columns
[**data_set_copy**](DatasetApi.md#data_set_copy) | **POST** /dataset/copy/{dataSetId} | Copy DataSet
[**data_set_data**](DatasetApi.md#data_set_data) | **GET** /dataset/data/{dataSetId} | DataSet Data
[**data_set_data_add**](DatasetApi.md#data_set_data_add) | **POST** /dataset/data/{dataSetId} | Add Row
[**data_set_data_delete**](DatasetApi.md#data_set_data_delete) | **DELETE** /dataset/data/{dataSetId}/{rowId} | Delete Row
[**data_set_data_edit**](DatasetApi.md#data_set_data_edit) | **PUT** /dataset/data/{dataSetId}/{rowId} | Edit Row
[**data_set_delete**](DatasetApi.md#data_set_delete) | **DELETE** /dataset/{dataSetId} | Delete DataSet
[**data_set_edit**](DatasetApi.md#data_set_edit) | **PUT** /dataset/{dataSetId} | Edit DataSet
[**data_set_import**](DatasetApi.md#data_set_import) | **POST** /dataset/import/{dataSetId} | Import CSV
[**data_set_import_json**](DatasetApi.md#data_set_import_json) | **POST** /dataset/importjson/{dataSetId} | Import JSON
[**data_set_search**](DatasetApi.md#data_set_search) | **GET** /dataset | DataSet Search


# **data_set_add**
> DataSet data_set_add(data_set, is_remote, description=description, code=code, method=method, uri=uri, post_data=post_data, authentication=authentication, username=username, password=password, refresh_rate=refresh_rate, clear_rate=clear_rate, runs_after=runs_after, data_root=data_root, summarize=summarize, summarize_field=summarize_field)

Add DataSet

Add a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set = 'data_set_example' # str | The DataSet Name
is_remote = 56 # int | Is this a remote DataSet?
description = 'description_example' # str | A description of this DataSet (optional)
code = 'code_example' # str | A code for this DataSet (optional)
method = 'method_example' # str | The Request Method GET or POST (optional)
uri = 'uri_example' # str | The URI, without query parameters (optional)
post_data = 'post_data_example' # str | query parameter encoded data to add to the request (optional)
authentication = 'authentication_example' # str | HTTP Authentication method None|Basic|Digest (optional)
username = 'username_example' # str | HTTP Authentication User Name (optional)
password = 'password_example' # str | HTTP Authentication Password (optional)
refresh_rate = 56 # int | How often in seconds should this remote DataSet be refreshed (optional)
clear_rate = 56 # int | How often in seconds should this remote DataSet be truncated (optional)
runs_after = 56 # int | An optional dataSetId which should be run before this Remote DataSet (optional)
data_root = 'data_root_example' # str | The root of the data in the Remote source which is used as the base for all remote columns (optional)
summarize = 'summarize_example' # str | Should the data be aggregated? None|Summarize|Count (optional)
summarize_field = 'summarize_field_example' # str | Which field should be used to summarize (optional)

try:
    # Add DataSet
    api_response = api_instance.data_set_add(data_set, is_remote, description=description, code=code, method=method, uri=uri, post_data=post_data, authentication=authentication, username=username, password=password, refresh_rate=refresh_rate, clear_rate=clear_rate, runs_after=runs_after, data_root=data_root, summarize=summarize, summarize_field=summarize_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set** | **str**| The DataSet Name | 
 **is_remote** | **int**| Is this a remote DataSet? | 
 **description** | **str**| A description of this DataSet | [optional] 
 **code** | **str**| A code for this DataSet | [optional] 
 **method** | **str**| The Request Method GET or POST | [optional] 
 **uri** | **str**| The URI, without query parameters | [optional] 
 **post_data** | **str**| query parameter encoded data to add to the request | [optional] 
 **authentication** | **str**| HTTP Authentication method None|Basic|Digest | [optional] 
 **username** | **str**| HTTP Authentication User Name | [optional] 
 **password** | **str**| HTTP Authentication Password | [optional] 
 **refresh_rate** | **int**| How often in seconds should this remote DataSet be refreshed | [optional] 
 **clear_rate** | **int**| How often in seconds should this remote DataSet be truncated | [optional] 
 **runs_after** | **int**| An optional dataSetId which should be run before this Remote DataSet | [optional] 
 **data_root** | **str**| The root of the data in the Remote source which is used as the base for all remote columns | [optional] 
 **summarize** | **str**| Should the data be aggregated? None|Summarize|Count | [optional] 
 **summarize_field** | **str**| Which field should be used to summarize | [optional] 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_column_add**
> DataSetColumn data_set_column_add(data_set_id, heading, column_order, data_type_id, data_set_column_type_id, show_filter, show_sort, list_content=list_content, formula=formula, remote_field=remote_field)

Add Column

Add a Column to a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
heading = 'heading_example' # str | The heading for the Column
column_order = 56 # int | The display order for this column
data_type_id = 56 # int | The data type ID for this column
data_set_column_type_id = 56 # int | The column type for this column
show_filter = 56 # int | Flag indicating whether this column should present a filter on DataEntry
show_sort = 56 # int | Flag indicating whether this column should allow sorting on DataEntry
list_content = 'list_content_example' # str | A comma separated list of content for drop downs (optional)
formula = 'formula_example' # str | MySQL SELECT syntax formula for this Column if the column type is formula (optional)
remote_field = 'remote_field_example' # str | JSON-String to select Data from the Remote DataSet (optional)

try:
    # Add Column
    api_response = api_instance.data_set_column_add(data_set_id, heading, column_order, data_type_id, data_set_column_type_id, show_filter, show_sort, list_content=list_content, formula=formula, remote_field=remote_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_column_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **heading** | **str**| The heading for the Column | 
 **column_order** | **int**| The display order for this column | 
 **data_type_id** | **int**| The data type ID for this column | 
 **data_set_column_type_id** | **int**| The column type for this column | 
 **show_filter** | **int**| Flag indicating whether this column should present a filter on DataEntry | 
 **show_sort** | **int**| Flag indicating whether this column should allow sorting on DataEntry | 
 **list_content** | **str**| A comma separated list of content for drop downs | [optional] 
 **formula** | **str**| MySQL SELECT syntax formula for this Column if the column type is formula | [optional] 
 **remote_field** | **str**| JSON-String to select Data from the Remote DataSet | [optional] 

### Return type

[**DataSetColumn**](DataSetColumn.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_column_delete**
> data_set_column_delete(data_set_id, data_set_column_id)

Delete Column

Delete DataSet Column

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set_column_id = 56 # int | The Column ID

try:
    # Delete Column
    api_instance.data_set_column_delete(data_set_id, data_set_column_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_column_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set_column_id** | **int**| The Column ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_column_edit**
> DataSetColumn data_set_column_edit(data_set_id, data_set_column_id, heading, column_order, data_type_id, data_set_column_type_id, show_filter, show_sort, list_content=list_content, formula=formula, remote_field=remote_field)

Edit Column

Edit a Column to a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set_column_id = 56 # int | The Column ID
heading = 'heading_example' # str | The heading for the Column
column_order = 56 # int | The display order for this column
data_type_id = 56 # int | The data type ID for this column
data_set_column_type_id = 56 # int | The column type for this column
show_filter = 56 # int | Flag indicating whether this column should present a filter on DataEntry
show_sort = 56 # int | Flag indicating whether this column should allow sorting on DataEntry
list_content = 'list_content_example' # str | A comma separated list of content for drop downs (optional)
formula = 'formula_example' # str | MySQL SELECT syntax formula for this Column if the column type is formula (optional)
remote_field = 'remote_field_example' # str | JSON-String to select Data from the Remote DataSet (optional)

try:
    # Edit Column
    api_response = api_instance.data_set_column_edit(data_set_id, data_set_column_id, heading, column_order, data_type_id, data_set_column_type_id, show_filter, show_sort, list_content=list_content, formula=formula, remote_field=remote_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_column_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set_column_id** | **int**| The Column ID | 
 **heading** | **str**| The heading for the Column | 
 **column_order** | **int**| The display order for this column | 
 **data_type_id** | **int**| The data type ID for this column | 
 **data_set_column_type_id** | **int**| The column type for this column | 
 **show_filter** | **int**| Flag indicating whether this column should present a filter on DataEntry | 
 **show_sort** | **int**| Flag indicating whether this column should allow sorting on DataEntry | 
 **list_content** | **str**| A comma separated list of content for drop downs | [optional] 
 **formula** | **str**| MySQL SELECT syntax formula for this Column if the column type is formula | [optional] 
 **remote_field** | **str**| JSON-String to select Data from the Remote DataSet | [optional] 

### Return type

[**DataSetColumn**](DataSetColumn.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_column_search**
> list[DataSetColumn] data_set_column_search(data_set_id, data_set_column_id=data_set_column_id)

Search Columns

Search Columns for DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set_column_id = 56 # int | Filter by DataSet ColumnID (optional)

try:
    # Search Columns
    api_response = api_instance.data_set_column_search(data_set_id, data_set_column_id=data_set_column_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_column_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set_column_id** | **int**| Filter by DataSet ColumnID | [optional] 

### Return type

[**list[DataSetColumn]**](DataSetColumn.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_copy**
> DataSet data_set_copy(data_set_id, data_set, description=description, code=code)

Copy DataSet

Copy a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set = 'data_set_example' # str | The DataSet Name
description = 'description_example' # str | A description of this DataSet (optional)
code = 'code_example' # str | A code for this DataSet (optional)

try:
    # Copy DataSet
    api_response = api_instance.data_set_copy(data_set_id, data_set, description=description, code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set** | **str**| The DataSet Name | 
 **description** | **str**| A description of this DataSet | [optional] 
 **code** | **str**| A code for this DataSet | [optional] 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_data**
> data_set_data(data_set_id)

DataSet Data

Get Data for DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID

try:
    # DataSet Data
    api_instance.data_set_data(data_set_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_data_add**
> data_set_data_add(data_set_id, data_set_column_id_id)

Add Row

Add a row of Data to a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set_column_id_id = 'data_set_column_id_id_example' # str | Parameter for each dataSetColumnId in the DataSet

try:
    # Add Row
    api_instance.data_set_data_add(data_set_id, data_set_column_id_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_data_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set_column_id_id** | **str**| Parameter for each dataSetColumnId in the DataSet | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_data_delete**
> data_set_data_delete(data_set_id, row_id)

Delete Row

Delete a row of Data to a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
row_id = 56 # int | The Row ID of the Data to Delete

try:
    # Delete Row
    api_instance.data_set_data_delete(data_set_id, row_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_data_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **row_id** | **int**| The Row ID of the Data to Delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_data_edit**
> data_set_data_edit(data_set_id, row_id, data_set_column_id_id)

Edit Row

Edit a row of Data to a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
row_id = 56 # int | The Row ID of the Data to Edit
data_set_column_id_id = 'data_set_column_id_id_example' # str | Parameter for each dataSetColumnId in the DataSet

try:
    # Edit Row
    api_instance.data_set_data_edit(data_set_id, row_id, data_set_column_id_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_data_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **row_id** | **int**| The Row ID of the Data to Edit | 
 **data_set_column_id_id** | **str**| Parameter for each dataSetColumnId in the DataSet | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_delete**
> data_set_delete(data_set_id)

Delete DataSet

Delete a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID

try:
    # Delete DataSet
    api_instance.data_set_delete(data_set_id)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_edit**
> DataSet data_set_edit(data_set_id, data_set, is_remote, description=description, code=code, method=method, uri=uri, post_data=post_data, authentication=authentication, username=username, password=password, refresh_rate=refresh_rate, clear_rate=clear_rate, runs_after=runs_after, data_root=data_root, summarize=summarize, summarize_field=summarize_field)

Edit DataSet

Edit a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID
data_set = 'data_set_example' # str | The DataSet Name
is_remote = 56 # int | Is this a remote DataSet?
description = 'description_example' # str | A description of this DataSet (optional)
code = 'code_example' # str | A code for this DataSet (optional)
method = 'method_example' # str | The Request Method GET or POST (optional)
uri = 'uri_example' # str | The URI, without query parameters (optional)
post_data = 'post_data_example' # str | query parameter encoded data to add to the request (optional)
authentication = 'authentication_example' # str | HTTP Authentication method None|Basic|Digest (optional)
username = 'username_example' # str | HTTP Authentication User Name (optional)
password = 'password_example' # str | HTTP Authentication Password (optional)
refresh_rate = 56 # int | How often in seconds should this remote DataSet be refreshed (optional)
clear_rate = 56 # int | How often in seconds should this remote DataSet be truncated (optional)
runs_after = 56 # int | An optional dataSetId which should be run before this Remote DataSet (optional)
data_root = 'data_root_example' # str | The root of the data in the Remote source which is used as the base for all remote columns (optional)
summarize = 'summarize_example' # str | Should the data be aggregated? None|Summarize|Count (optional)
summarize_field = 'summarize_field_example' # str | Which field should be used to summarize (optional)

try:
    # Edit DataSet
    api_response = api_instance.data_set_edit(data_set_id, data_set, is_remote, description=description, code=code, method=method, uri=uri, post_data=post_data, authentication=authentication, username=username, password=password, refresh_rate=refresh_rate, clear_rate=clear_rate, runs_after=runs_after, data_root=data_root, summarize=summarize, summarize_field=summarize_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID | 
 **data_set** | **str**| The DataSet Name | 
 **is_remote** | **int**| Is this a remote DataSet? | 
 **description** | **str**| A description of this DataSet | [optional] 
 **code** | **str**| A code for this DataSet | [optional] 
 **method** | **str**| The Request Method GET or POST | [optional] 
 **uri** | **str**| The URI, without query parameters | [optional] 
 **post_data** | **str**| query parameter encoded data to add to the request | [optional] 
 **authentication** | **str**| HTTP Authentication method None|Basic|Digest | [optional] 
 **username** | **str**| HTTP Authentication User Name | [optional] 
 **password** | **str**| HTTP Authentication Password | [optional] 
 **refresh_rate** | **int**| How often in seconds should this remote DataSet be refreshed | [optional] 
 **clear_rate** | **int**| How often in seconds should this remote DataSet be truncated | [optional] 
 **runs_after** | **int**| An optional dataSetId which should be run before this Remote DataSet | [optional] 
 **data_root** | **str**| The root of the data in the Remote source which is used as the base for all remote columns | [optional] 
 **summarize** | **str**| Should the data be aggregated? None|Summarize|Count | [optional] 
 **summarize_field** | **str**| Which field should be used to summarize | [optional] 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_import**
> data_set_import(data_set_id, files, csv_import_data_set_column_id, overwrite=overwrite, ignorefirstrow=ignorefirstrow)

Import CSV

Import a CSV into a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID to import into.
files = '/path/to/file.txt' # file | The file
csv_import_data_set_column_id = 56 # int | You need to provide dataSetColumnId after csvImport_, to know your dataSet columns Ids, you will need to use the GET /dataset/{dataSetId}/column call first. The value of this parameter is the index of the column in your csv file, where the first column is 1
overwrite = 56 # int | flag (0,1) Set to 1 to erase all content in the dataSet and overwrite it with new content in this import (optional)
ignorefirstrow = 56 # int | flag (0,1), Set to 1 to Ignore first row, useful if the CSV file has headings (optional)

try:
    # Import CSV
    api_instance.data_set_import(data_set_id, files, csv_import_data_set_column_id, overwrite=overwrite, ignorefirstrow=ignorefirstrow)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID to import into. | 
 **files** | **file**| The file | 
 **csv_import_data_set_column_id** | **int**| You need to provide dataSetColumnId after csvImport_, to know your dataSet columns Ids, you will need to use the GET /dataset/{dataSetId}/column call first. The value of this parameter is the index of the column in your csv file, where the first column is 1 | 
 **overwrite** | **int**| flag (0,1) Set to 1 to erase all content in the dataSet and overwrite it with new content in this import | [optional] 
 **ignorefirstrow** | **int**| flag (0,1), Set to 1 to Ignore first row, useful if the CSV file has headings | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_import_json**
> data_set_import_json(data_set_id, data)

Import JSON

Import JSON into a DataSet

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | The DataSet ID to import into.
data = swagger_client.null() #  | The row data, field name vs field data format. e.g. { uniqueKeys: [col1], rows: [{col1: value1}]}

try:
    # Import JSON
    api_instance.data_set_import_json(data_set_id, data)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_import_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| The DataSet ID to import into. | 
 **data** | [****](.md)| The row data, field name vs field data format. e.g. { uniqueKeys: [col1], rows: [{col1: value1}]} | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_set_search**
> list[DataSet] data_set_search(data_set_id=data_set_id, data_set=data_set, code=code, embed=embed)

DataSet Search

Search this users DataSets

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
api_instance = swagger_client.DatasetApi(swagger_client.ApiClient(configuration))
data_set_id = 56 # int | Filter by DataSet Id (optional)
data_set = 'data_set_example' # str | Filter by DataSet Name (optional)
code = 'code_example' # str | Filter by DataSet Code (optional)
embed = 'embed_example' # str | Embed related data such as columns (optional)

try:
    # DataSet Search
    api_response = api_instance.data_set_search(data_set_id=data_set_id, data_set=data_set, code=code, embed=embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->data_set_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**| Filter by DataSet Id | [optional] 
 **data_set** | **str**| Filter by DataSet Name | [optional] 
 **code** | **str**| Filter by DataSet Code | [optional] 
 **embed** | **str**| Embed related data such as columns | [optional] 

### Return type

[**list[DataSet]**](DataSet.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

