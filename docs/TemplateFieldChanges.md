# TemplateFieldChanges

The fields that changed between two versions of a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[ModelField]**](ModelField.md) | The fields that `to_version` has and `from_version` doesn't. | 
**removed** | [**List[ModelField]**](ModelField.md) | The fields that `from_version` has and `to_version` doesn't, as they were. | 
**changed** | [**List[TemplateFieldChange]**](TemplateFieldChange.md) | The fields with changed settings. | 
**reordered** | [**List[TemplateFieldMove]**](TemplateFieldMove.md) | The fields that moved in the template's field order (the order of its fields across all its pages, as the fields endpoint lists them): fields that swapped places, or the field that moved the furthest. The fields that a move pushed along aren't listed. | 

## Example

```python
from docspring.models.template_field_changes import TemplateFieldChanges

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldChanges from a JSON string
template_field_changes_instance = TemplateFieldChanges.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldChanges.to_json())

# convert the object into a dict
template_field_changes_dict = template_field_changes_instance.to_dict()
# create an instance of TemplateFieldChanges from a dict
template_field_changes_from_dict = TemplateFieldChanges.from_dict(template_field_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


