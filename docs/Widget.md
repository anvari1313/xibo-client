# Widget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_id** | **int** | The Widget ID | [optional] 
**playlist_id** | **int** | The ID of the Playlist this Widget belongs to | [optional] 
**owner_id** | **int** | The ID of the User that owns this Widget | [optional] 
**type** | **str** | The Module Type Code | [optional] 
**duration** | **int** | The duration in seconds this widget should be shown | [optional] 
**display_order** | **int** | The display order of this widget | [optional] 
**use_duration** | **int** | Flag indicating if this widget has a duration that should be used | [optional] 
**calculated_duration** | **int** | Calculated Duration of this widget after taking into account the useDuration flag | [optional] 
**created_dt** | **str** | The datetime the Layout was created | [optional] 
**modified_dt** | **str** | The datetime the Layout was last modified | [optional] 
**widget_options** | [**list[WidgetOption]**](WidgetOption.md) | An array of Widget Options | [optional] 
**media_ids** | **list[int]** | An array of MediaIds this widget is linked to | [optional] 
**audio** | [**list[WidgetAudio]**](WidgetAudio.md) | An array of Audio MediaIds this widget is linked to | [optional] 
**permissions** | [**list[Permission]**](Permission.md) | An array of permissions for this widget | [optional] 
**module** | [**ModuleWidget**](ModuleWidget.md) | The Module Object for this Widget | [optional] 
**playlist** | **str** | The name of the Playlist this Widget is on | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


