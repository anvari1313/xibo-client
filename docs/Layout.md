# Layout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_id** | **int** | The layoutId | [optional] 
**owner_id** | **int** | The userId of the Layout Owner | [optional] 
**campaign_id** | **int** | The id of the Layout&#39;s dedicated Campaign | [optional] 
**background_image_id** | **int** | The id of the image media set as the background | [optional] 
**schema_version** | **int** | The XLF schema version | [optional] 
**layout** | **str** | The name of the Layout | [optional] 
**description** | **str** | The description of the Layout | [optional] 
**background_color** | **str** | A HEX string representing the Layout background color | [optional] 
**created_dt** | **str** | The datetime the Layout was created | [optional] 
**modified_dt** | **str** | The datetime the Layout was last modified | [optional] 
**status** | **int** | Flag indicating the Layout status | [optional] 
**retired** | **int** | Flag indicating whether the Layout is retired | [optional] 
**backgroundz_index** | **int** | The Layer that the background should occupy | [optional] 
**width** | **float** | The Layout Width | [optional] 
**height** | **float** | The Layout Height | [optional] 
**display_order** | **int** | If this Layout has been requested by Campaign, then this is the display order of the Layout within the Campaign | [optional] 
**duration** | **int** | A read-only estimate of this Layout&#39;s total duration in seconds. This is equal to the longest region duration and is valid when the layout status is 1 or 2. | [optional] 
**status_message** | **str** | A status message detailing any errors with the layout | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


