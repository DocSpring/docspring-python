# MoveFolderRequest

Where to move the folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_folder_id** | **str** | The ID of the folder this folder is in. Null for a folder at the root. | 

## Example

```python
from docspring.models.move_folder_request import MoveFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFolderRequest from a JSON string
move_folder_request_instance = MoveFolderRequest.from_json(json)
# print the JSON string representation of the object
print(MoveFolderRequest.to_json())

# convert the object into a dict
move_folder_request_dict = move_folder_request_instance.to_dict()
# create an instance of MoveFolderRequest from a dict
move_folder_request_from_dict = MoveFolderRequest.from_dict(move_folder_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


