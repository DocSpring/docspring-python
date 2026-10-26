# TemplateFieldDependency

A conditional logic rule: when other fields' values meet its conditions, it shows its target fields, makes them required, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TemplateFieldDependencyAction**](TemplateFieldDependencyAction.md) | What the rule does to the fields it applies to when its conditions are met. | 
**match** | [**TemplateFieldDependencyMatch**](TemplateFieldDependencyMatch.md) | Whether all of the conditions (the default) or any of them must be met. | [optional] 
**conditions** | [**List[TemplateFieldDependencyCondition]**](TemplateFieldDependencyCondition.md) | The conditions on other fields' values. | 
**targets** | **List[str]** | The names of the fields the rule shows or makes required. | 
**group** | **str** | Marks a rule made for a field group in the template editor. Its targets outside the group are removed when the template is saved, and the rule is removed once the group has no fields. | [optional] 

## Example

```python
from docspring.models.template_field_dependency import TemplateFieldDependency

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldDependency from a JSON string
template_field_dependency_instance = TemplateFieldDependency.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldDependency.to_json())

# convert the object into a dict
template_field_dependency_dict = template_field_dependency_instance.to_dict()
# create an instance of TemplateFieldDependency from a dict
template_field_dependency_from_dict = TemplateFieldDependency.from_dict(template_field_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


