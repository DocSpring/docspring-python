# EmailActionList

A page of a template's email actions, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmailAction]**](EmailAction.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.email_action_list import EmailActionList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActionList from a JSON string
email_action_list_instance = EmailActionList.from_json(json)
# print the JSON string representation of the object
print(EmailActionList.to_json())

# convert the object into a dict
email_action_list_dict = email_action_list_instance.to_dict()
# create an instance of EmailActionList from a dict
email_action_list_from_dict = EmailActionList.from_dict(email_action_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


