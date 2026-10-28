# TemplateDocumentSummary

A PDF template's PDF, as template lists show it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The PDF's file name. Null until a `document_url` has been downloaded. | 
**state** | [**TemplateDocumentState**](TemplateDocumentState.md) | `pending` while DocSpring processes the PDF, then `processed` (`ready` says when its pages are done too). `password_required`, `malformed_pdf` and `unknown_error` mean the PDF couldn't be processed, and `error_message` says why: upload it again or upload another one. `downloading` while DocSpring downloads a `document_url`, then as for an upload. `download_failed` means it couldn't be downloaded, and `error_message` says why. A template keeps its PDF while a new one is downloaded, and when it couldn't be. | 
**error_message** | **str** | Why the PDF couldn't be processed or downloaded, and how to fix it. Null unless `state` is an error. | 
**page_count** | **int** | 0 until the PDF has been processed. | 

## Example

```python
from docspring.models.template_document_summary import TemplateDocumentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDocumentSummary from a JSON string
template_document_summary_instance = TemplateDocumentSummary.from_json(json)
# print the JSON string representation of the object
print(TemplateDocumentSummary.to_json())

# convert the object into a dict
template_document_summary_dict = template_document_summary_instance.to_dict()
# create an instance of TemplateDocumentSummary from a dict
template_document_summary_from_dict = TemplateDocumentSummary.from_dict(template_document_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


