# CustomFileList

A page of custom files, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomFile]**](CustomFile.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.custom_file_list import CustomFileList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFileList from a JSON string
custom_file_list_instance = CustomFileList.from_json(json)
# print the JSON string representation of the object
print(CustomFileList.to_json())

# convert the object into a dict
custom_file_list_dict = custom_file_list_instance.to_dict()
# create an instance of CustomFileList from a dict
custom_file_list_from_dict = CustomFileList.from_dict(custom_file_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


