# swagger_client.WidgetApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**widget_assigned_audio_edit**](WidgetApi.md#widget_assigned_audio_edit) | **PUT** /playlist/widget/{widgetId}/audio | Parameters for edting/adding audio file to a specific widget
[**widget_audio_delete**](WidgetApi.md#widget_audio_delete) | **DELETE** /playlist/widget/{widgetId}/audio | Delete assigned audio widget
[**widget_audio_edit**](WidgetApi.md#widget_audio_edit) | **POST** /playlist/widget/audio/{playlistId} | Parameters for editing existing audio widget on a layout
[**widget_chart_add**](WidgetApi.md#widget_chart_add) | **POST** /playlist/widget/chart/{playlistId} | Add a Chart Widget
[**widget_clock_add**](WidgetApi.md#widget_clock_add) | **POST** /playlist/widget/clock/{playlistId} | Add a Clock Widget
[**widget_currencies_add**](WidgetApi.md#widget_currencies_add) | **POST** /playlist/widget/currencies/{playlistId} | Add a Currencies Widget
[**widget_delete**](WidgetApi.md#widget_delete) | **DELETE** /playlist/widget/{widgetId} | Delete a Widget
[**widget_edit**](WidgetApi.md#widget_edit) | **PUT** /playlist/widget/{widgetId} | Edit a Widget
[**widget_edit_transition**](WidgetApi.md#widget_edit_transition) | **PUT** /playlist/widget/transition/{type}/{widgetId} | Adds In/Out transition
[**widget_embedded_add**](WidgetApi.md#widget_embedded_add) | **POST** /playlist/widget/embedded/{playlistId} | Add a Embedded Widget
[**widget_finance_add**](WidgetApi.md#widget_finance_add) | **POST** /playlist/widget/finance/{playlistId} | Add a Finance Widget
[**widget_google_traffic_add**](WidgetApi.md#widget_google_traffic_add) | **POST** /playlist/widget/googleTraffic/{playlistId} | Add a Google Traffic Widget
[**widget_hls_add**](WidgetApi.md#widget_hls_add) | **POST** /playlist/widget/hls/{playlistId} | Add a HLS Widget
[**widget_image_edit**](WidgetApi.md#widget_image_edit) | **POST** /playlist/widget/image/{playlistId} | Parameters for editing existing image on a layout
[**widget_local_video_add**](WidgetApi.md#widget_local_video_add) | **POST** /playlist/widget/localVideo/{playlistId} | Add a Local Video Widget
[**widget_notification_add**](WidgetApi.md#widget_notification_add) | **POST** /playlist/widget/notificationview/{playlistId} | Add a Notification Widget
[**widget_pdf_edit**](WidgetApi.md#widget_pdf_edit) | **POST** /playlist/widget/pdf/{playlistId} | Parameters for editing existing pdf on a layout
[**widget_shell_command_add**](WidgetApi.md#widget_shell_command_add) | **POST** /playlist/widget/shellCommand/{playlistId} | Add a Shell Command Widget
[**widget_stocks_add**](WidgetApi.md#widget_stocks_add) | **POST** /playlist/widget/stocks/{playlistId} | Add a Stocks Widget
[**widget_text_add**](WidgetApi.md#widget_text_add) | **POST** /playlist/widget/text/{playlistId} | Add a Text Widget
[**widget_ticker_add**](WidgetApi.md#widget_ticker_add) | **POST** /playlist/widget/ticker/{playlistId} | Add a ticker Widget
[**widget_twitter_add**](WidgetApi.md#widget_twitter_add) | **POST** /playlist/widget/twitter/{playlistId} | Add a Twitter Widget
[**widget_twitter_metro_add**](WidgetApi.md#widget_twitter_metro_add) | **POST** /playlist/widget/twittermetro/{playlistId} | Add a Twitter Metro Widget
[**widget_video_edit**](WidgetApi.md#widget_video_edit) | **POST** /playlist/widget/video/{playlistId} | Parameters for editing existing video on a layout
[**widget_video_in_add**](WidgetApi.md#widget_video_in_add) | **POST** /playlist/widget/videoin/{playlistId} | Add a Video In Widget
[**widget_weather_add**](WidgetApi.md#widget_weather_add) | **POST** /playlist/widget/forecastIo/{playlistId} | Add a Weather Widget
[**widget_webpage_add**](WidgetApi.md#widget_webpage_add) | **POST** /playlist/widget/webpage/{playlistId} | Add a Web page Widget
[**widgetdata_set_view_add**](WidgetApi.md#widgetdata_set_view_add) | **POST** /playlist/widget/dataSetView/{playlistId} | Add a dataSetView Widget


# **widget_assigned_audio_edit**
> Widget widget_assigned_audio_edit(widget_id, media_id=media_id, volume=volume, loop=loop)

Parameters for edting/adding audio file to a specific widget

Parameters for edting/adding audio file to a specific widget

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
widget_id = 56 # int | Id of a widget to which you want to add audio or edit existing audio
media_id = 56 # int | Id of a audio file in CMS library you wish to add to a widget (optional)
volume = 56 # int | Volume percentage(0-100) for this audio to play at (optional)
loop = 56 # int | Flag (0, 1) Should the audio loop if it finishes before the widget has finished? (optional)

try:
    # Parameters for edting/adding audio file to a specific widget
    api_response = api_instance.widget_assigned_audio_edit(widget_id, media_id=media_id, volume=volume, loop=loop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_assigned_audio_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_id** | **int**| Id of a widget to which you want to add audio or edit existing audio | 
 **media_id** | **int**| Id of a audio file in CMS library you wish to add to a widget | [optional] 
 **volume** | **int**| Volume percentage(0-100) for this audio to play at | [optional] 
 **loop** | **int**| Flag (0, 1) Should the audio loop if it finishes before the widget has finished? | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_audio_delete**
> widget_audio_delete(widget_id)

Delete assigned audio widget

Delete assigned audio widget from specified widget ID

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
widget_id = 56 # int | Id of a widget from which you want to delete the audio from

try:
    # Delete assigned audio widget
    api_instance.widget_audio_delete(widget_id)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_audio_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_id** | **int**| Id of a widget from which you want to delete the audio from | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_audio_edit**
> Widget widget_audio_edit(use_duration=use_duration, duration=duration, name=name, mute=mute, loop=loop)

Parameters for editing existing audio widget on a layout

Parameters for editing existing audio widget on a layout, for adding new audio, please refer to POST /library documentation

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
use_duration = 56 # int | Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well (optional)
duration = 56 # int | Edit Only - The Widget Duration (optional)
name = 'name_example' # str | Edit Only - The Widget name (optional)
mute = 56 # int | Edit only - Flag (0, 1) Should the audio be muted? (optional)
loop = 56 # int | Edit only - Flag (0, 1) Should the audio loop (only for duration > 0 )? (optional)

try:
    # Parameters for editing existing audio widget on a layout
    api_response = api_instance.widget_audio_edit(use_duration=use_duration, duration=duration, name=name, mute=mute, loop=loop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_audio_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_duration** | **int**| Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **duration** | **int**| Edit Only - The Widget Duration | [optional] 
 **name** | **str**| Edit Only - The Widget name | [optional] 
 **mute** | **int**| Edit only - Flag (0, 1) Should the audio be muted? | [optional] 
 **loop** | **int**| Edit only - Flag (0, 1) Should the audio loop (only for duration &gt; 0 )? | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_chart_add**
> Widget widget_chart_add(playlist_id, data_set_id, graph_type, name=name, column_type=column_type, data_set_column_id=data_set_column_id, duration=duration, use_duration=use_duration, update_interval=update_interval, filter=filter, ordering=ordering, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, background_color=background_color, font_color=font_color, font_size=font_size, show_legend=show_legend, legend_position=legend_position, start_y_at_zero=start_y_at_zero, title=title, x_axis_label=x_axis_label, y_axis_label=y_axis_label)

Add a Chart Widget

Add a new Chart Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
data_set_id = 56 # int | Create Chart Widget using provided dataSetId of an existing dataSet
graph_type = 'graph_type_example' # str | EDIT only - Chart Type
name = 'name_example' # str | Optional Widget Name (optional)
column_type = [56] # list[int] | EDIT only - Array of Column Types (x-axis, y-axis, series-identifier) to assign (optional)
data_set_column_id = [56] # list[int] | EDIT only - Array of dataSetColumn IDs to assign (optional)
duration = 56 # int | EDIT Only - The Chart Duration (optional)
use_duration = 56 # int | Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well (optional)
update_interval = 56 # int | EDIT Only - Update interval in minutes (optional)
filter = 'filter_example' # str | EDIT Only - SQL clause for filter this dataSet (optional)
ordering = 'ordering_example' # str | EDIT Only - SQL clause for how this dataSet should be ordered (optional)
use_ordering_clause = 56 # int | EDIT Only - flag (0,1) Use advanced order clause - set to 1 if ordering is provided (optional)
use_filtering_clause = 56 # int | EDIT Only - flag (0,1) Use advanced filter clause - set to 1 if filter is provided (optional)
background_color = 'background_color_example' # str | EDIT Only - Background Color (optional)
font_color = 'font_color_example' # str | EDIT Only - Font Color (optional)
font_size = 56 # int | EDIT Only - Font Size (optional)
show_legend = 56 # int | EDIT Only - Should the Legend be Shown (optional)
legend_position = 'legend_position_example' # str | EDIT Only - Where should the Legend be Shown (top, left, right, bottom) (optional)
start_y_at_zero = 56 # int | EDIT Only - Start the Y-Axis at 0 (optional)
title = 'title_example' # str | EDIT Only - Chart title (optional)
x_axis_label = 'x_axis_label_example' # str | EDIT Only - Chart x-axis label (optional)
y_axis_label = 'y_axis_label_example' # str | EDIT Only - Chart y-axis label (optional)

try:
    # Add a Chart Widget
    api_response = api_instance.widget_chart_add(playlist_id, data_set_id, graph_type, name=name, column_type=column_type, data_set_column_id=data_set_column_id, duration=duration, use_duration=use_duration, update_interval=update_interval, filter=filter, ordering=ordering, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, background_color=background_color, font_color=font_color, font_size=font_size, show_legend=show_legend, legend_position=legend_position, start_y_at_zero=start_y_at_zero, title=title, x_axis_label=x_axis_label, y_axis_label=y_axis_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_chart_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **data_set_id** | **int**| Create Chart Widget using provided dataSetId of an existing dataSet | 
 **graph_type** | **str**| EDIT only - Chart Type | 
 **name** | **str**| Optional Widget Name | [optional] 
 **column_type** | [**list[int]**](int.md)| EDIT only - Array of Column Types (x-axis, y-axis, series-identifier) to assign | [optional] 
 **data_set_column_id** | [**list[int]**](int.md)| EDIT only - Array of dataSetColumn IDs to assign | [optional] 
 **duration** | **int**| EDIT Only - The Chart Duration | [optional] 
 **use_duration** | **int**| Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **update_interval** | **int**| EDIT Only - Update interval in minutes | [optional] 
 **filter** | **str**| EDIT Only - SQL clause for filter this dataSet | [optional] 
 **ordering** | **str**| EDIT Only - SQL clause for how this dataSet should be ordered | [optional] 
 **use_ordering_clause** | **int**| EDIT Only - flag (0,1) Use advanced order clause - set to 1 if ordering is provided | [optional] 
 **use_filtering_clause** | **int**| EDIT Only - flag (0,1) Use advanced filter clause - set to 1 if filter is provided | [optional] 
 **background_color** | **str**| EDIT Only - Background Color | [optional] 
 **font_color** | **str**| EDIT Only - Font Color | [optional] 
 **font_size** | **int**| EDIT Only - Font Size | [optional] 
 **show_legend** | **int**| EDIT Only - Should the Legend be Shown | [optional] 
 **legend_position** | **str**| EDIT Only - Where should the Legend be Shown (top, left, right, bottom) | [optional] 
 **start_y_at_zero** | **int**| EDIT Only - Start the Y-Axis at 0 | [optional] 
 **title** | **str**| EDIT Only - Chart title | [optional] 
 **x_axis_label** | **str**| EDIT Only - Chart x-axis label | [optional] 
 **y_axis_label** | **str**| EDIT Only - Chart y-axis label | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_clock_add**
> Widget widget_clock_add(playlist_id, name=name, duration=duration, use_duration=use_duration, theme_id=theme_id, clock_type_id=clock_type_id, offset=offset, format=format, show_seconds=show_seconds, clock_face=clock_face)

Add a Clock Widget

Add a new Clock Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Clock widget to
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
theme_id = 56 # int | Flag (0 , 1) for Analogue clock the light and dark theme (optional)
clock_type_id = 56 # int | Type of a clock widget 1-Analogue, 2-Digital, 3-Flip clock (optional)
offset = 'offset_example' # str | The offset in minutes that should be applied to the current time, if a counter is selected then date/time to run from in the format Y-m-d H:i:s (optional)
format = 'format_example' # str | For digital clock, format in which the time should be displayed example [HH:mm] (optional)
show_seconds = 56 # int | For Flip Clock, should the clock show seconds or not (optional)
clock_face = 'clock_face_example' # str | For Flip Clock, supported options: TwelveHourClock TwentyFourHourClock HourlyCounter MinuteCounter DailyCounter (optional)

try:
    # Add a Clock Widget
    api_response = api_instance.widget_clock_add(playlist_id, name=name, duration=duration, use_duration=use_duration, theme_id=theme_id, clock_type_id=clock_type_id, offset=offset, format=format, show_seconds=show_seconds, clock_face=clock_face)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_clock_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Clock widget to | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **theme_id** | **int**| Flag (0 , 1) for Analogue clock the light and dark theme | [optional] 
 **clock_type_id** | **int**| Type of a clock widget 1-Analogue, 2-Digital, 3-Flip clock | [optional] 
 **offset** | **str**| The offset in minutes that should be applied to the current time, if a counter is selected then date/time to run from in the format Y-m-d H:i:s | [optional] 
 **format** | **str**| For digital clock, format in which the time should be displayed example [HH:mm] | [optional] 
 **show_seconds** | **int**| For Flip Clock, should the clock show seconds or not | [optional] 
 **clock_face** | **str**| For Flip Clock, supported options: TwelveHourClock TwentyFourHourClock HourlyCounter MinuteCounter DailyCounter | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_currencies_add**
> Widget widget_currencies_add(playlist_id, base, items, name=name, duration=duration, use_duration=use_duration, reverse_conversion=reverse_conversion, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, duration_is_per_page=duration_is_per_page, template_id=template_id, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, max_items_per_page=max_items_per_page, main_template=main_template, itemtemplate=itemtemplate, style_sheet=style_sheet, java_script=java_script)

Add a Currencies Widget

Add a new Currencies Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Currencies widget
base = 'base_example' # str | The base currency
items = 'items_example' # str | Items wanted
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
reverse_conversion = 56 # int | (0, 1) Select 1 if you'd like your base currency to be used as the comparison currency you've entered (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) (optional)
background_color = 'background_color_example' # str | A HEX color to use as the background color of this widget (optional)
no_records_message = 'no_records_message_example' # str | A message to display when there are no records returned by the search query (optional)
date_format = 'date_format_example' # str | The format to apply to all dates returned by he widget (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
duration_is_per_page = 56 # int | A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items (optional)
template_id = 'template_id_example' # str | Use pre-configured templates, available options: currencies1, currencies2 (optional)
override_template = 56 # int | flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters (optional)
widget_original_width = 56 # int | This is the intended Width of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
widget_original_height = 56 # int | This is the intended Height of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
max_items_per_page = 56 # int | This is the intended number of items on each page (optional)
main_template = 'main_template_example' # str | Main template, Pass only with overrideTemplate set to 1  (optional)
itemtemplate = 'itemtemplate_example' # str | Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1  (optional)
style_sheet = 'style_sheet_example' # str | Optional StyleSheet Pass only with overrideTemplate set to 1  (optional)
java_script = 'java_script_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)

try:
    # Add a Currencies Widget
    api_response = api_instance.widget_currencies_add(playlist_id, base, items, name=name, duration=duration, use_duration=use_duration, reverse_conversion=reverse_conversion, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, duration_is_per_page=duration_is_per_page, template_id=template_id, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, max_items_per_page=max_items_per_page, main_template=main_template, itemtemplate=itemtemplate, style_sheet=style_sheet, java_script=java_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_currencies_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Currencies widget | 
 **base** | **str**| The base currency | 
 **items** | **str**| Items wanted | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **reverse_conversion** | **int**| (0, 1) Select 1 if you&#39;d like your base currency to be used as the comparison currency you&#39;ve entered | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) | [optional] 
 **background_color** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **no_records_message** | **str**| A message to display when there are no records returned by the search query | [optional] 
 **date_format** | **str**| The format to apply to all dates returned by he widget | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **duration_is_per_page** | **int**| A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items | [optional] 
 **template_id** | **str**| Use pre-configured templates, available options: currencies1, currencies2 | [optional] 
 **override_template** | **int**| flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters | [optional] 
 **widget_original_width** | **int**| This is the intended Width of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **widget_original_height** | **int**| This is the intended Height of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **max_items_per_page** | **int**| This is the intended number of items on each page | [optional] 
 **main_template** | **str**| Main template, Pass only with overrideTemplate set to 1  | [optional] 
 **itemtemplate** | **str**| Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet** | **str**| Optional StyleSheet Pass only with overrideTemplate set to 1  | [optional] 
 **java_script** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_delete**
> widget_delete(widget_id)

Delete a Widget

Deleted a specified widget

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
widget_id = 56 # int | The widget ID to delete

try:
    # Delete a Widget
    api_instance.widget_delete(widget_id)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_id** | **int**| The widget ID to delete | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_edit**
> Widget widget_edit(widget_id)

Edit a Widget

Edit a Widget, please refer to individual widget Add documentation for module specific parameters

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
widget_id = 56 # int | The widget ID to edit

try:
    # Edit a Widget
    api_response = api_instance.widget_edit(widget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_id** | **int**| The widget ID to edit | 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_edit_transition**
> Widget widget_edit_transition(type, widget_id, transition_type, transition_duration=transition_duration, transition_direction=transition_direction)

Adds In/Out transition

Adds In/Out transition to a specified widget

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Transition type, available options: in, out
widget_id = 56 # int | The widget ID to add the transition to
transition_type = 'transition_type_example' # str | Type of a transition, available Options: fly, fadeIn, fadeOut
transition_duration = 56 # int | Duration of this transition in milliseconds (optional)
transition_direction = 56 # int | The direction for this transition, only appropriate for transitions that move, such as fly. Available options: N, NE, E, SE, S, SW, W, NW (optional)

try:
    # Adds In/Out transition
    api_response = api_instance.widget_edit_transition(type, widget_id, transition_type, transition_duration=transition_duration, transition_direction=transition_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_edit_transition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Transition type, available options: in, out | 
 **widget_id** | **int**| The widget ID to add the transition to | 
 **transition_type** | **str**| Type of a transition, available Options: fly, fadeIn, fadeOut | 
 **transition_duration** | **int**| Duration of this transition in milliseconds | [optional] 
 **transition_direction** | **int**| The direction for this transition, only appropriate for transitions that move, such as fly. Available options: N, NE, E, SE, S, SW, W, NW | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_embedded_add**
> Widget widget_embedded_add(playlist_id, name=name, duration=duration, use_duration=use_duration, transparency=transparency, scale_content=scale_content, embed_html=embed_html, embed_script=embed_script, embed_style=embed_style)

Add a Embedded Widget

Add a new Embedded Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add an Embedded Widget
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
transparency = 56 # int | Flag (0,1) - Should the HTML be shown with transparent background? - not available on Windows Clients (optional)
scale_content = 56 # int | Flag (0,1) - Should the embedded content be scaled along with the layout? (optional)
embed_html = 'embed_html_example' # str | HTML to embed (optional)
embed_script = 'embed_script_example' # str | HEAD content to Embed (including script tags) (optional)
embed_style = 'embed_style_example' # str | Custom Style Sheets (CSS) (optional)

try:
    # Add a Embedded Widget
    api_response = api_instance.widget_embedded_add(playlist_id, name=name, duration=duration, use_duration=use_duration, transparency=transparency, scale_content=scale_content, embed_html=embed_html, embed_script=embed_script, embed_style=embed_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_embedded_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add an Embedded Widget | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **transparency** | **int**| Flag (0,1) - Should the HTML be shown with transparent background? - not available on Windows Clients | [optional] 
 **scale_content** | **int**| Flag (0,1) - Should the embedded content be scaled along with the layout? | [optional] 
 **embed_html** | **str**| HTML to embed | [optional] 
 **embed_script** | **str**| HEAD content to Embed (including script tags) | [optional] 
 **embed_style** | **str**| Custom Style Sheets (CSS) | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_finance_add**
> Widget widget_finance_add(playlist_id, item, yql, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, template_id=template_id, duration_is_per_item=duration_is_per_item, override_template=override_template, result_identifier=result_identifier, template=template, style_sheet=style_sheet, java_script=java_script)

Add a Finance Widget

Add a new Finance Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Finance widget
item = 'item_example' # str | Items wanted, can be comma separated (example EURUSD, GBPUSD), pass only with overrideTemplate set to 1
yql = 'yql_example' # str | The YQL query to use for data, pass only with overrideTemplate set to 1
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) or the Marquee speed in a low to high scale (normal = 1) (optional)
background_color = 'background_color_example' # str | A HEX color to use as the background color of this widget (optional)
no_records_message = 'no_records_message_example' # str | A message to display when there are no records returned by the search query (optional)
date_format = 'date_format_example' # str | The format to apply to all dates returned by he widget (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
template_id = 'template_id_example' # str | Use pre-configured templates, available options: currency-simple, stock-simple (optional)
duration_is_per_item = 56 # int | A flag (0, 1), The duration specified is per item, otherwise the widget duration is divided between the number of items (optional)
override_template = 56 # int | flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters (optional)
result_identifier = 'result_identifier_example' # str | The name of the result identifier returned by the YQL, pass only with overrideTemplate set to 1 (optional)
template = 'template_example' # str | Main template, Pass only with overrideTemplate set to 1  (optional)
style_sheet = 'style_sheet_example' # str | Optional StyleSheet Pass only with overrideTemplate set to 1  (optional)
java_script = 'java_script_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)

try:
    # Add a Finance Widget
    api_response = api_instance.widget_finance_add(playlist_id, item, yql, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, template_id=template_id, duration_is_per_item=duration_is_per_item, override_template=override_template, result_identifier=result_identifier, template=template, style_sheet=style_sheet, java_script=java_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_finance_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Finance widget | 
 **item** | **str**| Items wanted, can be comma separated (example EURUSD, GBPUSD), pass only with overrideTemplate set to 1 | 
 **yql** | **str**| The YQL query to use for data, pass only with overrideTemplate set to 1 | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) or the Marquee speed in a low to high scale (normal &#x3D; 1) | [optional] 
 **background_color** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **no_records_message** | **str**| A message to display when there are no records returned by the search query | [optional] 
 **date_format** | **str**| The format to apply to all dates returned by he widget | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **template_id** | **str**| Use pre-configured templates, available options: currency-simple, stock-simple | [optional] 
 **duration_is_per_item** | **int**| A flag (0, 1), The duration specified is per item, otherwise the widget duration is divided between the number of items | [optional] 
 **override_template** | **int**| flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters | [optional] 
 **result_identifier** | **str**| The name of the result identifier returned by the YQL, pass only with overrideTemplate set to 1 | [optional] 
 **template** | **str**| Main template, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet** | **str**| Optional StyleSheet Pass only with overrideTemplate set to 1  | [optional] 
 **java_script** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_google_traffic_add**
> Widget widget_google_traffic_add(playlist_id, zoom, use_display_location, name=name, duration=duration, use_duration=use_duration, longitude=longitude, latitude=latitude)

Add a Google Traffic Widget

Add a new Google traffic Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget
zoom = 56 # int | How far should the map be zoomed in? The higher the number the closer the zoom, 1 represents entire globe
use_display_location = 56 # int | Flag (0, 1) Use the location configured on display
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
longitude = 8.14 # float | The longitude for this weather widget, only pass if useDisplayLocation set to 0 (optional)
latitude = 8.14 # float | The latitude for this weather widget, only pass if useDisplayLocation set to 0 (optional)

try:
    # Add a Google Traffic Widget
    api_response = api_instance.widget_google_traffic_add(playlist_id, zoom, use_display_location, name=name, duration=duration, use_duration=use_duration, longitude=longitude, latitude=latitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_google_traffic_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget | 
 **zoom** | **int**| How far should the map be zoomed in? The higher the number the closer the zoom, 1 represents entire globe | 
 **use_display_location** | **int**| Flag (0, 1) Use the location configured on display | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **longitude** | **float**| The longitude for this weather widget, only pass if useDisplayLocation set to 0 | [optional] 
 **latitude** | **float**| The latitude for this weather widget, only pass if useDisplayLocation set to 0 | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_hls_add**
> Widget widget_hls_add(playlist_id, uri, name=name, use_duration=use_duration, duration=duration, mute=mute, transparency=transparency)

Add a HLS Widget

Add a new HLS Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
uri = 'uri_example' # str | URL to HLS video stream
name = 'name_example' # str | Optional Widget Name (optional)
use_duration = 56 # int | Edit Only - (0, 1) Select only if you will provide duration parameter as well (optional)
duration = 56 # int | The Widget Duration (optional)
mute = 56 # int | Flag (0, 1) Should the video be muted? (optional)
transparency = 56 # int | Flag (0, 1), This causes some android devices to switch to a hardware accelerated web view (optional)

try:
    # Add a HLS Widget
    api_response = api_instance.widget_hls_add(playlist_id, uri, name=name, use_duration=use_duration, duration=duration, mute=mute, transparency=transparency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_hls_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **uri** | **str**| URL to HLS video stream | 
 **name** | **str**| Optional Widget Name | [optional] 
 **use_duration** | **int**| Edit Only - (0, 1) Select only if you will provide duration parameter as well | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **mute** | **int**| Flag (0, 1) Should the video be muted? | [optional] 
 **transparency** | **int**| Flag (0, 1), This causes some android devices to switch to a hardware accelerated web view | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_image_edit**
> Widget widget_image_edit(name=name, duration=duration, use_duration=use_duration, scale_type_id=scale_type_id, align_id=align_id, valign_id=valign_id)

Parameters for editing existing image on a layout

Parameters for editing existing image on a layout, for adding new images, please refer to POST /library documentation

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Edit only - Optional Widget Name (optional)
duration = 56 # int | Edit Only - The Widget Duration (optional)
use_duration = 56 # int | Edit only (0, 1) Select 1 only if you will provide duration parameter as well (optional)
scale_type_id = 'scale_type_id_example' # str | Edit only - Select scale type available options: center, stretch (optional)
align_id = 'align_id_example' # str | Edit only - Horizontal alignment - left, center, bottom (optional)
valign_id = 'valign_id_example' # str | Edit only - Vertical alignment - top, middle, bottom (optional)

try:
    # Parameters for editing existing image on a layout
    api_response = api_instance.widget_image_edit(name=name, duration=duration, use_duration=use_duration, scale_type_id=scale_type_id, align_id=align_id, valign_id=valign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_image_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Edit only - Optional Widget Name | [optional] 
 **duration** | **int**| Edit Only - The Widget Duration | [optional] 
 **use_duration** | **int**| Edit only (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **scale_type_id** | **str**| Edit only - Select scale type available options: center, stretch | [optional] 
 **align_id** | **str**| Edit only - Horizontal alignment - left, center, bottom | [optional] 
 **valign_id** | **str**| Edit only - Vertical alignment - top, middle, bottom | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_local_video_add**
> Widget widget_local_video_add(playlist_id, uri, duration=duration, use_duration=use_duration, scale_type_id=scale_type_id, mute=mute)

Add a Local Video Widget

Add a new Local Video Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
uri = 'uri_example' # str | A local file path or URL to the video. This can be RTSP stream.
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
scale_type_id = 'scale_type_id_example' # str | How should the video be scaled, available options: aspect, stretch (optional)
mute = 56 # int | Flag (0, 1) Should the video be muted? (optional)

try:
    # Add a Local Video Widget
    api_response = api_instance.widget_local_video_add(playlist_id, uri, duration=duration, use_duration=use_duration, scale_type_id=scale_type_id, mute=mute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_local_video_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **uri** | **str**| A local file path or URL to the video. This can be RTSP stream. | 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **scale_type_id** | **str**| How should the video be scaled, available options: aspect, stretch | [optional] 
 **mute** | **int**| Flag (0, 1) Should the video be muted? | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_notification_add**
> Widget widget_notification_add(playlist_id, age, name=name, duration=duration, use_duration=use_duration, no_data_message=no_data_message, effect=effect, speed=speed, duration_is_per_item=duration_is_per_item, embed_style=embed_style)

Add a Notification Widget

Add a new Notification Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add an Notification Widget
age = 56 # int | The maximum notification age in minutes - 0 for all
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
no_data_message = 'no_data_message_example' # str | Message to show when no notifications are available (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) (optional)
duration_is_per_item = 56 # int | A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items (optional)
embed_style = 'embed_style_example' # str | Custom Style Sheets (CSS) (optional)

try:
    # Add a Notification Widget
    api_response = api_instance.widget_notification_add(playlist_id, age, name=name, duration=duration, use_duration=use_duration, no_data_message=no_data_message, effect=effect, speed=speed, duration_is_per_item=duration_is_per_item, embed_style=embed_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_notification_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add an Notification Widget | 
 **age** | **int**| The maximum notification age in minutes - 0 for all | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **no_data_message** | **str**| Message to show when no notifications are available | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) | [optional] 
 **duration_is_per_item** | **int**| A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items | [optional] 
 **embed_style** | **str**| Custom Style Sheets (CSS) | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_pdf_edit**
> Widget widget_pdf_edit(name=name, use_duration=use_duration, duration=duration)

Parameters for editing existing pdf on a layout

Parameters for editing existing pdf on a layout, for adding new files, please refer to POST /library documentation

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Edit only - Optional Widget Name (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
duration = 56 # int | Edit Only - The Widget Duration (optional)

try:
    # Parameters for editing existing pdf on a layout
    api_response = api_instance.widget_pdf_edit(name=name, use_duration=use_duration, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_pdf_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Edit only - Optional Widget Name | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **duration** | **int**| Edit Only - The Widget Duration | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_shell_command_add**
> Widget widget_shell_command_add(playlist_id, name=name, duration=duration, use_duration=use_duration, windows_command=windows_command, linux_command=linux_command, launch_through_cmd=launch_through_cmd, terminate_command=terminate_command, use_taskkill=use_taskkill, command_code=command_code)

Add a Shell Command Widget

Add a new Shell Command Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
windows_command = 'windows_command_example' # str | Enter a Windows command line compatible command (optional)
linux_command = 'linux_command_example' # str | Enter a Android / Linux command line compatible command (optional)
launch_through_cmd = 56 # int | flag (0,1) Windows only, Should the player launch this command through the windows command line (cmd.exe)? This is useful for batch files, if you try to terminate this command only the command line will be terminated (optional)
terminate_command = 56 # int | flag (0,1) Should the player forcefully terminate the command after the duration specified, 0 to let the command terminate naturally (optional)
use_taskkill = 56 # int | flag (0,1) Windows only, should the player use taskkill to terminate commands (optional)
command_code = 'command_code_example' # str | Enter a reference code for exiting command in CMS (optional)

try:
    # Add a Shell Command Widget
    api_response = api_instance.widget_shell_command_add(playlist_id, name=name, duration=duration, use_duration=use_duration, windows_command=windows_command, linux_command=linux_command, launch_through_cmd=launch_through_cmd, terminate_command=terminate_command, use_taskkill=use_taskkill, command_code=command_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_shell_command_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **windows_command** | **str**| Enter a Windows command line compatible command | [optional] 
 **linux_command** | **str**| Enter a Android / Linux command line compatible command | [optional] 
 **launch_through_cmd** | **int**| flag (0,1) Windows only, Should the player launch this command through the windows command line (cmd.exe)? This is useful for batch files, if you try to terminate this command only the command line will be terminated | [optional] 
 **terminate_command** | **int**| flag (0,1) Should the player forcefully terminate the command after the duration specified, 0 to let the command terminate naturally | [optional] 
 **use_taskkill** | **int**| flag (0,1) Windows only, should the player use taskkill to terminate commands | [optional] 
 **command_code** | **str**| Enter a reference code for exiting command in CMS | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_stocks_add**
> Widget widget_stocks_add(playlist_id, items, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, template_id=template_id, duration_is_per_page=duration_is_per_page, override_template=override_template, max_items_per_page=max_items_per_page, main_template=main_template, itemtemplate=itemtemplate, style_sheet=style_sheet, java_script=java_script)

Add a Stocks Widget

Add a new Stocks Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Stocks widget
items = 'items_example' # str | Items wanted, can be comma separated
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) (optional)
background_color = 'background_color_example' # str | A HEX color to use as the background color of this widget (optional)
no_records_message = 'no_records_message_example' # str | A message to display when there are no records returned by the search query (optional)
date_format = 'date_format_example' # str | The format to apply to all dates returned by he widget (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
template_id = 'template_id_example' # str | Use pre-configured templates, available options: stocks1, stocks2 (optional)
duration_is_per_page = 56 # int | A flag (0, 1), The duration specified is per page, otherwise the widget duration is divided between the number of pages/items (optional)
override_template = 56 # int | flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters (optional)
max_items_per_page = 56 # int | This is the intended number of items on each page (optional)
main_template = 'main_template_example' # str | Main template, Pass only with overrideTemplate set to 1 (optional)
itemtemplate = 'itemtemplate_example' # str | Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1  (optional)
style_sheet = 'style_sheet_example' # str | Optional StyleSheet Pass only with overrideTemplate set to 1  (optional)
java_script = 'java_script_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)

try:
    # Add a Stocks Widget
    api_response = api_instance.widget_stocks_add(playlist_id, items, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, background_color=background_color, no_records_message=no_records_message, date_format=date_format, update_interval=update_interval, template_id=template_id, duration_is_per_page=duration_is_per_page, override_template=override_template, max_items_per_page=max_items_per_page, main_template=main_template, itemtemplate=itemtemplate, style_sheet=style_sheet, java_script=java_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_stocks_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Stocks widget | 
 **items** | **str**| Items wanted, can be comma separated | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) | [optional] 
 **background_color** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **no_records_message** | **str**| A message to display when there are no records returned by the search query | [optional] 
 **date_format** | **str**| The format to apply to all dates returned by he widget | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **template_id** | **str**| Use pre-configured templates, available options: stocks1, stocks2 | [optional] 
 **duration_is_per_page** | **int**| A flag (0, 1), The duration specified is per page, otherwise the widget duration is divided between the number of pages/items | [optional] 
 **override_template** | **int**| flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters | [optional] 
 **max_items_per_page** | **int**| This is the intended number of items on each page | [optional] 
 **main_template** | **str**| Main template, Pass only with overrideTemplate set to 1 | [optional] 
 **itemtemplate** | **str**| Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet** | **str**| Optional StyleSheet Pass only with overrideTemplate set to 1  | [optional] 
 **java_script** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_text_add**
> Widget widget_text_add(playlist_id, text, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, backgroundcolor=backgroundcolor, marquee_inline_selector=marquee_inline_selector, java_script=java_script)

Add a Text Widget

Add a new Text Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
text = 'text_example' # str | Enter the text to display
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) or the Marquee speed in a low to high scale (normal = 1) (optional)
backgroundcolor = 'backgroundcolor_example' # str | A HEX color to use as the background color of this widget (optional)
marquee_inline_selector = 'marquee_inline_selector_example' # str | The selector to use for stacking marquee items in a line when scrolling left/right (optional)
java_script = 'java_script_example' # str | Optional JavaScript (optional)

try:
    # Add a Text Widget
    api_response = api_instance.widget_text_add(playlist_id, text, name=name, duration=duration, use_duration=use_duration, effect=effect, speed=speed, backgroundcolor=backgroundcolor, marquee_inline_selector=marquee_inline_selector, java_script=java_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_text_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **text** | **str**| Enter the text to display | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) or the Marquee speed in a low to high scale (normal &#x3D; 1) | [optional] 
 **backgroundcolor** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **marquee_inline_selector** | **str**| The selector to use for stacking marquee items in a line when scrolling left/right | [optional] 
 **java_script** | **str**| Optional JavaScript | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_ticker_add**
> Widget widget_ticker_add(playlist_id, source_id, uri, data_set_id, name=name, duration=duration, use_duration=use_duration, update_interval=update_interval, effect=effect, speed=speed, copyright=copyright, num_items=num_items, take_items_from=take_items_from, duration_is_per_item=duration_is_per_item, items_side_by_side=items_side_by_side, upper_limit=upper_limit, lower_limit=lower_limit, items_per_page=items_per_page, date_format=date_format, allowed_attributes=allowed_attributes, strip_tags=strip_tags, background_color=background_color, disable_date_sort=disable_date_sort, text_direction=text_direction, no_data_message=no_data_message, template_id=template_id, override_template=override_template, template=template, css=css, java_script=java_script, filter=filter, ordering=ordering, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, randomise_items=randomise_items)

Add a ticker Widget

Add a new ticker Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
source_id = 56 # int | Add only - 1 for rss feed, 2 for dataset
uri = 'uri_example' # str | For sourceId=1, the link for the rss feed
data_set_id = 56 # int | For sourceId=2, Create ticker Widget using provided dataSetId of an existing dataSet
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
update_interval = 56 # int | EDIT Only - Update interval in minutes (optional)
effect = 'effect_example' # str | Edit only - Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft (optional)
speed = 56 # int | Edit only - The transition speed of the selected effect in milliseconds (1000 = normal) or the Marquee speed in a low to high scale (normal = 1) (optional)
copyright = 'copyright_example' # str | EDIT Only and SourceId=1 - Copyright information to display as the last item in this feed. can be styled with the #copyright CSS selector (optional)
num_items = 56 # int | EDIT Only and SourceId=1 - The number of RSS items you want to display (optional)
take_items_from = 'take_items_from_example' # str | EDIT Only and SourceId=1 - Take the items form the beginning or the end of the list, available options: start, end (optional)
duration_is_per_item = 56 # int | A flag (0, 1), The duration specified is per item, otherwise it is per feed (optional)
items_side_by_side = 56 # int | A flag (0, 1), Should items be shown side by side (optional)
upper_limit = 56 # int | EDIT Only, SourceId=2 - Upper low limit for this dataSet, 0 for nor limit (optional)
lower_limit = 56 # int | EDIT Only, SourceId=2 - Lower low limit for this dataSet, 0 for nor limit (optional)
items_per_page = 56 # int | EDIT Only - When in single mode, how many items per page should be shown (optional)
date_format = 'date_format_example' # str | EDIT Only - The date format to apply to all dates returned by the ticker (optional)
allowed_attributes = 'allowed_attributes_example' # str | EDIT Only and SourceId=1 - A comma separated list of attributes that should not be stripped from the feed (optional)
strip_tags = 'strip_tags_example' # str | EDIT Only and SourceId=1 - A comma separated list of attributes that should be stripped from the feed (optional)
background_color = 'background_color_example' # str | Edit only - A HEX color to use as the background color of this widget (optional)
disable_date_sort = 56 # int | EDIT Only, SourceId=1 - Should the date sort applied to the feed be disabled? (optional)
text_direction = 'text_direction_example' # str | EDIT Only, SourceId=1 - Which direction does the text in the feed use? Available options: ltr, rtl (optional)
no_data_message = 'no_data_message_example' # str | EDIT Only - A message to display when no data is returned from the source (optional)
template_id = 'template_id_example' # str | EDIT Only, SourceId=1 - Template you'd like to apply, options available: title-only, prominent-title-with-desc-and-name-separator, media-rss-with-title, media-rss-wth-left-hand-text, media-rss-image-only (optional)
override_template = 56 # int | EDIT Only, SourceId=1 - flag (0, 1) override template checkbox (optional)
template = 'template_example' # str | Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1 or with sourceId=2  (optional)
css = 'css_example' # str | Optional StyleSheet Pass only with overrideTemplate set to 1 or with sourceId=2  (optional)
java_script = 'java_script_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)
filter = 'filter_example' # str | EDIT Only, SourceId=2 - SQL clause for filter this dataSet (optional)
ordering = 'ordering_example' # str | EDIT Only, SourceId=2- SQL clause for how this dataSet should be ordered (optional)
use_ordering_clause = 56 # int | EDIT Only, SourceId=2 - flag (0,1) Use advanced order clause - set to 1 if ordering is provided (optional)
use_filtering_clause = 56 # int | EDIT Only, SourceId=2 - flag (0,1) Use advanced filter clause - set to 1 if filter is provided (optional)
randomise_items = 56 # int | A flag (0, 1), whether to randomise the feed (optional)

try:
    # Add a ticker Widget
    api_response = api_instance.widget_ticker_add(playlist_id, source_id, uri, data_set_id, name=name, duration=duration, use_duration=use_duration, update_interval=update_interval, effect=effect, speed=speed, copyright=copyright, num_items=num_items, take_items_from=take_items_from, duration_is_per_item=duration_is_per_item, items_side_by_side=items_side_by_side, upper_limit=upper_limit, lower_limit=lower_limit, items_per_page=items_per_page, date_format=date_format, allowed_attributes=allowed_attributes, strip_tags=strip_tags, background_color=background_color, disable_date_sort=disable_date_sort, text_direction=text_direction, no_data_message=no_data_message, template_id=template_id, override_template=override_template, template=template, css=css, java_script=java_script, filter=filter, ordering=ordering, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, randomise_items=randomise_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_ticker_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **source_id** | **int**| Add only - 1 for rss feed, 2 for dataset | 
 **uri** | **str**| For sourceId&#x3D;1, the link for the rss feed | 
 **data_set_id** | **int**| For sourceId&#x3D;2, Create ticker Widget using provided dataSetId of an existing dataSet | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **update_interval** | **int**| EDIT Only - Update interval in minutes | [optional] 
 **effect** | **str**| Edit only - Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind, marqueeUp, marqueeDown, marqueeRight, marqueeLeft | [optional] 
 **speed** | **int**| Edit only - The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) or the Marquee speed in a low to high scale (normal &#x3D; 1) | [optional] 
 **copyright** | **str**| EDIT Only and SourceId&#x3D;1 - Copyright information to display as the last item in this feed. can be styled with the #copyright CSS selector | [optional] 
 **num_items** | **int**| EDIT Only and SourceId&#x3D;1 - The number of RSS items you want to display | [optional] 
 **take_items_from** | **str**| EDIT Only and SourceId&#x3D;1 - Take the items form the beginning or the end of the list, available options: start, end | [optional] 
 **duration_is_per_item** | **int**| A flag (0, 1), The duration specified is per item, otherwise it is per feed | [optional] 
 **items_side_by_side** | **int**| A flag (0, 1), Should items be shown side by side | [optional] 
 **upper_limit** | **int**| EDIT Only, SourceId&#x3D;2 - Upper low limit for this dataSet, 0 for nor limit | [optional] 
 **lower_limit** | **int**| EDIT Only, SourceId&#x3D;2 - Lower low limit for this dataSet, 0 for nor limit | [optional] 
 **items_per_page** | **int**| EDIT Only - When in single mode, how many items per page should be shown | [optional] 
 **date_format** | **str**| EDIT Only - The date format to apply to all dates returned by the ticker | [optional] 
 **allowed_attributes** | **str**| EDIT Only and SourceId&#x3D;1 - A comma separated list of attributes that should not be stripped from the feed | [optional] 
 **strip_tags** | **str**| EDIT Only and SourceId&#x3D;1 - A comma separated list of attributes that should be stripped from the feed | [optional] 
 **background_color** | **str**| Edit only - A HEX color to use as the background color of this widget | [optional] 
 **disable_date_sort** | **int**| EDIT Only, SourceId&#x3D;1 - Should the date sort applied to the feed be disabled? | [optional] 
 **text_direction** | **str**| EDIT Only, SourceId&#x3D;1 - Which direction does the text in the feed use? Available options: ltr, rtl | [optional] 
 **no_data_message** | **str**| EDIT Only - A message to display when no data is returned from the source | [optional] 
 **template_id** | **str**| EDIT Only, SourceId&#x3D;1 - Template you&#39;d like to apply, options available: title-only, prominent-title-with-desc-and-name-separator, media-rss-with-title, media-rss-wth-left-hand-text, media-rss-image-only | [optional] 
 **override_template** | **int**| EDIT Only, SourceId&#x3D;1 - flag (0, 1) override template checkbox | [optional] 
 **template** | **str**| Template for each item, replaces [itemsTemplate] in main template, Pass only with overrideTemplate set to 1 or with sourceId&#x3D;2  | [optional] 
 **css** | **str**| Optional StyleSheet Pass only with overrideTemplate set to 1 or with sourceId&#x3D;2  | [optional] 
 **java_script** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 
 **filter** | **str**| EDIT Only, SourceId&#x3D;2 - SQL clause for filter this dataSet | [optional] 
 **ordering** | **str**| EDIT Only, SourceId&#x3D;2- SQL clause for how this dataSet should be ordered | [optional] 
 **use_ordering_clause** | **int**| EDIT Only, SourceId&#x3D;2 - flag (0,1) Use advanced order clause - set to 1 if ordering is provided | [optional] 
 **use_filtering_clause** | **int**| EDIT Only, SourceId&#x3D;2 - flag (0,1) Use advanced filter clause - set to 1 if filter is provided | [optional] 
 **randomise_items** | **int**| A flag (0, 1), whether to randomise the feed | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_twitter_add**
> Widget widget_twitter_add(playlist_id, search_term, name=name, duration=duration, use_duration=use_duration, language=language, effect=effect, speed=speed, background_color=background_color, no_tweets_message=no_tweets_message, date_format=date_format, result_type=result_type, tweet_distance=tweet_distance, tweet_count=tweet_count, remove_urls=remove_urls, remove_mentions=remove_mentions, remove_hashtags=remove_hashtags, update_interval=update_interval, duration_is_per_item=duration_is_per_item, items_per_page=items_per_page, template_id=template_id, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, widget_original_padding=widget_original_padding, result_content=result_content, template=template, style_sheet=style_sheet, java_script=java_script)

Add a Twitter Widget

Add a new Twitter Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Twitter widget
search_term = 'search_term_example' # str | Twitter search term, you can test your search term in twitter.com search box first
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
language = 'language_example' # str | Language in which tweets should be returned (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) (optional)
background_color = 'background_color_example' # str | A HEX color to use as the background color of this widget (optional)
no_tweets_message = 'no_tweets_message_example' # str | A message to display when there are no tweets returned by the search query (optional)
date_format = 'date_format_example' # str | The format to apply to all dates returned by he widget (optional)
result_type = 'result_type_example' # str | 1 - Mixed, 2 -Recent 3 - Popular, Recent shows only recent tweets, Popular the most popular tweets and Mixed included both popular and recent (optional)
tweet_distance = 56 # int | Distance in miles that the tweets should be returned from. Set 0 for no restrictions (optional)
tweet_count = 56 # int | The number of tweets to return (optional)
remove_urls = 56 # int | Flag (0, 1) Should the URLs be removed from the tweet text? (optional)
remove_mentions = 56 # int | Flag (0, 1) Should mentions (@someone) be removed from the tweet text? (optional)
remove_hashtags = 56 # int | Flag (0, 1) Should the hashtags (#something) be removed from the tweet text (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
duration_is_per_item = 56 # int | A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items (optional)
items_per_page = 56 # int | EDIT Only - When in single mode, how many items per page should be shown (optional)
template_id = 'template_id_example' # str | Use pre-configured templates, available options: full-timeline-np, full-timeline, tweet-only, tweet-with-profileimage-left, tweet-with-profileimage-right, tweet-1, tweet-2, tweet-4. tweet-6NP, tweet-6PL, tweet-7, tweet-8 (optional)
override_template = 56 # int | flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters (optional)
widget_original_width = 56 # int | This is the intended Width of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
widget_original_height = 56 # int | This is the intended Height of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
widget_original_padding = 56 # int | This is the intended Padding of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
result_content = 'result_content_example' # str | Intended content Type, available Options: 0 - All Tweets 1 - Tweets with the text only content 2 - Tweets with the text and image content. Pass only with overrideTemplate set to 1 (optional)
template = 'template_example' # str | Main template, Pass only with overrideTemplate set to 1  (optional)
style_sheet = 'style_sheet_example' # str | Optional StyleSheet Pass only with overrideTemplate set to 1  (optional)
java_script = 'java_script_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)

try:
    # Add a Twitter Widget
    api_response = api_instance.widget_twitter_add(playlist_id, search_term, name=name, duration=duration, use_duration=use_duration, language=language, effect=effect, speed=speed, background_color=background_color, no_tweets_message=no_tweets_message, date_format=date_format, result_type=result_type, tweet_distance=tweet_distance, tweet_count=tweet_count, remove_urls=remove_urls, remove_mentions=remove_mentions, remove_hashtags=remove_hashtags, update_interval=update_interval, duration_is_per_item=duration_is_per_item, items_per_page=items_per_page, template_id=template_id, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, widget_original_padding=widget_original_padding, result_content=result_content, template=template, style_sheet=style_sheet, java_script=java_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_twitter_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Twitter widget | 
 **search_term** | **str**| Twitter search term, you can test your search term in twitter.com search box first | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **language** | **str**| Language in which tweets should be returned | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) | [optional] 
 **background_color** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **no_tweets_message** | **str**| A message to display when there are no tweets returned by the search query | [optional] 
 **date_format** | **str**| The format to apply to all dates returned by he widget | [optional] 
 **result_type** | **str**| 1 - Mixed, 2 -Recent 3 - Popular, Recent shows only recent tweets, Popular the most popular tweets and Mixed included both popular and recent | [optional] 
 **tweet_distance** | **int**| Distance in miles that the tweets should be returned from. Set 0 for no restrictions | [optional] 
 **tweet_count** | **int**| The number of tweets to return | [optional] 
 **remove_urls** | **int**| Flag (0, 1) Should the URLs be removed from the tweet text? | [optional] 
 **remove_mentions** | **int**| Flag (0, 1) Should mentions (@someone) be removed from the tweet text? | [optional] 
 **remove_hashtags** | **int**| Flag (0, 1) Should the hashtags (#something) be removed from the tweet text | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **duration_is_per_item** | **int**| A flag (0, 1), The duration specified is per page/item, otherwise the widget duration is divided between the number of pages/items | [optional] 
 **items_per_page** | **int**| EDIT Only - When in single mode, how many items per page should be shown | [optional] 
 **template_id** | **str**| Use pre-configured templates, available options: full-timeline-np, full-timeline, tweet-only, tweet-with-profileimage-left, tweet-with-profileimage-right, tweet-1, tweet-2, tweet-4. tweet-6NP, tweet-6PL, tweet-7, tweet-8 | [optional] 
 **override_template** | **int**| flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters | [optional] 
 **widget_original_width** | **int**| This is the intended Width of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **widget_original_height** | **int**| This is the intended Height of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **widget_original_padding** | **int**| This is the intended Padding of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **result_content** | **str**| Intended content Type, available Options: 0 - All Tweets 1 - Tweets with the text only content 2 - Tweets with the text and image content. Pass only with overrideTemplate set to 1 | [optional] 
 **template** | **str**| Main template, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet** | **str**| Optional StyleSheet Pass only with overrideTemplate set to 1  | [optional] 
 **java_script** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_twitter_metro_add**
> Widget widget_twitter_metro_add(playlist_id, search_term, name=name, duration=duration, use_duration=use_duration, language=language, effect=effect, speed=speed, background_color=background_color, no_tweets_message=no_tweets_message, date_format=date_format, result_type=result_type, tweet_distance=tweet_distance, tweet_count=tweet_count, remove_urls=remove_urls, remove_mentions=remove_mentions, remove_hashtags=remove_hashtags, update_interval=update_interval, color_template_id=color_template_id, override_color_template=override_color_template, template_colours=template_colours, result_content=result_content, remove_retweets=remove_retweets)

Add a Twitter Metro Widget

Add a new Twitter Metro Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Twitter Metro widget
search_term = 'search_term_example' # str | Twitter search term, you can test your search term in twitter.com search box first
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
language = 'language_example' # str | Language in which tweets should be returned (optional)
effect = 'effect_example' # str | Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  (optional)
speed = 56 # int | The transition speed of the selected effect in milliseconds (1000 = normal) (optional)
background_color = 'background_color_example' # str | A HEX color to use as the background color of this widget (optional)
no_tweets_message = 'no_tweets_message_example' # str | A message to display when there are no tweets returned by the search query (optional)
date_format = 'date_format_example' # str | The format to apply to all dates returned by he widget (optional)
result_type = 'result_type_example' # str | 1 - Mixed, 2 -Recent 3 - Popular, Recent shows only recent tweets, Popular the most popular tweets and Mixed included both popular and recent (optional)
tweet_distance = 56 # int | Distance in miles that the tweets should be returned from. Set 0 for no restrictions (optional)
tweet_count = 56 # int | The number of tweets to return (optional)
remove_urls = 56 # int | Flag (0, 1) Should the URLs be removed from the tweet text? (optional)
remove_mentions = 56 # int | Flag (0, 1) Should mentions (@someone) be removed from the tweet text? (optional)
remove_hashtags = 56 # int | Flag (0, 1) Should the hashtags (#something) be removed from the tweet text (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
color_template_id = 'color_template_id_example' # str | Use pre-configured templates, available options: default, full, gray, light, soft, vivid (optional)
override_color_template = 56 # int | flag (0, 1) set to 0 and use colorTemplateId or set to 1 and provide colours to use in templateColours parameter (optional)
template_colours = 'template_colours_example' # str | Provide a string of new HEX colour codes to use, separated by |, for example: #e0d2c8|#5e411d|#fccf12|#82ff00|#64bae8 (optional)
result_content = 'result_content_example' # str | Intended content Type, available Options: 0 - All Tweets 1 - Tweets with the text only content 2 - Tweets with the text and image content. Pass only with overrideColorTemplate set to 1 (optional)
remove_retweets = 56 # int | Flag (0, 1) Should retweets be filtered? (optional)

try:
    # Add a Twitter Metro Widget
    api_response = api_instance.widget_twitter_metro_add(playlist_id, search_term, name=name, duration=duration, use_duration=use_duration, language=language, effect=effect, speed=speed, background_color=background_color, no_tweets_message=no_tweets_message, date_format=date_format, result_type=result_type, tweet_distance=tweet_distance, tweet_count=tweet_count, remove_urls=remove_urls, remove_mentions=remove_mentions, remove_hashtags=remove_hashtags, update_interval=update_interval, color_template_id=color_template_id, override_color_template=override_color_template, template_colours=template_colours, result_content=result_content, remove_retweets=remove_retweets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_twitter_metro_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Twitter Metro widget | 
 **search_term** | **str**| Twitter search term, you can test your search term in twitter.com search box first | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **language** | **str**| Language in which tweets should be returned | [optional] 
 **effect** | **str**| Effect that will be used to transitions between items, available options: fade, fadeout, scrollVert, scollHorz, flipVert, flipHorz, shuffle, tileSlide, tileBlind  | [optional] 
 **speed** | **int**| The transition speed of the selected effect in milliseconds (1000 &#x3D; normal) | [optional] 
 **background_color** | **str**| A HEX color to use as the background color of this widget | [optional] 
 **no_tweets_message** | **str**| A message to display when there are no tweets returned by the search query | [optional] 
 **date_format** | **str**| The format to apply to all dates returned by he widget | [optional] 
 **result_type** | **str**| 1 - Mixed, 2 -Recent 3 - Popular, Recent shows only recent tweets, Popular the most popular tweets and Mixed included both popular and recent | [optional] 
 **tweet_distance** | **int**| Distance in miles that the tweets should be returned from. Set 0 for no restrictions | [optional] 
 **tweet_count** | **int**| The number of tweets to return | [optional] 
 **remove_urls** | **int**| Flag (0, 1) Should the URLs be removed from the tweet text? | [optional] 
 **remove_mentions** | **int**| Flag (0, 1) Should mentions (@someone) be removed from the tweet text? | [optional] 
 **remove_hashtags** | **int**| Flag (0, 1) Should the hashtags (#something) be removed from the tweet text | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **color_template_id** | **str**| Use pre-configured templates, available options: default, full, gray, light, soft, vivid | [optional] 
 **override_color_template** | **int**| flag (0, 1) set to 0 and use colorTemplateId or set to 1 and provide colours to use in templateColours parameter | [optional] 
 **template_colours** | **str**| Provide a string of new HEX colour codes to use, separated by |, for example: #e0d2c8|#5e411d|#fccf12|#82ff00|#64bae8 | [optional] 
 **result_content** | **str**| Intended content Type, available Options: 0 - All Tweets 1 - Tweets with the text only content 2 - Tweets with the text and image content. Pass only with overrideColorTemplate set to 1 | [optional] 
 **remove_retweets** | **int**| Flag (0, 1) Should retweets be filtered? | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_video_edit**
> Widget widget_video_edit(name=name, use_duration=use_duration, duration=duration, scale_type_id=scale_type_id, mute=mute, loop=loop)

Parameters for editing existing video on a layout

Parameters for editing existing video on a layout, for adding new videos, please refer to POST /library documentation

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Edit only - Optional Widget Name (optional)
use_duration = 56 # int | Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well (optional)
duration = 56 # int | Edit Only - The Widget Duration (optional)
scale_type_id = 'scale_type_id_example' # str | How should the video be scaled, available options: aspect, stretch (optional)
mute = 56 # int | Edit only - Flag (0, 1) Should the video be muted? (optional)
loop = 56 # int | Edit only - Flag (0, 1) Should the video loop (only for duration > 0 )? (optional)

try:
    # Parameters for editing existing video on a layout
    api_response = api_instance.widget_video_edit(name=name, use_duration=use_duration, duration=duration, scale_type_id=scale_type_id, mute=mute, loop=loop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_video_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Edit only - Optional Widget Name | [optional] 
 **use_duration** | **int**| Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **duration** | **int**| Edit Only - The Widget Duration | [optional] 
 **scale_type_id** | **str**| How should the video be scaled, available options: aspect, stretch | [optional] 
 **mute** | **int**| Edit only - Flag (0, 1) Should the video be muted? | [optional] 
 **loop** | **int**| Edit only - Flag (0, 1) Should the video loop (only for duration &gt; 0 )? | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_video_in_add**
> Widget widget_video_in_add(playlist_id, source_id, duration=duration, use_duration=use_duration)

Add a Video In Widget

Add a new Video In Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
source_id = 'source_id_example' # str | Which device input should be shown? available options: HDMI, RGB, DVI, DP, OPS
duration = 56 # int | The Widget Duration (optional)
use_duration = 56 # int | Flag (0, 1) Select only if you will provide duration parameter as well (optional)

try:
    # Add a Video In Widget
    api_response = api_instance.widget_video_in_add(playlist_id, source_id, duration=duration, use_duration=use_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_video_in_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **source_id** | **str**| Which device input should be shown? available options: HDMI, RGB, DVI, DP, OPS | 
 **duration** | **int**| The Widget Duration | [optional] 
 **use_duration** | **int**| Flag (0, 1) Select only if you will provide duration parameter as well | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_weather_add**
> Widget widget_weather_add(playlist_id, use_display_location, name=name, duration=duration, use_duration=use_duration, longitude=longitude, latitude=latitude, template_id=template_id, units=units, update_interval=update_interval, lang=lang, day_conditions_only=day_conditions_only, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, current_template=current_template, daily_template=daily_template, style_sheet=style_sheet, style_sheet2=style_sheet2)

Add a Weather Widget

Add a new Weather Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Weather widget
use_display_location = 56 # int | Flag (0, 1) Use the location configured on display
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | Widget Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
longitude = 8.14 # float | The longitude for this weather widget, only pass if useDisplayLocation set to 0 (optional)
latitude = 8.14 # float | The latitude for this weather widget, only pass if useDisplayLocation set to 0 (optional)
template_id = 'template_id_example' # str | Use pre-configured templates, available options: weather-module0-5day, weather-module0-singleday, weather-module0-singleday2, weather-module1l, weather-module1p, weather-module2l, weather-module2p, weather-module3l, weather-module3p, weather-module4l, weather-module4p, weather-module5l, weather-module6v, weather-module6h (optional)
units = 'units_example' # str | Units you would like to use, available options: auto, ca, si, uk2, us (optional)
update_interval = 56 # int | Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 (optional)
lang = 'lang_example' # str | Language you'd like to use, supported languages ar, az, be, bs, cs, de, en, el, es, fr, hr, hu, id, it, is, kw, nb, nl, pl, pt, ru, sk, sr, sv, tet, tr, uk, x-pig-latin, zh, zh-tw (optional)
day_conditions_only = 56 # int | Flag (0, 1) Would you like to only show the Daytime weather conditions (optional)
override_template = 56 # int | flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters (optional)
widget_original_width = 56 # int | This is the intended Width of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
widget_original_height = 56 # int | This is the intended Height of the template and is used to scale the Widget within it's region when the template is applied, Pass only with overrideTemplate set to 1 (optional)
current_template = 'current_template_example' # str | Current template, Pass only with overrideTemplate set to 1  (optional)
daily_template = 'daily_template_example' # str | Replaces [dailyForecast] in main template, Pass only with overrideTemplate set to 1  (optional)
style_sheet = 'style_sheet_example' # str | Optional StyleSheet, Pass only with overrideTemplate set to 1  (optional)
style_sheet2 = 'style_sheet_example' # str | Optional JavaScript, Pass only with overrideTemplate set to 1  (optional)

try:
    # Add a Weather Widget
    api_response = api_instance.widget_weather_add(playlist_id, use_display_location, name=name, duration=duration, use_duration=use_duration, longitude=longitude, latitude=latitude, template_id=template_id, units=units, update_interval=update_interval, lang=lang, day_conditions_only=day_conditions_only, override_template=override_template, widget_original_width=widget_original_width, widget_original_height=widget_original_height, current_template=current_template, daily_template=daily_template, style_sheet=style_sheet, style_sheet2=style_sheet2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_weather_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Weather widget | 
 **use_display_location** | **int**| Flag (0, 1) Use the location configured on display | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| Widget Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **longitude** | **float**| The longitude for this weather widget, only pass if useDisplayLocation set to 0 | [optional] 
 **latitude** | **float**| The latitude for this weather widget, only pass if useDisplayLocation set to 0 | [optional] 
 **template_id** | **str**| Use pre-configured templates, available options: weather-module0-5day, weather-module0-singleday, weather-module0-singleday2, weather-module1l, weather-module1p, weather-module2l, weather-module2p, weather-module3l, weather-module3p, weather-module4l, weather-module4p, weather-module5l, weather-module6v, weather-module6h | [optional] 
 **units** | **str**| Units you would like to use, available options: auto, ca, si, uk2, us | [optional] 
 **update_interval** | **int**| Update interval in minutes, should be kept as high as possible, if data change once per hour, this should be set to 60 | [optional] 
 **lang** | **str**| Language you&#39;d like to use, supported languages ar, az, be, bs, cs, de, en, el, es, fr, hr, hu, id, it, is, kw, nb, nl, pl, pt, ru, sk, sr, sv, tet, tr, uk, x-pig-latin, zh, zh-tw | [optional] 
 **day_conditions_only** | **int**| Flag (0, 1) Would you like to only show the Daytime weather conditions | [optional] 
 **override_template** | **int**| flag (0, 1) set to 0 and use templateId or set to 1 and provide whole template in the next parameters | [optional] 
 **widget_original_width** | **int**| This is the intended Width of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **widget_original_height** | **int**| This is the intended Height of the template and is used to scale the Widget within it&#39;s region when the template is applied, Pass only with overrideTemplate set to 1 | [optional] 
 **current_template** | **str**| Current template, Pass only with overrideTemplate set to 1  | [optional] 
 **daily_template** | **str**| Replaces [dailyForecast] in main template, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet** | **str**| Optional StyleSheet, Pass only with overrideTemplate set to 1  | [optional] 
 **style_sheet2** | **str**| Optional JavaScript, Pass only with overrideTemplate set to 1  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_webpage_add**
> Widget widget_webpage_add(playlist_id, uri, mode_id, name=name, duration=duration, use_duration=use_duration, transparency=transparency, scaling=scaling, offset_left=offset_left, offset_top=offset_top, page_width=page_width, page_height=page_height)

Add a Web page Widget

Add a new Web page Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Web page to
uri = 'uri_example' # str |  string containing the location (URL) of the web page
mode_id = 56 # int | The mode option for Web page, 1- Open Natively, 2- Manual Position, 3- Best Ft
name = 'name_example' # str | Optional Widget Name (optional)
duration = 56 # int | The Web page Duration (optional)
use_duration = 56 # int | (0, 1) Select 1 only if you will provide duration parameter as well (optional)
transparency = 56 # int |  flag (0,1) should the HTML be shown with a transparent background? (optional)
scaling = 56 # int | For Manual position the percentage to scale the Web page (0-100) (optional)
offset_left = 56 # int | For Manual position, the starting point from the left in pixels (optional)
offset_top = 56 # int | For Manual position, the starting point from the Top in pixels (optional)
page_width = 56 # int | For Manual Position and Best Fit, The width of the page - if empty it will use region width (optional)
page_height = 56 # int | For Manual Position and Best Fit, The height of the page - if empty it will use region height (optional)

try:
    # Add a Web page Widget
    api_response = api_instance.widget_webpage_add(playlist_id, uri, mode_id, name=name, duration=duration, use_duration=use_duration, transparency=transparency, scaling=scaling, offset_left=offset_left, offset_top=offset_top, page_width=page_width, page_height=page_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widget_webpage_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Web page to | 
 **uri** | **str**|  string containing the location (URL) of the web page | 
 **mode_id** | **int**| The mode option for Web page, 1- Open Natively, 2- Manual Position, 3- Best Ft | 
 **name** | **str**| Optional Widget Name | [optional] 
 **duration** | **int**| The Web page Duration | [optional] 
 **use_duration** | **int**| (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **transparency** | **int**|  flag (0,1) should the HTML be shown with a transparent background? | [optional] 
 **scaling** | **int**| For Manual position the percentage to scale the Web page (0-100) | [optional] 
 **offset_left** | **int**| For Manual position, the starting point from the left in pixels | [optional] 
 **offset_top** | **int**| For Manual position, the starting point from the Top in pixels | [optional] 
 **page_width** | **int**| For Manual Position and Best Fit, The width of the page - if empty it will use region width | [optional] 
 **page_height** | **int**| For Manual Position and Best Fit, The height of the page - if empty it will use region height | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widgetdata_set_view_add**
> Widget widgetdata_set_view_add(playlist_id, data_set_id, name=name, data_set_column_id=data_set_column_id, duration=duration, use_duration=use_duration, update_interval=update_interval, rows_per_page=rows_per_page, show_headings=show_headings, upper_limit=upper_limit, lower_limit=lower_limit, filter=filter, ordering=ordering, template_id=template_id, override_template=override_template, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, no_data_message=no_data_message)

Add a dataSetView Widget

Add a new dataSetView Widget to the specified playlist

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
api_instance = swagger_client.WidgetApi(swagger_client.ApiClient(configuration))
playlist_id = 56 # int | The playlist ID to add a Widget to
data_set_id = 56 # int | Create dataSetView Widget using provided dataSetId of an existing dataSet
name = 'name_example' # str | Optional Widget Name (optional)
data_set_column_id = [56] # list[int] |  EDIT only - Array of dataSetColumn IDs to assign (optional)
duration = 56 # int | EDIT Only - The dataSetView Duration (optional)
use_duration = 56 # int | Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well (optional)
update_interval = 56 # int | EDIT Only - Update interval in minutes (optional)
rows_per_page = 56 # int | EDIT Only - Number of rows per page, 0 for no pages (optional)
show_headings = 56 # int | EDIT Only - Should the table show Heading? (0,1) (optional)
upper_limit = 56 # int | EDIT Only - Upper low limit for this dataSet, 0 for nor limit (optional)
lower_limit = 56 # int | EDIT Only - Lower low limit for this dataSet, 0 for nor limit (optional)
filter = 'filter_example' # str | EDIT Only - SQL clause for filter this dataSet (optional)
ordering = 'ordering_example' # str | EDIT Only - SQL clause for how this dataSet should be ordered (optional)
template_id = 'template_id_example' # str | EDIT Only - Template you'd like to apply, options available: empty, light-green (optional)
override_template = 56 # int | EDIT Only - flag (0, 1) override template checkbox (optional)
use_ordering_clause = 56 # int | EDIT Only - flag (0,1) Use advanced order clause - set to 1 if ordering is provided (optional)
use_filtering_clause = 56 # int | EDIT Only - flag (0,1) Use advanced filter clause - set to 1 if filter is provided (optional)
no_data_message = 'no_data_message_example' # str | EDIT Only - A message to display when no data is returned from the source (optional)

try:
    # Add a dataSetView Widget
    api_response = api_instance.widgetdata_set_view_add(playlist_id, data_set_id, name=name, data_set_column_id=data_set_column_id, duration=duration, use_duration=use_duration, update_interval=update_interval, rows_per_page=rows_per_page, show_headings=show_headings, upper_limit=upper_limit, lower_limit=lower_limit, filter=filter, ordering=ordering, template_id=template_id, override_template=override_template, use_ordering_clause=use_ordering_clause, use_filtering_clause=use_filtering_clause, no_data_message=no_data_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetApi->widgetdata_set_view_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| The playlist ID to add a Widget to | 
 **data_set_id** | **int**| Create dataSetView Widget using provided dataSetId of an existing dataSet | 
 **name** | **str**| Optional Widget Name | [optional] 
 **data_set_column_id** | [**list[int]**](int.md)|  EDIT only - Array of dataSetColumn IDs to assign | [optional] 
 **duration** | **int**| EDIT Only - The dataSetView Duration | [optional] 
 **use_duration** | **int**| Edit Only - (0, 1) Select 1 only if you will provide duration parameter as well | [optional] 
 **update_interval** | **int**| EDIT Only - Update interval in minutes | [optional] 
 **rows_per_page** | **int**| EDIT Only - Number of rows per page, 0 for no pages | [optional] 
 **show_headings** | **int**| EDIT Only - Should the table show Heading? (0,1) | [optional] 
 **upper_limit** | **int**| EDIT Only - Upper low limit for this dataSet, 0 for nor limit | [optional] 
 **lower_limit** | **int**| EDIT Only - Lower low limit for this dataSet, 0 for nor limit | [optional] 
 **filter** | **str**| EDIT Only - SQL clause for filter this dataSet | [optional] 
 **ordering** | **str**| EDIT Only - SQL clause for how this dataSet should be ordered | [optional] 
 **template_id** | **str**| EDIT Only - Template you&#39;d like to apply, options available: empty, light-green | [optional] 
 **override_template** | **int**| EDIT Only - flag (0, 1) override template checkbox | [optional] 
 **use_ordering_clause** | **int**| EDIT Only - flag (0,1) Use advanced order clause - set to 1 if ordering is provided | [optional] 
 **use_filtering_clause** | **int**| EDIT Only - flag (0,1) Use advanced filter clause - set to 1 if filter is provided | [optional] 
 **no_data_message** | **str**| EDIT Only - A message to display when no data is returned from the source | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

