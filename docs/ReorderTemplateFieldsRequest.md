# ReorderTemplateFieldsRequest

The new order of the fields in the template's draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ids** | **List[int]** | The ID of every field, in the new order. Each field stays on its page, and a page's fields take the order their IDs have here: the order they're printed in (a later field prints over an earlier one where they overlap), and the order of their values in the template's data schema and forms. | 

## Example

```python
from docspring.models.reorder_template_fields_request import ReorderTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderTemplateFieldsRequest from a JSON string
reorder_template_fields_request_instance = ReorderTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(ReorderTemplateFieldsRequest.to_json())

# convert the object into a dict
reorder_template_fields_request_dict = reorder_template_fields_request_instance.to_dict()
# create an instance of ReorderTemplateFieldsRequest from a dict
reorder_template_fields_request_from_dict = ReorderTemplateFieldsRequest.from_dict(reorder_template_fields_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


