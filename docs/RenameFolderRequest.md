# RenameFolderRequest

The folder's new name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The folder's name. It can't contain `/`, and is unique within its parent folder. | 

## Example

```python
from docspring.models.rename_folder_request import RenameFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenameFolderRequest from a JSON string
rename_folder_request_instance = RenameFolderRequest.from_json(json)
# print the JSON string representation of the object
print(RenameFolderRequest.to_json())

# convert the object into a dict
rename_folder_request_dict = rename_folder_request_instance.to_dict()
# create an instance of RenameFolderRequest from a dict
rename_folder_request_from_dict = RenameFolderRequest.from_dict(rename_folder_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


