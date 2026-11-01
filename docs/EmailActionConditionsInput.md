# EmailActionConditionsInput

The conditions a submission's values must meet for an email action to send its email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**TemplateFieldDependencyMatch**](TemplateFieldDependencyMatch.md) | Whether all of the conditions (the default) or any of them must be met. | [optional] 
**conditions** | [**List[TemplateFieldDependencyConditionInput]**](TemplateFieldDependencyConditionInput.md) | The conditions on other fields' values. | 

## Example

```python
from docspring.models.email_action_conditions_input import EmailActionConditionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActionConditionsInput from a JSON string
email_action_conditions_input_instance = EmailActionConditionsInput.from_json(json)
# print the JSON string representation of the object
print(EmailActionConditionsInput.to_json())

# convert the object into a dict
email_action_conditions_input_dict = email_action_conditions_input_instance.to_dict()
# create an instance of EmailActionConditionsInput from a dict
email_action_conditions_input_from_dict = EmailActionConditionsInput.from_dict(email_action_conditions_input_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


