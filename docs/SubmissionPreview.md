# SubmissionPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  | 
**data_requests** | [**List[SubmissionDataRequest]**](SubmissionDataRequest.md) |  | 
**editable** | **bool** |  | 
**expired** | **bool** |  | 
**expires_at** | **str** |  | 
**id** | **str** |  | 
**json_schema_errors** | **List[str]** |  | 
**metadata** | **object** |  | 
**password** | **str** |  | 
**processed_at** | **str** |  | 
**state** | **str** |  | 
**template_id** | **str** |  | 
**template_type** | **str** |  | 
**template_version** | **str** |  | 
**test** | **bool** |  | 
**truncated_text** | **object** |  | 
**pdf_hash** | **str** |  | 
**download_url** | **str** |  | 
**permanent_download_url** | **str** |  | 
**preview_download_url** | **str** |  | 
**preview_generated_at** | **str** |  | 
**audit_trail_download_url** | **str** |  | 
**actions** | [**List[SubmissionAction]**](SubmissionAction.md) |  | 

## Example

```python
from docspring.models.submission_preview import SubmissionPreview

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionPreview from a JSON string
submission_preview_instance = SubmissionPreview.from_json(json)
# print the JSON string representation of the object
print(SubmissionPreview.to_json())

# convert the object into a dict
submission_preview_dict = submission_preview_instance.to_dict()
# create an instance of SubmissionPreview from a dict
submission_preview_from_dict = SubmissionPreview.from_dict(submission_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


