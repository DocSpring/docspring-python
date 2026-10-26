# FieldDependencyInput

A field's own conditional logic rule: when other fields' values meet its conditions, the field is shown, made required, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TemplateFieldDependencyAction**](TemplateFieldDependencyAction.md) | What the rule does to the fields it applies to when its conditions are met. | 
**match** | [**TemplateFieldDependencyMatch**](TemplateFieldDependencyMatch.md) | Whether all of the conditions (the default) or any of them must be met. | [optional] 
**conditions** | [**List[TemplateFieldDependencyConditionInput]**](TemplateFieldDependencyConditionInput.md) | The conditions on other fields' values. | 

## Example

```python
from docspring.models.field_dependency_input import FieldDependencyInput

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDependencyInput from a JSON string
field_dependency_input_instance = FieldDependencyInput.from_json(json)
# print the JSON string representation of the object
print(FieldDependencyInput.to_json())

# convert the object into a dict
field_dependency_input_dict = field_dependency_input_instance.to_dict()
# create an instance of FieldDependencyInput from a dict
field_dependency_input_from_dict = FieldDependencyInput.from_dict(field_dependency_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


