# SubmissionDataRequestEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**submission_id** | **str** |  | 
**submission_data_request_id** | **str** |  | 
**event_type** | **str** |  | 
**message_type** | **str** |  | 
**message_recipient** | **str** |  | 
**occurred_at** | **str** |  | 

## Example

```python
from docspring.models.submission_data_request_event import SubmissionDataRequestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionDataRequestEvent from a JSON string
submission_data_request_event_instance = SubmissionDataRequestEvent.from_json(json)
# print the JSON string representation of the object
print(SubmissionDataRequestEvent.to_json())

# convert the object into a dict
submission_data_request_event_dict = submission_data_request_event_instance.to_dict()
# create an instance of SubmissionDataRequestEvent from a dict
submission_data_request_event_from_dict = SubmissionDataRequestEvent.from_dict(submission_data_request_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


