# UpdateWebhookRequest

The settings to change. Properties left out keep their values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the webhook, shown in the dashboard. | [optional] 
**url** | **str** | The endpoint that receives webhook POST requests. | [optional] 
**enabled** | **bool** | Whether DocSpring sends events to the webhook. Webhooks are disabled after repeated failures. | [optional] 
**event_types** | [**List[WebhookEventType]**](WebhookEventType.md) | The events the webhook subscribes to. A webhook made in the dashboard can also subscribe to API token, account integration and user events, which are listed with their own names. | [optional] 
**mode** | [**WebhookMode**](WebhookMode.md) | Only send events for test or live submissions. Null sends both. | [optional] 
**api_token_ids** | **List[str]** | Only send events from these API tokens. Combined with the other scope lists using OR. Applies to submission, signature request, combined PDF, submission batch and custom file events. | [optional] 
**template_ids** | **List[str]** | Only send events for these templates. Combined with the other scope lists using OR. Applies to submission, signature request and template events. | [optional] 
**folder_ids** | **List[str]** | Only send events for templates in these folders, including their subfolders. Combined with the other scope lists using OR. Applies to submission, signature request, template and folder events. | [optional] 
**include_submission_data** | **bool** | Include the submission's field data in the payload. When false, the submission's data and truncated_text, and each signature request's data, ip_address and user_agent, are null. | [optional] 
**strip_fields** | **List[str]** | Dot-separated paths to remove from the event's data object. Form fields live under `data` (`data.ssn` removes the ssn field). A bare name removes a top-level key (`metadata` removes the whole metadata object). | [optional] 
**headers** | **Dict[str, str]** | Headers to send with each request. | [optional] 

## Example

```python
from docspring.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


