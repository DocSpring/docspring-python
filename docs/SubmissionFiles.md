# SubmissionFiles

A submission's generated files. Each one is left out until it exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdf** | [**GeneratedFile**](GeneratedFile.md) | The submission's PDF. | [optional] 
**audit_trail** | [**GeneratedFile**](GeneratedFile.md) | The audit trail of a submission with signature requests: who signed, when and how. It's also added to the end of the PDF when the template's `merge_audit_trail_pdf` is on. | [optional] 
**preview** | [**GeneratedFile**](GeneratedFile.md) | The preview PDF from POST /submissions/{submission_id}/generate_preview, such as for a submission still waiting for its signature requests. | [optional] 

## Example

```python
from docspring.models.submission_files import SubmissionFiles

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionFiles from a JSON string
submission_files_instance = SubmissionFiles.from_json(json)
# print the JSON string representation of the object
print(SubmissionFiles.to_json())

# convert the object into a dict
submission_files_dict = submission_files_instance.to_dict()
# create an instance of SubmissionFiles from a dict
submission_files_from_dict = SubmissionFiles.from_dict(submission_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


