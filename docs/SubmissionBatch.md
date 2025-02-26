# SubmissionBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**state** | **str** |  | 
**metadata** | **object** |  | 
**processed_at** | **str** |  | 
**total_count** | **int** |  | 
**pending_count** | **int** |  | 
**error_count** | **int** |  | 
**completion_percentage** | **float** |  | 

## Example

```python
from docspring.models.submission_batch import SubmissionBatch

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionBatch from a JSON string
submission_batch_instance = SubmissionBatch.from_json(json)
# print the JSON string representation of the object
print(SubmissionBatch.to_json())

# convert the object into a dict
submission_batch_dict = submission_batch_instance.to_dict()
# create an instance of SubmissionBatch from a dict
submission_batch_from_dict = SubmissionBatch.from_dict(submission_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


