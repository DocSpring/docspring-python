# SignatureRequestEvent

Something that happened to a signature request outside DocSpring, for its audit trail: you sent the request to the person (`send_request`). The audit trail shows it as reported by your account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event's ID. | 
**submission_id** | **str** | The ID of the signature request's submission. | 
**signature_request_id** | **str** | The ID of the signature request. | 
**event_type** | [**SignatureRequestEventType**](SignatureRequestEventType.md) | What happened. | 
**message_type** | [**SignatureRequestMessageType**](SignatureRequestMessageType.md) | How you sent the request. Required for `send_request`. | 
**message_recipient** | **str** | Where you sent the request, such as an email address or a phone number. Required for `send_request`. | 
**occurred_at** | **datetime** | When it happened. Default now. | 
**created_at** | **datetime** | When the event was recorded. | 

## Example

```python
from docspring.models.signature_request_event import SignatureRequestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestEvent from a JSON string
signature_request_event_instance = SignatureRequestEvent.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestEvent.to_json())

# convert the object into a dict
signature_request_event_dict = signature_request_event_instance.to_dict()
# create an instance of SignatureRequestEvent from a dict
signature_request_event_from_dict = SignatureRequestEvent.from_dict(signature_request_event_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


