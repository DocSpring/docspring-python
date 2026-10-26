# UpdateTemplateDocumentRequest

The new PDF, as one of `cache_id`, `document_url` and `document_base64`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **str** | The `fields.key` of the new PDF, uploaded with the presigned upload (GET /uploads/presign). | [optional] 
**document_url** | **str** | An https:// link to the template's PDF (up to 100 MB), instead of `cache_id`. DocSpring downloads it after responding, following redirects to other https:// links: the template's `document.state` is `downloading` until then (sync.api hosts wait for it). If it can't be downloaded, the state is `download_failed` and `document.error_message` says why. | [optional] 
**document_base64** | **str** | The template's PDF, encoded as base64 (a `data:` URI works too), instead of `cache_id`. Up to 7 MB before it's encoded: send a larger file with `cache_id` or `document_url`. | [optional] 
**filename** | **str** | The PDF's file name, for a `cache_id` (presigned uploads don't send one) or `document_base64`. A `document_url`'s is the last part of its path unless you set it. | [optional] 
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


