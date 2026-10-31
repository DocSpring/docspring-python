# Folder

A folder of templates. Folders can contain other folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The folder's ID. | 
**name** | **str** | The folder's name. It can't contain `/`, and is unique within its parent folder. | 
**path** | **str** | The path of the folder this folder is in, such as `/Contracts`. `/` for a folder at the root. | 
**parent_folder_id** | **str** | The ID of the folder this folder is in. Null for a folder at the root. | 
**created_at** | **datetime** | When the folder was created. | 
**updated_at** | **datetime** | When the folder was last updated. | 

## Example

```python
from docspring.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print(Folder.to_json())

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


