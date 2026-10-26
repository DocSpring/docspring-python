# GeneratedFile

A file that DocSpring generated, such as a submission's PDF. A file made after its submission was processed is listed while it's being made: check its `state` before using its links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**GeneratedFileState**](GeneratedFileState.md) | `processed` once the file has been made. `pending` while it's being made, and `error` if it couldn't be made (see `error_message`). | 
**error_message** | **str** | Why the file couldn't be made, when `state` is `error`. | 
**download_url** | **str** | A temporary link to download the file. Null until the file has been made, and when your account turns off download links for submissions. | 
**permanent_url** | **str** | A link to download the file that doesn't expire: it redirects to a new temporary link. It needs your API token or a signed-in session, except for a submission of a template that makes its submissions public. Null until the file has been made. | 
**filename** | **str** | The file's name, such as `sub_123.pdf`. | 
**content_type** | **str** | The file's media type, such as `application/pdf`. | 
**size** | **int** | The file's size in bytes. Null until the file has been made. | 
**sha256** | **str** | The SHA-256 hash of the file. Null until the file has been made. | 

## Example

```python
from docspring.models.generated_file import GeneratedFile

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedFile from a JSON string
generated_file_instance = GeneratedFile.from_json(json)
# print the JSON string representation of the object
print(GeneratedFile.to_json())

# convert the object into a dict
generated_file_dict = generated_file_instance.to_dict()
# create an instance of GeneratedFile from a dict
generated_file_from_dict = GeneratedFile.from_dict(generated_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


