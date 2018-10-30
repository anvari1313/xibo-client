# Media

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **int** | The Media ID | [optional] 
**owner_id** | **int** | The ID of the User that owns this Media | [optional] 
**parent_id** | **int** | The Parent ID of this Media if it has been revised | [optional] 
**name** | **str** | The Name of this Media | [optional] 
**media_type** | **int** | The module type of this Media | [optional] 
**stored_as** | **str** | The file name of the media as stored in the library | [optional] 
**file_name** | **str** | The original file name as it was uploaded | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Tags associated with this Media | [optional] 
**file_size** | **int** | The file size in bytes | [optional] 
**duration** | **int** | The duration to use when assigning this media to a Layout widget | [optional] 
**valid** | **int** | Flag indicating whether this media is valid. | [optional] 
**module_system_file** | **int** | Flag indicating whether this media is a system file or not | [optional] 
**expires** | **int** | Timestamp indicating when this media should expire | [optional] 
**retired** | **int** | Flag indicating whether this media is retired | [optional] 
**is_edited** | **int** | Flag indicating whether this media has been edited and replaced with a newer file | [optional] 
**md5** | **str** | A MD5 checksum of the stored media file | [optional] 
**owner** | **str** | The username of the User that owns this media | [optional] 
**groups_with_permissions** | **str** | A comma separated list of groups/users with permissions to this Media | [optional] 
**released** | **int** | A flag indicating whether this media has been released | [optional] 
**api_ref** | **str** | An API reference | [optional] 
**created_dt** | **str** | The datetime the Media was created | [optional] 
**modified_dt** | **str** | The datetime the Media was last modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


