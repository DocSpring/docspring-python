# CreateSignatureRequestEventRequest

The event to record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**SignatureRequestEventType**](SignatureRequestEventType.md) | `send_request`: you sent the signature request to the person (`message_type` and `message_recipient` are required). It's the only event the API records: DocSpring records everything that happens in the signing form itself, and people decline a signature request in its form. | 
**message_type** | [**SignatureRequestMessageType**](SignatureRequestMessageType.md) | How you sent the request. Required for `send_request`. | [optional] 
**message_recipient** | **str** | Where you sent the request, such as an email address or a phone number. Required for `send_request`. | [optional] 
**occurred_at** | **datetime** | When it happened. Default now. | [optional] 

## Example

```python
from docspring.models.create_signature_request_event_request import CreateSignatureRequestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSignatureRequestEventRequest from a JSON string
create_signature_request_event_request_instance = CreateSignatureRequestEventRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSignatureRequestEventRequest.to_json())

# convert the object into a dict
create_signature_request_event_request_dict = create_signature_request_event_request_instance.to_dict()
# create an instance of CreateSignatureRequestEventRequest from a dict
create_signature_request_event_request_from_dict = CreateSignatureRequestEventRequest.from_dict(create_signature_request_event_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


