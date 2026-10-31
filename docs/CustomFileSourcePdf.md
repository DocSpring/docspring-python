# CustomFileSourcePdf

A custom file to merge (POST /custom_files).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Must be `custom_file`. | [default to 'custom_file']
**id** | **str** | The ID of the submission, combined PDF, template or custom file. | 

## Example

```python
from docspring.models.custom_file_source_pdf import CustomFileSourcePdf

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFileSourcePdf from a JSON string
custom_file_source_pdf_instance = CustomFileSourcePdf.from_json(json)
# print the JSON string representation of the object
print(CustomFileSourcePdf.to_json())

# convert the object into a dict
custom_file_source_pdf_dict = custom_file_source_pdf_instance.to_dict()
# create an instance of CustomFileSourcePdf from a dict
custom_file_source_pdf_from_dict = CustomFileSourcePdf.from_dict(custom_file_source_pdf_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


