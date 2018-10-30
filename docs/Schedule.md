# Schedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | The ID of this Event | [optional] 
**event_type_id** | **int** | The Event Type ID | [optional] 
**campaign_id** | **int** | The CampaignID this event is for | [optional] 
**command_id** | **int** | The CommandId this event is for | [optional] 
**display_groups** | [**list[DisplayGroup]**](DisplayGroup.md) | Display Groups assigned to this Scheduled Event. | [optional] 
**user_id** | **int** | The userId that owns this event. | [optional] 
**from_dt** | **int** | A Unix timestamp representing the from date of this event in CMS time. | [optional] 
**to_dt** | **int** | A Unix timestamp representing the to date of this event in CMS time. | [optional] 
**is_priority** | **int** | Integer indicating the event priority. | [optional] 
**display_order** | **int** | The display order for this event. | [optional] 
**recurrence_type** | **str** | If this event recurs when what is the recurrence period. | [optional] 
**recurrence_detail** | **int** | If this event recurs when what is the recurrence frequency. | [optional] 
**recurrence_range** | **int** | A Unix timestamp indicating the end time of the recurring events. | [optional] 
**recurrence_repeats_on** | **str** | Recurrence repeats on days - 0 to 7 where 0 is a monday | [optional] 
**campaign** | **str** | The Campaign/Layout Name | [optional] 
**command** | **str** | The Command Name | [optional] 
**day_part_id** | **int** | The Day Part Id | [optional] 
**is_always** | **int** | Is this event an always on event? | [optional] 
**is_custom** | **int** | Does this event have custom from/to date times? | [optional] 
**sync_timezone** | **int** | Flag indicating whether the event will sync to the Display timezone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


