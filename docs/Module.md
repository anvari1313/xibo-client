# Module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | The ID of this Module | [optional] 
**name** | **str** | Module Name | [optional] 
**description** | **str** | Description of the Module | [optional] 
**valid_extensions** | **str** | A comma separated list of Valid Extensions | [optional] 
**image_uri** | **str** | The file uri of an image to represent this Module | [optional] 
**type** | **str** | The type code for this module | [optional] 
**enabled** | **int** | A flag indicating whether this module is enabled | [optional] 
**region_specific** | **int** | A flag indicating whether this module is specific to a Layout or can be uploaded to the Library | [optional] 
**preview_enabled** | **int** | A flag indicating whether the Layout designer should render a preview of this module | [optional] 
**assignable** | **int** | A flag indicating whether the module is assignable to a Layout | [optional] 
**render_as** | **str** | A flag indicating whether the module should be rendered natively by the Player or via the CMS (native|html) | [optional] 
**default_duration** | **int** | The default duration for Widgets of this Module when the user has elected to not set a specific duration. | [optional] 
**settings** | **list[str]** | An array of additional module specific settings | [optional] 
**schema_version** | **int** | The schema version of the module | [optional] 
**_class** | **str** | Class Name including namespace | [optional] 
**view_path** | **str** | The Twig View path for module specific templates | [optional] 
**install_name** | **str** | The original installation name of this module. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


