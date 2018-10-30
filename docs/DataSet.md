# DataSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_id** | **int** | The dataSetId | [optional] 
**data_set** | **str** | The dataSet Name | [optional] 
**description** | **str** | The dataSet description | [optional] 
**user_id** | **int** | The userId of the User that owns this DataSet | [optional] 
**last_data_edit** | **int** | Timestamp indicating the date/time this DataSet was edited last | [optional] 
**owner** | **str** | The user name of the User that owns this DataSet | [optional] 
**groups_with_permissions** | **str** | A comma separated list of Groups/Users that have permission to this DataSet | [optional] 
**code** | **str** | A code for this Data Set | [optional] 
**is_lookup** | **int** | Flag to indicate whether this DataSet is a lookup table | [optional] 
**is_remote** | **int** | Flag to indicate whether this DataSet is Remote | [optional] 
**method** | **str** | Method to fetch the Data, can be GET or POST | [optional] 
**uri** | **str** | URI to call to fetch Data from. Replacements are {{DATE}}, {{TIME}} and, in case this is a sequencial used DataSet, {{COL.NAME}} where NAME is a ColumnName from the underlying DataSet. | [optional] 
**post_data** | **str** | Data to send as POST-Data to the remote host with the same Replacements as in the URI. | [optional] 
**authentication** | **str** | Authentication method, can be none, digest, basic | [optional] 
**username** | **str** | Username to authenticate with | [optional] 
**password** | **str** | Corresponding password | [optional] 
**refresh_rate** | **int** | Time in seconds this DataSet should fetch new Datas from the remote host | [optional] 
**clear_rate** | **int** | Time in seconds when this Dataset should be cleared. If here is a lower value than in RefreshRate it will be cleared when the data is refreshed | [optional] 
**runs_after** | **int** | DataSetID of the DataSet which should be fetched and present before the Data from this DataSet are fetched | [optional] 
**last_sync** | **int** | Last Synchronisation Timestamp | [optional] 
**last_clear** | **int** | Last Clear Timestamp | [optional] 
**data_root** | **str** | Root-Element form JSON where the data are stored in | [optional] 
**summarize** | **str** | Optional function to use for summarize or count unique fields in a remote request | [optional] 
**summarize_field** | **str** | JSON-Element below the Root-Element on which the consolidation should be applied on | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


