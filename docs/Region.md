# Region

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** | The ID of this region | [optional] 
**layout_id** | **int** | The Layout ID this region belongs to | [optional] 
**owner_id** | **int** | The userId of the User that owns this Region | [optional] 
**name** | **str** | The name of this Region | [optional] 
**width** | **float** | Width of the region | [optional] 
**height** | **float** | Height of the Region | [optional] 
**top** | **float** | The top coordinate of the Region | [optional] 
**left** | **float** | The left coordinate of the Region | [optional] 
**z_index** | **int** | The z-index of the Region to control Layering | [optional] 
**playlists** | [**list[Playlist]**](Playlist.md) | An array of Playlists assigned | [optional] 
**region_options** | [**list[RegionOption]**](RegionOption.md) | An array of Region Options | [optional] 
**permissions** | [**list[Permission]**](Permission.md) | An array of Permissions | [optional] 
**display_order** | **int** | When linked from a Playlist, what is the display order of that link | [optional] 
**duration** | **int** | A read-only estimate of this Regions&#39;s total duration in seconds. This is valid when the parent layout status is 1 or 2. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


