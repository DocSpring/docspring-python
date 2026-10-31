# TemplateModelCode

Typed code for the template's submission data, for an app that creates submissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | [**ModelCodeLanguage**](ModelCodeLanguage.md) | The language of `code`. | 
**root_type_name** | **str** | The name of the type for the whole submission data object. | 
**code** | **str** | The source code of the types, starting with `root_type_name`. | 

## Example

```python
from docspring.models.template_model_code import TemplateModelCode

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateModelCode from a JSON string
template_model_code_instance = TemplateModelCode.from_json(json)
# print the JSON string representation of the object
print(TemplateModelCode.to_json())

# convert the object into a dict
template_model_code_dict = template_model_code_instance.to_dict()
# create an instance of TemplateModelCode from a dict
template_model_code_from_dict = TemplateModelCode.from_dict(template_model_code_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


