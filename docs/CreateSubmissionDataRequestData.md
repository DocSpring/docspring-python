# CreateSubmissionDataRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_second_factor_type** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**metadata** | **object** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from docspring.models.create_submission_data_request_data import CreateSubmissionDataRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionDataRequestData from a JSON string
create_submission_data_request_data_instance = CreateSubmissionDataRequestData.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionDataRequestData.to_json())

# convert the object into a dict
create_submission_data_request_data_dict = create_submission_data_request_data_instance.to_dict()
# create an instance of CreateSubmissionDataRequestData from a dict
create_submission_data_request_data_from_dict = CreateSubmissionDataRequestData.from_dict(create_submission_data_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


