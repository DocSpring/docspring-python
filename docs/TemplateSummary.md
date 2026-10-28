# TemplateSummary

A template in a list: its name, type, folder, latest published version and whether it's ready. Get a template by its ID for its settings, its PDF in full, its HTML, defaults, field dependency rules and published versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The template's ID. | 
**name** | **str** | The template's name. | 
**description** | **str** | Shown under the template's name at the top of its hosted forms, and used as their meta description. Not shown on embedded forms or signature requests. | 
**template_type** | [**TemplateType**](TemplateType.md) | `pdf`: fields placed on an uploaded PDF. `html`: a PDF rendered from HTML and SCSS. It can't be changed after the template is created. | 
**ready** | **bool** | Whether the template can generate PDFs. HTML templates are always ready. A PDF template is ready once DocSpring has stored its PDF, made an image of each page and finished looking for fields on each page, which can be after `document.state` becomes `processed`. A PDF template with no PDF (`document` is null) isn't ready. | 
**document** | [**TemplateDocumentSummary**](TemplateDocumentSummary.md) | The PDF of a PDF template: its file name, page count and processing state. Null for HTML templates, and for a PDF template that has no PDF yet. | 
**parent_folder_id** | **str** | The ID of the folder the template is in. Null for a template at the root. Setting it moves the template and all of its published versions. | 
**path** | **str** | The path of the folder the template is in, such as `/Contracts`. `/` for a template at the root. | 
**latest_version** | **str** | The template's latest published version. Null if no version has been published. | 
**version_published_at** | **datetime** | When this version was published. Null for the draft. | 
**locked** | **bool** | A locked template can't be changed or deleted until it's unlocked (`locked` can always be changed). | 
**last_changed_at** | **datetime** | When the draft was last changed. | 
**created_at** | **datetime** | When the template was created. | 
**updated_at** | **datetime** | When the template was last updated. | 

## Example

```python
from docspring.models.template_summary import TemplateSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSummary from a JSON string
template_summary_instance = TemplateSummary.from_json(json)
# print the JSON string representation of the object
print(TemplateSummary.to_json())

# convert the object into a dict
template_summary_dict = template_summary_instance.to_dict()
# create an instance of TemplateSummary from a dict
template_summary_from_dict = TemplateSummary.from_dict(template_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


