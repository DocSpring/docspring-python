# AuthenticationCheck

Returned when the Authorization header has a valid API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** | Always true. | 

## Example

```python
from docspring.models.authentication_check import AuthenticationCheck

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationCheck from a JSON string
authentication_check_instance = AuthenticationCheck.from_json(json)
# print the JSON string representation of the object
print(AuthenticationCheck.to_json())

# convert the object into a dict
authentication_check_dict = authentication_check_instance.to_dict()
# create an instance of AuthenticationCheck from a dict
authentication_check_from_dict = AuthenticationCheck.from_dict(authentication_check_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


