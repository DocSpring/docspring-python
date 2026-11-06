# TemplateFormSection

A section of the template's web form, with its fields in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The section's ID, unique among the template's sections. Any string you choose. | 
**title** | **str** | The section's heading on the web form. | 
**description** | **str** | Text shown under the section's heading. Null for none. | 
**field_ids** | **List[int]** | The IDs of the section's fields (Field's `id`), in the order the web form shows them. A field can be in one section only. | 

## Example

```python
from docspring.models.template_form_section import TemplateFormSection

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFormSection from a JSON string
template_form_section_instance = TemplateFormSection.from_json(json)
# print the JSON string representation of the object
print(TemplateFormSection.to_json())

# convert the object into a dict
template_form_section_dict = template_form_section_instance.to_dict()
# create an instance of TemplateFormSection from a dict
template_form_section_from_dict = TemplateFormSection.from_dict(template_form_section_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


