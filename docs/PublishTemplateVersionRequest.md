# PublishTemplateVersionRequest

The version to publish.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_type** | [**TemplateVersionType**](TemplateVersionType.md) | Which part of the latest version number to increase. | 
**description** | **str** | What changed in the version, shown with it in DocSpring. | [optional] 

## Example

```python
from docspring.models.publish_template_version_request import PublishTemplateVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishTemplateVersionRequest from a JSON string
publish_template_version_request_instance = PublishTemplateVersionRequest.from_json(json)
# print the JSON string representation of the object
print(PublishTemplateVersionRequest.to_json())

# convert the object into a dict
publish_template_version_request_dict = publish_template_version_request_instance.to_dict()
# create an instance of PublishTemplateVersionRequest from a dict
publish_template_version_request_from_dict = PublishTemplateVersionRequest.from_dict(publish_template_version_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


