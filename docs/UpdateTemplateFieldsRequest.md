# UpdateTemplateFieldsRequest

The fields to change in the template's draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[FieldInput]**](FieldInput.md) | The changes, each with the `id` of the field it changes. Settings left out keep their values. Changing a shared setting changes it for every field with the same name. Renaming a field moves it to the shared settings of its new name, and conditional logic and formulas that use the old name follow it when no other field has that name. | 

## Example

```python
from docspring.models.update_template_fields_request import UpdateTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateFieldsRequest from a JSON string
update_template_fields_request_instance = UpdateTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateFieldsRequest.to_json())

# convert the object into a dict
update_template_fields_request_dict = update_template_fields_request_instance.to_dict()
# create an instance of UpdateTemplateFieldsRequest from a dict
update_template_fields_request_from_dict = UpdateTemplateFieldsRequest.from_dict(update_template_fields_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


