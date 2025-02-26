# CreateSubmissionDataRequestEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**event** | [**SubmissionDataRequestEvent**](SubmissionDataRequestEvent.md) |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from docspring.models.create_submission_data_request_event_response import CreateSubmissionDataRequestEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionDataRequestEventResponse from a JSON string
create_submission_data_request_event_response_instance = CreateSubmissionDataRequestEventResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionDataRequestEventResponse.to_json())

# convert the object into a dict
create_submission_data_request_event_response_dict = create_submission_data_request_event_response_instance.to_dict()
# create an instance of CreateSubmissionDataRequestEventResponse from a dict
create_submission_data_request_event_response_from_dict = CreateSubmissionDataRequestEventResponse.from_dict(create_submission_data_request_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


