# ForbiddenErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from docspring.models.forbidden_error_response import ForbiddenErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenErrorResponse from a JSON string
forbidden_error_response_instance = ForbiddenErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ForbiddenErrorResponse.to_json())

# convert the object into a dict
forbidden_error_response_dict = forbidden_error_response_instance.to_dict()
# create an instance of ForbiddenErrorResponse from a dict
forbidden_error_response_from_dict = ForbiddenErrorResponse.from_dict(forbidden_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


