# FieldDependency

A field's own conditional logic rule: when other fields' values meet its conditions, the field is shown, made required, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TemplateFieldDependencyAction**](TemplateFieldDependencyAction.md) | What the rule does to the fields it applies to when its conditions are met. | 
**match** | [**TemplateFieldDependencyMatch**](TemplateFieldDependencyMatch.md) | Whether all of the conditions (the default) or any of them must be met. | [optional] 
**conditions** | [**List[TemplateFieldDependencyCondition]**](TemplateFieldDependencyCondition.md) | The conditions on other fields' values. | 

## Example

```python
from docspring.models.field_dependency import FieldDependency

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDependency from a JSON string
field_dependency_instance = FieldDependency.from_json(json)
# print the JSON string representation of the object
print(FieldDependency.to_json())

# convert the object into a dict
field_dependency_dict = field_dependency_instance.to_dict()
# create an instance of FieldDependency from a dict
field_dependency_from_dict = FieldDependency.from_dict(field_dependency_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


