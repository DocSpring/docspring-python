# SupportHelpTurn

One turn of a conversation with DocSpring's AI help.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**SupportHelpTurnRole**](SupportHelpTurnRole.md) | `user`: a question. `assistant`: an answer. | 
**text** | **str** | What was said. | 

## Example

```python
from docspring.models.support_help_turn import SupportHelpTurn

# TODO update the JSON string below
json = "{}"
# create an instance of SupportHelpTurn from a JSON string
support_help_turn_instance = SupportHelpTurn.from_json(json)
# print the JSON string representation of the object
print(SupportHelpTurn.to_json())

# convert the object into a dict
support_help_turn_dict = support_help_turn_instance.to_dict()
# create an instance of SupportHelpTurn from a dict
support_help_turn_from_dict = SupportHelpTurn.from_dict(support_help_turn_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


