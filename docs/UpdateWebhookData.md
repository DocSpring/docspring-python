# UpdateWebhookData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **object** |  | 

## Example

```python
from docspring.models.update_webhook_data import UpdateWebhookData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookData from a JSON string
update_webhook_data_instance = UpdateWebhookData.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookData.to_json())

# convert the object into a dict
update_webhook_data_dict = update_webhook_data_instance.to_dict()
# create an instance of UpdateWebhookData from a dict
update_webhook_data_from_dict = UpdateWebhookData.from_dict(update_webhook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


