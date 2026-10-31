# GenerateSubmissionFilesRequest

The formats to make.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | [**List[GenerateFilesFormat]**](GenerateFilesFormat.md) | The formats to add to the submission's files: `pdf`, the PDF of a Word template's submission that didn't make one (converted from its Word document); `docx`, the Word document of a Word template's submission that didn't make one (made again from the submission's data and the template version it used); `odt`, the OpenDocument file of a Word template's submission that didn't make one (converted from its Word document); and `png`, an image of each page of the PDF (up to 100 pages), which makes the PDF first if the submission doesn't have one. A submission without a Word document makes it again for `pdf` and `odt`, without keeping it. A format the submission already has (or is making) is left as it is. | 

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
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


