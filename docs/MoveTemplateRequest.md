# MoveTemplateRequest

Where to move the template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_folder_id** | **str** | The folder to move the template and all of its published versions to. Null moves them to the root. | 

## Example

```python
from docspring.models.move_template_request import MoveTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveTemplateRequest from a JSON string
move_template_request_instance = MoveTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(MoveTemplateRequest.to_json())

# convert the object into a dict
move_template_request_dict = move_template_request_instance.to_dict()
# create an instance of MoveTemplateRequest from a dict
move_template_request_from_dict = MoveTemplateRequest.from_dict(move_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


