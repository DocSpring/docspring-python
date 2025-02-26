# UpdateSubmissionDataRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**metadata** | **object** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from docspring.models.update_submission_data_request_data import UpdateSubmissionDataRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionDataRequestData from a JSON string
update_submission_data_request_data_instance = UpdateSubmissionDataRequestData.from_json(json)
# print the JSON string representation of the object
print(UpdateSubmissionDataRequestData.to_json())

# convert the object into a dict
update_submission_data_request_data_dict = update_submission_data_request_data_instance.to_dict()
# create an instance of UpdateSubmissionDataRequestData from a dict
update_submission_data_request_data_from_dict = UpdateSubmissionDataRequestData.from_dict(update_submission_data_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


