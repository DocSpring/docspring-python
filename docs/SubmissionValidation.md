# SubmissionValidation

Whether creating the submission would succeed, checked without saving it or making any files. `error` is the error that creating it would return (`validation_failed`, or `invalid_data` for data that doesn't match the template's fields), and is left out when `valid` is true.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | True when creating the submission would succeed. | 
**template_id** | **str** | The template's ID. | 
**template_version** | **str** | The published version the request was checked against, such as `1.2.0`. Null for the draft. | 
**error** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 

## Example

```python
from docspring.models.submission_validation import SubmissionValidation

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionValidation from a JSON string
submission_validation_instance = SubmissionValidation.from_json(json)
# print the JSON string representation of the object
print(SubmissionValidation.to_json())

# convert the object into a dict
submission_validation_dict = submission_validation_instance.to_dict()
# create an instance of SubmissionValidation from a dict
submission_validation_from_dict = SubmissionValidation.from_dict(submission_validation_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


