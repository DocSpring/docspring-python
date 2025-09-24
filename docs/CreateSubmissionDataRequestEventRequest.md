# CreateSubmissionDataRequestEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | 
**message_recipient** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**occurred_at** | **str** |  | [optional] 

## Example

```python
from docspring.models.create_submission_data_request_event_request import CreateSubmissionDataRequestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionDataRequestEventRequest from a JSON string
create_submission_data_request_event_request_instance = CreateSubmissionDataRequestEventRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionDataRequestEventRequest.to_json())

# convert the object into a dict
create_submission_data_request_event_request_dict = create_submission_data_request_event_request_instance.to_dict()
# create an instance of CreateSubmissionDataRequestEventRequest from a dict
create_submission_data_request_event_request_from_dict = CreateSubmissionDataRequestEventRequest.from_dict(create_submission_data_request_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


