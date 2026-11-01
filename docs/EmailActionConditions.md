# EmailActionConditions

The conditions a submission's values must meet for an email action to send its email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**TemplateFieldDependencyMatch**](TemplateFieldDependencyMatch.md) | Whether all of the conditions (the default) or any of them must be met. | [optional] 
**conditions** | [**List[TemplateFieldDependencyCondition]**](TemplateFieldDependencyCondition.md) | The conditions on other fields' values. | 

## Example

```python
from docspring.models.email_action_conditions import EmailActionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActionConditions from a JSON string
email_action_conditions_instance = EmailActionConditions.from_json(json)
# print the JSON string representation of the object
print(EmailActionConditions.to_json())

# convert the object into a dict
email_action_conditions_dict = email_action_conditions_instance.to_dict()
# create an instance of EmailActionConditions from a dict
email_action_conditions_from_dict = EmailActionConditions.from_dict(email_action_conditions_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


