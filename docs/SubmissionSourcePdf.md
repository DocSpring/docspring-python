# SubmissionSourcePdf

A submission's PDF to merge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Must be `submission`. | [default to 'submission']
**id** | **str** | The ID of the submission, combined PDF, template or custom file. | 

## Example

```python
from docspring.models.submission_source_pdf import SubmissionSourcePdf

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionSourcePdf from a JSON string
submission_source_pdf_instance = SubmissionSourcePdf.from_json(json)
# print the JSON string representation of the object
print(SubmissionSourcePdf.to_json())

# convert the object into a dict
submission_source_pdf_dict = submission_source_pdf_instance.to_dict()
# create an instance of SubmissionSourcePdf from a dict
submission_source_pdf_from_dict = SubmissionSourcePdf.from_dict(submission_source_pdf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


