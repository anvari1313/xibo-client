# Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **int** | The Notifcation ID | [optional] 
**created_dt** | **int** | Create Date as Unix Timestamp | [optional] 
**release_dt** | **int** | Release Date as Unix Timestamp | [optional] 
**subject** | **str** | The subject line | [optional] 
**body** | **str** | The HTML body of the notification | [optional] 
**is_email** | **int** | Should the notification be emailed | [optional] 
**is_interrupt** | **int** | Should the notification interrupt the CMS UI on navigate/login | [optional] 
**is_system** | **int** | Flag for system notification | [optional] 
**user_id** | **int** | The Owner User Id | [optional] 
**user_groups** | [**list[UserGroup]**](UserGroup.md) | User Group Notifications associated with this notification | [optional] 
**display_groups** | [**list[DisplayGroup]**](DisplayGroup.md) | Display Groups associated with this notification | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


