# CombinedSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**state** | **str** |  | 
**expired** | **bool** |  | 
**expires_in** | **int** |  | 
**expires_at** | **str** |  | 
**processed_at** | **str** |  | 
**error_message** | **str** |  | 
**submission_ids** | **List[str]** |  | 
**source_pdfs** | **List[object]** |  | 
**metadata** | **object** |  | 
**password** | **str** |  | 
**pdf_hash** | **str** |  | 
**download_url** | **str** |  | 
**actions** | [**List[CombinedSubmissionAction]**](CombinedSubmissionAction.md) |  | 

## Example

```python
from docspring.models.combined_submission import CombinedSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedSubmission from a JSON string
combined_submission_instance = CombinedSubmission.from_json(json)
# print the JSON string representation of the object
print(CombinedSubmission.to_json())

# convert the object into a dict
combined_submission_dict = combined_submission_instance.to_dict()
# create an instance of CombinedSubmission from a dict
combined_submission_from_dict = CombinedSubmission.from_dict(combined_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


