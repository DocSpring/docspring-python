# FieldPresenceCondition

A condition on whether a field has a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | [**FieldPresenceOperator**](FieldPresenceOperator.md) | How the field's value is compared with `value`. `in`: one of a list. `range`: from `value` to `range_max`. | 

## Example

```python
from docspring.models.field_presence_condition import FieldPresenceCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldPresenceCondition from a JSON string
field_presence_condition_instance = FieldPresenceCondition.from_json(json)
# print the JSON string representation of the object
print(FieldPresenceCondition.to_json())

# convert the object into a dict
field_presence_condition_dict = field_presence_condition_instance.to_dict()
# create an instance of FieldPresenceCondition from a dict
field_presence_condition_from_dict = FieldPresenceCondition.from_dict(field_presence_condition_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


