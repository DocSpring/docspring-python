# SignatureRequestReminders

How often DocSpring reminds people who haven't signed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_days** | **int** | Days between reminders. | 
**max_count** | **int** | The most reminders each person gets. | 

## Example

```python
from docspring.models.signature_request_reminders import SignatureRequestReminders

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestReminders from a JSON string
signature_request_reminders_instance = SignatureRequestReminders.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestReminders.to_json())

# convert the object into a dict
signature_request_reminders_dict = signature_request_reminders_instance.to_dict()
# create an instance of SignatureRequestReminders from a dict
signature_request_reminders_from_dict = SignatureRequestReminders.from_dict(signature_request_reminders_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


