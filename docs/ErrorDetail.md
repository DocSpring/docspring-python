# ErrorDetail

One problem with the request, such as a missing or invalid property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | What's wrong: `required`, `unknown_property`, `type`, `enum`, `format`, a JSON Schema keyword such as `minLength`, or a DocSpring code. New codes can be added. | 
**message** | **str** | A human-readable explanation of the problem. | 
**pointer** | **str** | A JSON pointer to the value in the request body (RFC 6901). An empty string means the whole body. In a submission's `data_errors`, it points into the request that created the submission. | [optional] 
**parameter** | **str** | The query parameter or header the detail is about. | [optional] 
**submission_id** | **str** | For a batch item that failed validation, the ID of the submission recorded for it. | [optional] 

## Example

```python
from docspring.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ErrorDetail.to_json())

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_from_dict = ErrorDetail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


