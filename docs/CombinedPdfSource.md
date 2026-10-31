# CombinedPdfSource

A PDF to merge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CombinedPdfSourceType**](CombinedPdfSourceType.md) | What the PDF is: a submission's PDF, another combined PDF, a template's PDF, a custom file (POST /custom_files) or a PDF to download from a URL. | 
**id** | **str** | The ID of the submission, combined PDF, template or custom file. | [optional] 
**url** | **str** | For a `url` source, the URL to download the PDF from. Removed once the combined PDF has expired. | [optional] 
**template_version** | **str** | For a `template` source, the version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). | [optional] 
**processed** | **bool** | For a `template` source: true (the default) merges the template's processed PDF, which is the PDF submissions are filled in on (decrypted, with its form fields removed). false merges the PDF as it was uploaded. | [optional] 

## Example

```python
from docspring.models.combined_pdf_source import CombinedPdfSource

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedPdfSource from a JSON string
combined_pdf_source_instance = CombinedPdfSource.from_json(json)
# print the JSON string representation of the object
print(CombinedPdfSource.to_json())

# convert the object into a dict
combined_pdf_source_dict = combined_pdf_source_instance.to_dict()
# create an instance of CombinedPdfSource from a dict
combined_pdf_source_from_dict = CombinedPdfSource.from_dict(combined_pdf_source_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


