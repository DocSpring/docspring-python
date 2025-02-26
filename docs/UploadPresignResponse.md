# UploadPresignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **object** |  | 
**headers** | **object** |  | 
**url** | **str** |  | 
**method** | **str** |  | [optional] 

## Example

```python
from docspring.models.upload_presign_response import UploadPresignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPresignResponse from a JSON string
upload_presign_response_instance = UploadPresignResponse.from_json(json)
# print the JSON string representation of the object
print(UploadPresignResponse.to_json())

# convert the object into a dict
upload_presign_response_dict = upload_presign_response_instance.to_dict()
# create an instance of UploadPresignResponse from a dict
upload_presign_response_from_dict = UploadPresignResponse.from_dict(upload_presign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


