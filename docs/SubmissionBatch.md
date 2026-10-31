# SubmissionBatch

Submissions created together in one request. Their files are only generated when every submission in the batch is valid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The batch's ID. | 
**state** | [**SubmissionBatchState**](SubmissionBatchState.md) | `pending` while the files are being generated, then `processed`. `error` as soon as a submission fails, while the others can still be pending: the batch has finished once `processed_at` is set. | 
**metadata** | **Dict[str, object]** | Your own data about the batch, such as an ID from your app. | 
**total_count** | **int** | The number of submissions in the request. | 
**pending_count** | **int** | The submissions whose files haven't been generated yet. | 
**error_count** | **int** | The submissions that were invalid or whose files couldn't be generated. | 
**completion_percentage** | **int** | The percentage of the batch's submissions that have finished, from 0 to 100. | 
**submissions** | [**List[Submission]**](Submission.md) | The batch's submissions, in the order of the request. Their `data` is null unless you pass `include_data=true`. A batch that failed validation only has the submissions that were recorded as `invalid_data`. | 
**processed_at** | **datetime** | When every submission had finished. | 
**created_at** | **datetime** | When the batch was created. | 
**updated_at** | **datetime** | When the batch was last updated. | 

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
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


