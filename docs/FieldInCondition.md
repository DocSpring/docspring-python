# FieldInCondition

A condition on whether a field's value is one of a list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field whose value is compared. | 
**operator** | **str** | Must be `in`. | [default to 'in']
**value** | **List[object]** | The values the field's value must be one of. | 

## Example

```python
from docspring.models.field_in_condition import FieldInCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldInCondition from a JSON string
field_in_condition_instance = FieldInCondition.from_json(json)
# print the JSON string representation of the object
print(FieldInCondition.to_json())

# convert the object into a dict
field_in_condition_dict = field_in_condition_instance.to_dict()
# create an instance of FieldInCondition from a dict
field_in_condition_from_dict = FieldInCondition.from_dict(field_in_condition_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


