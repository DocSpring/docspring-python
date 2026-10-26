# TemplateVersion

A published version of a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version number, such as `1.2.0`. | 
**description** | **str** | What changed in the version, as written when it was published. | 
**published_at** | **datetime** | When the version was published. | 
**published_by** | [**TemplateActor**](TemplateActor.md) | Who published the version. Null when that wasn't recorded. | 

## Example

```python
from docspring.models.template_version import TemplateVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersion from a JSON string
template_version_instance = TemplateVersion.from_json(json)
# print the JSON string representation of the object
print(TemplateVersion.to_json())

# convert the object into a dict
template_version_dict = template_version_instance.to_dict()
# create an instance of TemplateVersion from a dict
template_version_from_dict = TemplateVersion.from_dict(template_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


