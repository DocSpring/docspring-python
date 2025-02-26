# BatchGeneratePdfs201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**submission_batch** | [**SubmissionBatch**](SubmissionBatch.md) |  | 
**submissions** | **List[object]** |  | 

## Example

```python
from docspring.models.batch_generate_pdfs201_response import BatchGeneratePdfs201Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGeneratePdfs201Response from a JSON string
batch_generate_pdfs201_response_instance = BatchGeneratePdfs201Response.from_json(json)
# print the JSON string representation of the object
print(BatchGeneratePdfs201Response.to_json())

# convert the object into a dict
batch_generate_pdfs201_response_dict = batch_generate_pdfs201_response_instance.to_dict()
# create an instance of BatchGeneratePdfs201Response from a dict
batch_generate_pdfs201_response_from_dict = BatchGeneratePdfs201Response.from_dict(batch_generate_pdfs201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


