# CreatePdfSubmissionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**data_requests** | [**List[CreateSubmissionDataRequestData]**](CreateSubmissionDataRequestData.md) |  | [optional] 
**editable** | **bool** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**field_overrides** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**password** | **str** |  | [optional] 
**test** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from docspring.models.create_pdf_submission_data import CreatePdfSubmissionData

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePdfSubmissionData from a JSON string
create_pdf_submission_data_instance = CreatePdfSubmissionData.from_json(json)
# print the JSON string representation of the object
print(CreatePdfSubmissionData.to_json())

# convert the object into a dict
create_pdf_submission_data_dict = create_pdf_submission_data_instance.to_dict()
# create an instance of CreatePdfSubmissionData from a dict
create_pdf_submission_data_from_dict = CreatePdfSubmissionData.from_dict(create_pdf_submission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


