# WebhookList

A page of webhooks, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Webhook]**](Webhook.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.webhook_list import WebhookList

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookList from a JSON string
webhook_list_instance = WebhookList.from_json(json)
# print the JSON string representation of the object
print(WebhookList.to_json())

# convert the object into a dict
webhook_list_dict = webhook_list_instance.to_dict()
# create an instance of WebhookList from a dict
webhook_list_from_dict = WebhookList.from_dict(webhook_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


