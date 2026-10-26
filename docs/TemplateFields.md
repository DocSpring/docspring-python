# TemplateFields

A template's fields, page by page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | The template's ID. | 
**version** | **str** | The published version the fields are of, such as `1.2.0`. Null for the draft. | 
**fields** | [**List[ModelField]**](ModelField.md) | The fields. | 

## Example

```python
from docspring.models.template_fields import TemplateFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFields from a JSON string
template_fields_instance = TemplateFields.from_json(json)
# print the JSON string representation of the object
print(TemplateFields.to_json())

# convert the object into a dict
template_fields_dict = template_fields_instance.to_dict()
# create an instance of TemplateFields from a dict
template_fields_from_dict = TemplateFields.from_dict(template_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


