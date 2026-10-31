# CopyTemplateRequest

Settings for the copy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Default: the template's name followed by a number, such as "Contract (2)". For a published version, the name followed by the version, such as "Contract (v1.2.0)". | [optional] 
**parent_folder_id** | **str** | The folder to put the copy in. Null puts it at the root. Left out, the copy goes in the template's own folder. | [optional] 
**version** | **str** | Copy this published version (`1.2.0`, or `1` for the latest 1.x.x) instead of the draft. | [optional] 

## Example

```python
from docspring.models.copy_template_request import CopyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyTemplateRequest from a JSON string
copy_template_request_instance = CopyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CopyTemplateRequest.to_json())

# convert the object into a dict
copy_template_request_dict = copy_template_request_instance.to_dict()
# create an instance of CopyTemplateRequest from a dict
copy_template_request_from_dict = CopyTemplateRequest.from_dict(copy_template_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


