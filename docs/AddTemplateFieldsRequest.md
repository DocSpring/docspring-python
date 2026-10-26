# AddTemplateFieldsRequest

The fields to add to the template's draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[FieldInput]**](FieldInput.md) | The fields to add. Settings left out have their defaults, except that a field with the name of other fields takes their shared settings. Shared settings it sets change them for every field with the name. | 

## Example

```python
from docspring.models.add_template_fields_request import AddTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTemplateFieldsRequest from a JSON string
add_template_fields_request_instance = AddTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(AddTemplateFieldsRequest.to_json())

# convert the object into a dict
add_template_fields_request_dict = add_template_fields_request_instance.to_dict()
# create an instance of AddTemplateFieldsRequest from a dict
add_template_fields_request_from_dict = AddTemplateFieldsRequest.from_dict(add_template_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


