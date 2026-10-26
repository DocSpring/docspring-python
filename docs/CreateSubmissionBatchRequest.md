# CreateSubmissionBatchRequest

The submissions to create, and the settings they share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Your own data about the batch, such as an ID from your app. | [optional] 
**template_id** | **str** | The template for each submission that doesn't name its own `template_id`. | [optional] 
**template_version** | **str** | The template version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). | [optional] 
**test** | **bool** | The default `test` for each submission that doesn't set its own. | [optional] 
**output_formats** | [**List[OutputFormat]**](OutputFormat.md) | The default `output_formats` for each submission that doesn't set its own. | [optional] 
**submissions** | [**List[SubmissionInput]**](SubmissionInput.md) | Up to 50 submissions. Each one takes the properties of POST /templates/{template_id}/submissions except `signature_requests`, plus `template_id` and `template_version` when it uses a different template from the batch. | 

## Example

```python
from docspring.models.create_submission_batch_request import CreateSubmissionBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionBatchRequest from a JSON string
create_submission_batch_request_instance = CreateSubmissionBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubmissionBatchRequest.to_json())

# convert the object into a dict
create_submission_batch_request_dict = create_submission_batch_request_instance.to_dict()
# create an instance of CreateSubmissionBatchRequest from a dict
create_submission_batch_request_from_dict = CreateSubmissionBatchRequest.from_dict(create_submission_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


