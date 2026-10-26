# TemplateFieldDependencyCondition

A condition on a field's value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | [**TemplateFieldDependencyOperator**](TemplateFieldDependencyOperator.md) | How the field's value is compared with `value`. `in`: one of a list. `range`: from `value` to `range_max`. | 
**value** | **object** | The value to compare the field's value with. | [optional] 
**range_max** | **object** | The upper end of a `range`, a number (or a number as a string, as the template editor saves it). | [optional] 

## Example

```python
from docspring.models.template_field_dependency_condition import TemplateFieldDependencyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldDependencyCondition from a JSON string
template_field_dependency_condition_instance = TemplateFieldDependencyCondition.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldDependencyCondition.to_json())

# convert the object into a dict
template_field_dependency_condition_dict = template_field_dependency_condition_instance.to_dict()
# create an instance of TemplateFieldDependencyCondition from a dict
template_field_dependency_condition_from_dict = TemplateFieldDependencyCondition.from_dict(template_field_dependency_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


