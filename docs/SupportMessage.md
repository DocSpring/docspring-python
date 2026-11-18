# SupportMessage

A message on a support ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The message's ID. | 
**author** | [**SupportMessageAuthor**](SupportMessageAuthor.md) | `reporter`: your side. `team`: a person at DocSpring. `system`: DocSpring itself. | 
**body** | **str** | The message, as plain text. | 
**created_at** | **datetime** | When the message was sent. | 
**first_read_at** | **datetime** | When one of the team's messages was first returned by the API. It shows that the message was fetched, not that a person read it. Null for your own messages. | 

## Example

```python
from docspring.models.support_message import SupportMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SupportMessage from a JSON string
support_message_instance = SupportMessage.from_json(json)
# print the JSON string representation of the object
print(SupportMessage.to_json())

# convert the object into a dict
support_message_dict = support_message_instance.to_dict()
# create an instance of SupportMessage from a dict
support_message_from_dict = SupportMessage.from_dict(support_message_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


