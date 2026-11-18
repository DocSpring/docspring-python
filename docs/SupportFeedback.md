# SupportFeedback

A piece of feedback that was sent to the DocSpring team. Feedback goes one way: nobody replies to it, and it can't be read back or checked later. Open a support ticket when you need an answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The feedback's ID. | 
**received_at** | **datetime** | When DocSpring received it. | 
**follow_up** | **str** | What happens next, in a sentence for an AI agent to act on. Nobody replies to feedback. | 

## Example

```python
from docspring.models.support_feedback import SupportFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of SupportFeedback from a JSON string
support_feedback_instance = SupportFeedback.from_json(json)
# print the JSON string representation of the object
print(SupportFeedback.to_json())

# convert the object into a dict
support_feedback_dict = support_feedback_instance.to_dict()
# create an instance of SupportFeedback from a dict
support_feedback_from_dict = SupportFeedback.from_dict(support_feedback_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


