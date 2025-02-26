# CreateSubmissionDataRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data_request** | [**SubmissionDataRequestShow**](SubmissionDataRequestShow.md) |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from docspring.models.create_submission_data_request_response import CreateSubmissionDataRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionDataRequestResponse from a JSON string
create_submission_data_request_response_instance = CreateSubmissionDataRequestResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionDataRequestResponse.to_json())

# convert the object into a dict
create_submission_data_request_response_dict = create_submission_data_request_response_instance.to_dict()
# create an instance of CreateSubmissionDataRequestResponse from a dict
create_submission_data_request_response_from_dict = CreateSubmissionDataRequestResponse.from_dict(create_submission_data_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


