# TemplateDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**errors** | **List[str]** |  | [optional] 
**latest_version** | **str** |  | [optional] 
**versions** | **List[object]** |  | [optional] 

## Example

```python
from docspring.models.template_delete_response import TemplateDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDeleteResponse from a JSON string
template_delete_response_instance = TemplateDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateDeleteResponse.to_json())

# convert the object into a dict
template_delete_response_dict = template_delete_response_instance.to_dict()
# create an instance of TemplateDeleteResponse from a dict
template_delete_response_from_dict = TemplateDeleteResponse.from_dict(template_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


