# CustomFile

A PDF you uploaded to merge with other PDFs (POST /combined_pdfs). Get an upload URL with GET /uploads/presign first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The custom file's ID. | 
**download_url** | **str** | A temporary link to download the file. | 
**size** | **int** | The file's size in bytes. | 
**content_type** | **str** | The file's media type, such as `application/pdf`. | 
**created_at** | **datetime** | When the custom file was created. | 
**updated_at** | **datetime** | When the custom file was last updated. | 

## Example

```python
from docspring.models.custom_file import CustomFile

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFile from a JSON string
custom_file_instance = CustomFile.from_json(json)
# print the JSON string representation of the object
print(CustomFile.to_json())

# convert the object into a dict
custom_file_dict = custom_file_instance.to_dict()
# create an instance of CustomFile from a dict
custom_file_from_dict = CustomFile.from_dict(custom_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


