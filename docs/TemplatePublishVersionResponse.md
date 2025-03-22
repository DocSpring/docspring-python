# TemplatePublishVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**result** | **object** |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from docspring.models.template_publish_version_response import TemplatePublishVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePublishVersionResponse from a JSON string
template_publish_version_response_instance = TemplatePublishVersionResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatePublishVersionResponse.to_json())

# convert the object into a dict
template_publish_version_response_dict = template_publish_version_response_instance.to_dict()
# create an instance of TemplatePublishVersionResponse from a dict
template_publish_version_response_from_dict = TemplatePublishVersionResponse.from_dict(template_publish_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


