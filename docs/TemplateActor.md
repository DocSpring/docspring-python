# TemplateActor

A user in your account, an API token, or someone using the embedded template editor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TemplateActorType**](TemplateActorType.md) | `user`: a user in your account. `api`: an API token. `external_user`: someone using the embedded template editor, as identified by your app. | 
**user_id** | **str** | The user's ID, for `user`. | 
**external_id** | **str** | The ID your app gave the embedded editor's user, for `external_user`. | 
**name** | **str** | The user's name, or the name your app gave the embedded editor's user. | 
**email** | **str** | The email address your app gave the embedded editor's user, for `external_user`. | 

## Example

```python
from docspring.models.template_actor import TemplateActor

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateActor from a JSON string
template_actor_instance = TemplateActor.from_json(json)
# print the JSON string representation of the object
print(TemplateActor.to_json())

# convert the object into a dict
template_actor_dict = template_actor_instance.to_dict()
# create an instance of TemplateActor from a dict
template_actor_from_dict = TemplateActor.from_dict(template_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


