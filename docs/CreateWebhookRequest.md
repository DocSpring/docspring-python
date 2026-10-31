# CreateWebhookRequest

The webhook to create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the webhook, shown in the dashboard. | [optional] 
**url** | **str** | The endpoint that receives webhook POST requests. | 
**enabled** | **bool** | Whether DocSpring sends events to the webhook. Webhooks are disabled after repeated failures. | [optional] 
**event_types** | [**List[WebhookEventType]**](WebhookEventType.md) | The events the webhook subscribes to. A webhook made in the dashboard can also subscribe to API token, account integration and user events, which are listed with their own names. | 
**mode** | [**WebhookMode**](WebhookMode.md) | Only send events for test or live submissions. Null sends both. | [optional] 
**api_token_ids** | **List[str]** | Only send events from these API tokens. Combined with the other scope lists using OR. Applies to submission, signature request, combined PDF, submission batch and custom file events. | [optional] 
**template_ids** | **List[str]** | Only send events for these templates. Combined with the other scope lists using OR. Applies to submission, signature request and template events. | [optional] 
**folder_ids** | **List[str]** | Only send events for templates in these folders, including their subfolders. Combined with the other scope lists using OR. Applies to submission, signature request, template and folder events. | [optional] 
**include_submission_data** | **bool** | Include the submission's field data in the payload. When false, the submission's data and truncated_text, and each signature request's data, ip_address and user_agent, are null. | [optional] 
**strip_fields** | **List[str]** | Dot-separated paths to remove from the event's data object. Form fields live under `data` (`data.ssn` removes the ssn field). A bare name removes a top-level key (`metadata` removes the whole metadata object). | [optional] 
**headers** | **Dict[str, str]** | Headers to send with each request. | [optional] 

## Example

```python
from docspring.models.create_webhook_request import CreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookRequest from a JSON string
create_webhook_request_instance = CreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookRequest.to_json())

# convert the object into a dict
create_webhook_request_dict = create_webhook_request_instance.to_dict()
# create an instance of CreateWebhookRequest from a dict
create_webhook_request_from_dict = CreateWebhookRequest.from_dict(create_webhook_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


