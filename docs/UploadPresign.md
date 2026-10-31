# UploadPresign

A presigned S3 form for uploading a file. POST `fields` and the file (as `file`, last) to `url` as multipart/form-data. Then use `fields.key` as the `cache_id` when you create a custom file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The S3 URL to upload the file to. | 
**method** | [**UploadMethod**](UploadMethod.md) | The HTTP method for the upload. | 
**fields** | **Dict[str, str]** | Form fields to send with the file. Send them all, as they are. `key` is the uploaded file's ID: pass it as `cache_id`. | 
**headers** | **Dict[str, str]** | Headers to send with the upload. | 

## Example

```python
from docspring.models.upload_presign import UploadPresign

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPresign from a JSON string
upload_presign_instance = UploadPresign.from_json(json)
# print the JSON string representation of the object
print(UploadPresign.to_json())

# convert the object into a dict
upload_presign_dict = upload_presign_instance.to_dict()
# create an instance of UploadPresign from a dict
upload_presign_from_dict = UploadPresign.from_dict(upload_presign_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


