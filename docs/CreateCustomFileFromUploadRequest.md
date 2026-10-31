# CreateCustomFileFromUploadRequest

The uploaded file to create the custom file from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **str** | The `fields.key` from GET /uploads/presign, after you upload the file to its URL. | 

## Example

```python
from docspring.models.create_custom_file_from_upload_request import CreateCustomFileFromUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFileFromUploadRequest from a JSON string
create_custom_file_from_upload_request_instance = CreateCustomFileFromUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomFileFromUploadRequest.to_json())

# convert the object into a dict
create_custom_file_from_upload_request_dict = create_custom_file_from_upload_request_instance.to_dict()
# create an instance of CreateCustomFileFromUploadRequest from a dict
create_custom_file_from_upload_request_from_dict = CreateCustomFileFromUploadRequest.from_dict(create_custom_file_from_upload_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


