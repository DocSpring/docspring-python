# CreateSubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**submission** | [**SubmissionPreview**](SubmissionPreview.md) |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from docspring.models.create_submission_response import CreateSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionResponse from a JSON string
create_submission_response_instance = CreateSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionResponse.to_json())

# convert the object into a dict
create_submission_response_dict = create_submission_response_instance.to_dict()
# create an instance of CreateSubmissionResponse from a dict
create_submission_response_from_dict = CreateSubmissionResponse.from_dict(create_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


