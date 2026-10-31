# TemplateSourcePdf

A template's PDF to merge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Must be `template`. | [default to 'template']
**id** | **str** | The ID of the submission, combined PDF, template or custom file. | 
**template_version** | **str** | For a `template` source, the version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). | [optional] 
**processed** | **bool** | For a `template` source: true (the default) merges the template's processed PDF, which is the PDF submissions are filled in on (decrypted, with its form fields removed). false merges the PDF as it was uploaded. | [optional] 

## Example

```python
from docspring.models.template_source_pdf import TemplateSourcePdf

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSourcePdf from a JSON string
template_source_pdf_instance = TemplateSourcePdf.from_json(json)
# print the JSON string representation of the object
print(TemplateSourcePdf.to_json())

# convert the object into a dict
template_source_pdf_dict = template_source_pdf_instance.to_dict()
# create an instance of TemplateSourcePdf from a dict
template_source_pdf_from_dict = TemplateSourcePdf.from_dict(template_source_pdf_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


