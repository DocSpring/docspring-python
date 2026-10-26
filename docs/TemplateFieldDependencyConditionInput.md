# TemplateFieldDependencyConditionInput

A condition on a field's value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | **str** | Must be `range`. | [default to 'range']
**value** | **object** | The lower end of the range, a number (or a number as a string, as the template editor saves it). Null or left out for no lower end. A range needs `value`, `range_max` or both. | 
**range_max** | **object** | The upper end of the range, a number (or a number as a string, as the template editor saves it). Null or left out for no upper end. | [optional] 

## Example

```python
from docspring.models.template_field_dependency_condition_input import TemplateFieldDependencyConditionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldDependencyConditionInput from a JSON string
template_field_dependency_condition_input_instance = TemplateFieldDependencyConditionInput.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldDependencyConditionInput.to_json())

# convert the object into a dict
template_field_dependency_condition_input_dict = template_field_dependency_condition_input_instance.to_dict()
# create an instance of TemplateFieldDependencyConditionInput from a dict
template_field_dependency_condition_input_from_dict = TemplateFieldDependencyConditionInput.from_dict(template_field_dependency_condition_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


