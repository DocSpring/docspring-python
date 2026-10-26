# GenerateSubmissionFilesRequest

The formats to make.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | [**List[GenerateFilesFormat]**](GenerateFilesFormat.md) | The formats to add to the submission's files: `png`, an image of each page of the submission's PDF (up to 100 pages). A format the submission already has (or is making) is left as it is. | 

## Example

```python
from docspring.models.generate_submission_files_request import GenerateSubmissionFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSubmissionFilesRequest from a JSON string
generate_submission_files_request_instance = GenerateSubmissionFilesRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateSubmissionFilesRequest.to_json())

# convert the object into a dict
generate_submission_files_request_dict = generate_submission_files_request_instance.to_dict()
# create an instance of GenerateSubmissionFilesRequest from a dict
generate_submission_files_request_from_dict = GenerateSubmissionFilesRequest.from_dict(generate_submission_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


