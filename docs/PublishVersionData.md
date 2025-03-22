# PublishVersionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**version_type** | **str** |  | 

## Example

```python
from docspring.models.publish_version_data import PublishVersionData

# TODO update the JSON string below
json = "{}"
# create an instance of PublishVersionData from a JSON string
publish_version_data_instance = PublishVersionData.from_json(json)
# print the JSON string representation of the object
print(PublishVersionData.to_json())

# convert the object into a dict
publish_version_data_dict = publish_version_data_instance.to_dict()
# create an instance of PublishVersionData from a dict
publish_version_data_from_dict = PublishVersionData.from_dict(publish_version_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


