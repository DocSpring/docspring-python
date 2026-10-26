# RemoveTemplateFieldsRequest

The fields to remove from the template's draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ids** | **List[int]** | The IDs of the fields to remove. | 

## Example

```python
from docspring.models.remove_template_fields_request import RemoveTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTemplateFieldsRequest from a JSON string
remove_template_fields_request_instance = RemoveTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveTemplateFieldsRequest.to_json())

# convert the object into a dict
remove_template_fields_request_dict = remove_template_fields_request_instance.to_dict()
# create an instance of RemoveTemplateFieldsRequest from a dict
remove_template_fields_request_from_dict = RemoveTemplateFieldsRequest.from_dict(remove_template_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


