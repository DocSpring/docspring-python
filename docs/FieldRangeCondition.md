# FieldRangeCondition

A condition on whether a number field's value is in a range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | **str** | Must be `range`. | [default to 'range']
**value** | **object** | The lower end of the range, a number (or a number as a string, as the template editor saves it). Null or left out for no lower end. A range needs `value`, `range_max` or both. | [optional] 
**range_max** | **object** | The upper end of the range, a number (or a number as a string, as the template editor saves it). Null or left out for no upper end. | [optional] 

## Example

```python
from docspring.models.field_range_condition import FieldRangeCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldRangeCondition from a JSON string
field_range_condition_instance = FieldRangeCondition.from_json(json)
# print the JSON string representation of the object
print(FieldRangeCondition.to_json())

# convert the object into a dict
field_range_condition_dict = field_range_condition_instance.to_dict()
# create an instance of FieldRangeCondition from a dict
field_range_condition_from_dict = FieldRangeCondition.from_dict(field_range_condition_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


