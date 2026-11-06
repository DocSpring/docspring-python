# TemplateFormSectionInput

A section of the template's web form, with its fields in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The section's ID, unique among the template's sections. Any string you choose. | 
**title** | **str** | The section's heading on the web form. | 
**description** | **str** | Text shown under the section's heading. Null for none. | [optional] 
**field_ids** | **List[int]** | The IDs of the section's fields (Field's `id`), in the order the web form shows them. A field can be in one section only. | 

## Example

```python
from docspring.models.template_form_section_input import TemplateFormSectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFormSectionInput from a JSON string
template_form_section_input_instance = TemplateFormSectionInput.from_json(json)
# print the JSON string representation of the object
print(TemplateFormSectionInput.to_json())

# convert the object into a dict
template_form_section_input_dict = template_form_section_input_instance.to_dict()
# create an instance of TemplateFormSectionInput from a dict
template_form_section_input_from_dict = TemplateFormSectionInput.from_dict(template_form_section_input_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


