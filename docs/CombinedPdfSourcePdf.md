# CombinedPdfSourcePdf

Another combined PDF to merge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Must be `combined_pdf`. | [default to 'combined_pdf']
**id** | **str** | The ID of the submission, combined PDF, template or custom file. | 

## Example

```python
from docspring.models.combined_pdf_source_pdf import CombinedPdfSourcePdf

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedPdfSourcePdf from a JSON string
combined_pdf_source_pdf_instance = CombinedPdfSourcePdf.from_json(json)
# print the JSON string representation of the object
print(CombinedPdfSourcePdf.to_json())

# convert the object into a dict
combined_pdf_source_pdf_dict = combined_pdf_source_pdf_instance.to_dict()
# create an instance of CombinedPdfSourcePdf from a dict
combined_pdf_source_pdf_from_dict = CombinedPdfSourcePdf.from_dict(combined_pdf_source_pdf_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


