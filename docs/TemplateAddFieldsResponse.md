# TemplateAddFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**errors** | **List[str]** |  | [optional] 
**new_field_ids** | **List[int]** |  | [optional] 

## Example

```python
from docspring.models.template_add_fields_response import TemplateAddFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateAddFieldsResponse from a JSON string
template_add_fields_response_instance = TemplateAddFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateAddFieldsResponse.to_json())

# convert the object into a dict
template_add_fields_response_dict = template_add_fields_response_instance.to_dict()
# create an instance of TemplateAddFieldsResponse from a dict
template_add_fields_response_from_dict = TemplateAddFieldsResponse.from_dict(template_add_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


