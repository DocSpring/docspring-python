# FieldGroup

A group of a template's fields: the fields whose names start with the group's name and a `/`. In submission data, a group is an object, or an array for a list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The group's name: `address` for the field `address/city`. A list's item numbers are written as `~`, so the fields `items/0/price` and `items/1/price` are in the groups `items` and `items/~`, the list's items. | 
**type** | [**FieldGroupType**](FieldGroupType.md) | `array` for a list, whose fields' names number its items after the group's name (`items/0/price`, or `items/~/price` in an HTML template), and `object` for the other groups. | 
**title** | **str** | The group's title in the template's data schema and on forms. When it's empty, a title is made from the group's name. | 
**description** | **str** | Help text for the group, added to the template's data schema and shown on forms. | 
**metadata** | **str** | Text for your own use, added to the template's data schema as `x-metadata`. DocSpring doesn't use it. | 
**min_items** | **int** | Lists only (`type` `array`): the fewest items submission data must have. Null for no minimum. | 
**max_items** | **int** | HTML templates' lists only: the most items submission data can have. Null for no limit. A PDF template's list takes as many items as its fields are numbered for, or more with `allow_additional_items`. | 
**allow_additional_items** | **bool** | PDF templates' lists only: submission data can have more items than the list's fields are numbered for. Default false. | 

## Example

```python
from docspring.models.field_group import FieldGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FieldGroup from a JSON string
field_group_instance = FieldGroup.from_json(json)
# print the JSON string representation of the object
print(FieldGroup.to_json())

# convert the object into a dict
field_group_dict = field_group_instance.to_dict()
# create an instance of FieldGroup from a dict
field_group_from_dict = FieldGroup.from_dict(field_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


