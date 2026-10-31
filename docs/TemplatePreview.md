# TemplatePreview

PNG images of a template's pages filled in with data you send (not a PDF), to check how an HTML, PDF or Word template prints with your data before you publish a version or send live data. A preview makes no submission and uses no credits. Its pages are watermarked like a test submission's PDF, and it's deleted an hour after it's created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The preview's ID. | 
**template_id** | **str** | The template's ID. | 
**version** | **str** | The published version that was rendered, such as `1.2.0`. Null for the draft. | 
**state** | [**TemplatePreviewState**](TemplatePreviewState.md) | `pending` while it renders (usually a few seconds), then `processed`, or `error` with an `error_message`. | 
**error_message** | **str** | Why the preview couldn't be rendered, such as an error in an HTML or Word template's Liquid, or a value in the data that a field can't print. | 
**page_count** | **int** | How many pages the template printed, once it's processed. | 
**pages** | [**List[PageImage]**](PageImage.md) | A PNG image of each page once it's processed, in order: `pages[0]` is page 1. A preview has no PDF. Their `download_url`s expire, so get the preview again when you need them. | 
**expires_at** | **datetime** | When the preview and its images are deleted. | 

## Example

```python
from docspring.models.template_preview import TemplatePreview

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePreview from a JSON string
template_preview_instance = TemplatePreview.from_json(json)
# print the JSON string representation of the object
print(TemplatePreview.to_json())

# convert the object into a dict
template_preview_dict = template_preview_instance.to_dict()
# create an instance of TemplatePreview from a dict
template_preview_from_dict = TemplatePreview.from_dict(template_preview_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


