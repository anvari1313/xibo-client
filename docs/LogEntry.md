# LogEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **int** | The Log ID | [optional] 
**run_no** | **str** | A unique run number for a set of Log Messages. | [optional] 
**log_date** | **int** | A timestamp representing the CMS date this log message occured | [optional] 
**channel** | **str** | The Channel that generated this message. WEB/API/MAINT/TEST | [optional] 
**page** | **str** | The requested route | [optional] 
**function** | **str** | The request method, GET/POST/PUT/DELETE | [optional] 
**message** | **str** | The log message | [optional] 
**display_id** | **int** | The display ID this message relates to or NULL for CMS | [optional] 
**type** | **str** | The Log Level | [optional] 
**display** | **str** | The display this message relates to or CMS for CMS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


