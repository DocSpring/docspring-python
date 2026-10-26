# UpdateTemplateDocumentRequest

The new PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **str** | The `fields.key` of the new PDF, uploaded with the presigned upload (GET /uploads/presign). | 
**filename** | **str** | The PDF's file name, for a `cache_id` (presigned uploads don't send one). | [optional] 
**reimport_fields** | **bool** | Replace all of the template's fields with the fillable fields in the new PDF, once DocSpring has processed it (`document.field_reimport_state`). As on a first upload, the default typeface, font size, bold and color are taken from the PDF's fields; the template's other settings are kept. If the PDF has no fillable fields, the template keeps its fields. A locked template can't re-import its fields. | [optional] 

## Example

```python
from docspring.models.update_template_document_request import UpdateTemplateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateDocumentRequest from a JSON string
update_template_document_request_instance = UpdateTemplateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateDocumentRequest.to_json())

# convert the object into a dict
update_template_document_request_dict = update_template_document_request_instance.to_dict()
# create an instance of UpdateTemplateDocumentRequest from a dict
update_template_document_request_from_dict = UpdateTemplateDocumentRequest.from_dict(update_template_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


