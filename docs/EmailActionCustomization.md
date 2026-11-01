# EmailActionCustomization

A template's changes to an account email action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the account email action sends for this template. It also needs to be on itself (`enabled`). | 
**customized** | [**List[EmailActionSetting]**](EmailActionSetting.md) | The settings this template changes. The others follow the account email action. | 
**consecutive_failures** | **int** | How many of this template's emails in a row have failed because of a setting it changes. | 
**failing_since** | **datetime** | When the current run of those failures started. | 
**last_failure_at** | **datetime** | When one of those emails last failed. | 
**last_failure_message** | **str** | Why it failed. | 
**disabled_at** | **datetime** | When DocSpring turned the email action off for this template, such as when an address the template added bounced. | 
**disabled_reason** | **str** | Why DocSpring turned it off for this template. | 
**created_at** | **datetime** | When the template first changed the email action. | 
**updated_at** | **datetime** | When the template's changes last changed. | 

## Example

```python
from docspring.models.email_action_customization import EmailActionCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActionCustomization from a JSON string
email_action_customization_instance = EmailActionCustomization.from_json(json)
# print the JSON string representation of the object
print(EmailActionCustomization.to_json())

# convert the object into a dict
email_action_customization_dict = email_action_customization_instance.to_dict()
# create an instance of EmailActionCustomization from a dict
email_action_customization_from_dict = EmailActionCustomization.from_dict(email_action_customization_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


