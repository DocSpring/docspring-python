# Submission422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **str** | Single error message (for non-validation errors) | [optional] 
**submission** | [**SubmissionPreview**](SubmissionPreview.md) |  | [optional] 
**errors** | **List[str]** | Array of validation error messages (when submission data is invalid) | [optional] 

## Example

```python
from docspring.models.submission422_response import Submission422Response

# TODO update the JSON string below
json = "{}"
# create an instance of Submission422Response from a JSON string
submission422_response_instance = Submission422Response.from_json(json)
# print the JSON string representation of the object
print(Submission422Response.to_json())

# convert the object into a dict
submission422_response_dict = submission422_response_instance.to_dict()
# create an instance of Submission422Response from a dict
submission422_response_from_dict = Submission422Response.from_dict(submission422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


