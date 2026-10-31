# SubmissionAction

An upload of a PDF to your storage, such as an S3 bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The upload's ID. | 
**integration_id** | **str** | The ID of the account integration it used. | 
**state** | [**SubmissionActionState**](SubmissionActionState.md) | `pending` until the upload has run, then `processed`. `failed`: your storage rejected it. `error`: it failed in DocSpring. | 
**action_type** | [**SubmissionActionType**](SubmissionActionType.md) | The kind of storage, such as `aws_s3_upload` for an S3 bucket. | 
**result_data** | **Dict[str, object]** | Where the PDF was uploaded, such as the S3 bucket and key. | 
**error_message** | **str** | Why the upload failed, when `state` is `failed` or `error`. | 

## Example

```python
from docspring.models.submission_action import SubmissionAction

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionAction from a JSON string
submission_action_instance = SubmissionAction.from_json(json)
# print the JSON string representation of the object
print(SubmissionAction.to_json())

# convert the object into a dict
submission_action_dict = submission_action_instance.to_dict()
# create an instance of SubmissionAction from a dict
submission_action_from_dict = SubmissionAction.from_dict(submission_action_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


