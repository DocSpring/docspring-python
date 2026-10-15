# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**enabled** | **bool** |  | 
**event_types** | **List[str]** |  | 
**mode** | **str** |  | 
**version** | **int** |  | 
**api_token_ids** | **List[str]** |  | 
**template_ids** | **List[str]** |  | 
**folder_ids** | **List[str]** |  | 
**include_submission_data** | **bool** |  | 
**strip_fields** | **List[str]** |  | 
**headers** | **Dict[str, str]** |  | 
**consecutive_failures** | **int** |  | 
**last_failure_at** | **str** |  | 
**disabled_at** | **str** |  | 
**disabled_reason** | **str** |  | 
**secret** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from docspring.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


