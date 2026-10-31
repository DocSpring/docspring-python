# FieldEqualsCondition

A condition on whether a field's value is (or isn't) a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | [**FieldEqualsOperator**](FieldEqualsOperator.md) | How the field's value is compared with `value`. `in`: one of a list. `range`: from `value` to `range_max`. | 
**value** | **object** | The value the field's value is compared with. | 

## Example

```python
from docspring.models.field_equals_condition import FieldEqualsCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldEqualsCondition from a JSON string
field_equals_condition_instance = FieldEqualsCondition.from_json(json)
# print the JSON string representation of the object
print(FieldEqualsCondition.to_json())

# convert the object into a dict
field_equals_condition_dict = field_equals_condition_instance.to_dict()
# create an instance of FieldEqualsCondition from a dict
field_equals_condition_from_dict = FieldEqualsCondition.from_dict(field_equals_condition_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


