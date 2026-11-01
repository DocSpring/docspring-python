# SendAccountEmailActionTestEmailRequest

Which template the test email is for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | A template the email action sends for: the test uses its PDF and name. Left out, it uses the one that changed most recently. | [optional] 

## Example

```python
from docspring.models.send_account_email_action_test_email_request import SendAccountEmailActionTestEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendAccountEmailActionTestEmailRequest from a JSON string
send_account_email_action_test_email_request_instance = SendAccountEmailActionTestEmailRequest.from_json(json)
# print the JSON string representation of the object
print(SendAccountEmailActionTestEmailRequest.to_json())

# convert the object into a dict
send_account_email_action_test_email_request_dict = send_account_email_action_test_email_request_instance.to_dict()
# create an instance of SendAccountEmailActionTestEmailRequest from a dict
send_account_email_action_test_email_request_from_dict = SendAccountEmailActionTestEmailRequest.from_dict(send_account_email_action_test_email_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


