# SuccessErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from docspring.models.success_error_response import SuccessErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessErrorResponse from a JSON string
success_error_response_instance = SuccessErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessErrorResponse.to_json())

# convert the object into a dict
success_error_response_dict = success_error_response_instance.to_dict()
# create an instance of SuccessErrorResponse from a dict
success_error_response_from_dict = SuccessErrorResponse.from_dict(success_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


