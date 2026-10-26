# TemplateFieldMove

A field that moved in a template's field order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The field's ID. | 
**old_index** | **int** | Its place in `from_version`'s field order, starting at 0. | 
**new_index** | **int** | Its place in `to_version`'s field order, starting at 0. | 

## Example

```python
from docspring.models.template_field_move import TemplateFieldMove

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldMove from a JSON string
template_field_move_instance = TemplateFieldMove.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldMove.to_json())

# convert the object into a dict
template_field_move_dict = template_field_move_instance.to_dict()
# create an instance of TemplateFieldMove from a dict
template_field_move_from_dict = TemplateFieldMove.from_dict(template_field_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


