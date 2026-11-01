# EmailActionTestEmail

A test email that was sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent_to** | **str** | The address the test email went to, the email address of the API token's user. | 

## Example

```python
from docspring.models.email_action_test_email import EmailActionTestEmail

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActionTestEmail from a JSON string
email_action_test_email_instance = EmailActionTestEmail.from_json(json)
# print the JSON string representation of the object
print(EmailActionTestEmail.to_json())

# convert the object into a dict
email_action_test_email_dict = email_action_test_email_instance.to_dict()
# create an instance of EmailActionTestEmail from a dict
email_action_test_email_from_dict = EmailActionTestEmail.from_dict(email_action_test_email_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


