# CombinedPdfFiles

A combined PDF's generated files, by format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdf** | [**GeneratedFile**](GeneratedFile.md) |  | [optional] 

## Example

```python
from docspring.models.combined_pdf_files import CombinedPdfFiles

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedPdfFiles from a JSON string
combined_pdf_files_instance = CombinedPdfFiles.from_json(json)
# print the JSON string representation of the object
print(CombinedPdfFiles.to_json())

# convert the object into a dict
combined_pdf_files_dict = combined_pdf_files_instance.to_dict()
# create an instance of CombinedPdfFiles from a dict
combined_pdf_files_from_dict = CombinedPdfFiles.from_dict(combined_pdf_files_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


