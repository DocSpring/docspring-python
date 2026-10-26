# FieldComparisonCondition

A condition comparing a number field's value with a number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | [**FieldComparisonOperator**](FieldComparisonOperator.md) | How the field's value is compared with `value`. `in`: one of a list. `range`: from `value` to `range_max`. | 
**value** | **object** | The number the field's value is compared with, or a number as a string (as the template editor saves it). The field must be a number field. | 

## Example

```python
from docspring.models.field_comparison_condition import FieldComparisonCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldComparisonCondition from a JSON string
field_comparison_condition_instance = FieldComparisonCondition.from_json(json)
# print the JSON string representation of the object
print(FieldComparisonCondition.to_json())

# convert the object into a dict
field_comparison_condition_dict = field_comparison_condition_instance.to_dict()
# create an instance of FieldComparisonCondition from a dict
field_comparison_condition_from_dict = FieldComparisonCondition.from_dict(field_comparison_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


