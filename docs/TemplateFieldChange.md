# TemplateFieldChange

A field whose settings changed between two versions of a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The field's ID. | 
**changed_settings** | **List[str]** | The names of the settings that changed, such as `x` or `required`. | 
**old** | [**ModelField**](ModelField.md) |  | 
**new** | [**ModelField**](ModelField.md) |  | 

## Example

```python
from docspring.models.template_field_change import TemplateFieldChange

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldChange from a JSON string
template_field_change_instance = TemplateFieldChange.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldChange.to_json())

# convert the object into a dict
template_field_change_dict = template_field_change_instance.to_dict()
# create an instance of TemplateFieldChange from a dict
template_field_change_from_dict = TemplateFieldChange.from_dict(template_field_change_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


