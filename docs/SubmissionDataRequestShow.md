# SubmissionDataRequestShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**order** | **int** |  | 
**sort_order** | **int** |  | 
**fields** | **List[str]** |  | 
**metadata** | **object** |  | 
**state** | **str** |  | 
**viewed_at** | **str** |  | 
**completed_at** | **str** |  | 
**data** | **object** |  | 
**auth_type** | **str** |  | 
**auth_second_factor_type** | **str** |  | 
**auth_provider** | **str** |  | 
**auth_session_started_at** | **str** |  | 
**auth_session_id_hash** | **str** |  | 
**auth_user_id_hash** | **str** |  | 
**auth_username_hash** | **str** |  | 
**auth_phone_number_hash** | **str** |  | 
**ip_address** | **str** |  | 
**user_agent** | **str** |  | 
**submission_id** | **str** |  | 

## Example

```python
from docspring.models.submission_data_request_show import SubmissionDataRequestShow

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionDataRequestShow from a JSON string
submission_data_request_show_instance = SubmissionDataRequestShow.from_json(json)
# print the JSON string representation of the object
print(SubmissionDataRequestShow.to_json())

# convert the object into a dict
submission_data_request_show_dict = submission_data_request_show_instance.to_dict()
# create an instance of SubmissionDataRequestShow from a dict
submission_data_request_show_from_dict = SubmissionDataRequestShow.from_dict(submission_data_request_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


