# RestoreTemplateVersionRequest

The version to restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The published version to restore to the draft (`1.2.0`, or `1` for the latest 1.x.x). | 

## Example

```python
from docspring.models.restore_template_version_request import RestoreTemplateVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreTemplateVersionRequest from a JSON string
restore_template_version_request_instance = RestoreTemplateVersionRequest.from_json(json)
# print the JSON string representation of the object
print(RestoreTemplateVersionRequest.to_json())

# convert the object into a dict
restore_template_version_request_dict = restore_template_version_request_instance.to_dict()
# create an instance of RestoreTemplateVersionRequest from a dict
restore_template_version_request_from_dict = RestoreTemplateVersionRequest.from_dict(restore_template_version_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


