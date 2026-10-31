# CreateFolderRequest

The folder to create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The folder's name. It can't contain `/`, and is unique within its parent folder. | 
**parent_folder_id** | **str** | The ID of the folder this folder is in. Null for a folder at the root. | [optional] 

## Example

```python
from docspring.models.create_folder_request import CreateFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderRequest from a JSON string
create_folder_request_instance = CreateFolderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFolderRequest.to_json())

# convert the object into a dict
create_folder_request_dict = create_folder_request_instance.to_dict()
# create an instance of CreateFolderRequest from a dict
create_folder_request_from_dict = CreateFolderRequest.from_dict(create_folder_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


