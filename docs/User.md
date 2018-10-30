# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of this User | [optional] 
**user_name** | **str** | The user name | [optional] 
**user_type_id** | **int** | The user type ID | [optional] 
**logged_in** | **int** | Flag indicating whether this user is logged in or not | [optional] 
**email** | **str** | Email address of the user used for email alerts | [optional] 
**home_page_id** | **int** | The pageId of the Homepage for this User | [optional] 
**last_accessed** | **int** | A timestamp indicating the time the user last logged into the CMS | [optional] 
**new_user_wizard** | **int** | A flag indicating whether this user has see the new user wizard | [optional] 
**retired** | **int** | A flag indicating whether the user is retired | [optional] 
**group_id** | **int** | The users user group ID | [optional] 
**group** | **int** | The users group name | [optional] 
**library_quota** | **int** | The users library quota in bytes | [optional] 
**first_name** | **str** | First Name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**phone** | **str** | Phone Number | [optional] 
**ref1** | **str** | Reference field 1 | [optional] 
**ref2** | **str** | Reference field 2 | [optional] 
**ref3** | **str** | Reference field 3 | [optional] 
**ref4** | **str** | Reference field 4 | [optional] 
**ref5** | **str** | Reference field 5 | [optional] 
**groups** | [**list[UserGroup]**](UserGroup.md) | An array of user groups this user is assigned to | [optional] 
**campaigns** | [**list[Campaign]**](Campaign.md) | An array of Campaigns for this User | [optional] 
**layouts** | [**list[Layout]**](Layout.md) | An array of Layouts for this User | [optional] 
**media** | [**list[Media]**](Media.md) | An array of Media for this user | [optional] 
**events** | [**list[Schedule]**](Schedule.md) | An array of Scheduled Events for this User | [optional] 
**home_page** | **str** | The name of home page | [optional] 
**is_system_notification** | **int** | Does this Group receive system notifications. | [optional] 
**is_display_notification** | **int** | Does this Group receive system notifications. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


