# CreateWebhookData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **object** |  | 

## Example

```python
from docspring.models.create_webhook_data import CreateWebhookData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookData from a JSON string
create_webhook_data_instance = CreateWebhookData.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookData.to_json())

# convert the object into a dict
create_webhook_data_dict = create_webhook_data_instance.to_dict()
# create an instance of CreateWebhookData from a dict
create_webhook_data_from_dict = CreateWebhookData.from_dict(create_webhook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


