# CreateTemplatePreviewRequest

The data to render the template with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | The values of the template's fields, by field name, as you'd send them to create a submission. They're rendered as they are: they aren't checked against the template's fields. A value that a field can't print, such as an image URL that doesn't download, makes the preview's `state` `error`, with an `error_message`. | 

## Example

```python
from docspring.models.create_template_preview_request import CreateTemplatePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplatePreviewRequest from a JSON string
create_template_preview_request_instance = CreateTemplatePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplatePreviewRequest.to_json())

# convert the object into a dict
create_template_preview_request_dict = create_template_preview_request_instance.to_dict()
# create an instance of CreateTemplatePreviewRequest from a dict
create_template_preview_request_from_dict = CreateTemplatePreviewRequest.from_dict(create_template_preview_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


