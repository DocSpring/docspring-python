# SupportReportAgent

An AI agent, as it describes itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The agent's name, such as `Claude Code`. | [optional] 
**version** | **str** | The agent's version. | [optional] 
**model** | **str** | The model the agent runs on. | [optional] 

## Example

```python
from docspring.models.support_report_agent import SupportReportAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SupportReportAgent from a JSON string
support_report_agent_instance = SupportReportAgent.from_json(json)
# print the JSON string representation of the object
print(SupportReportAgent.to_json())

# convert the object into a dict
support_report_agent_dict = support_report_agent_instance.to_dict()
# create an instance of SupportReportAgent from a dict
support_report_agent_from_dict = SupportReportAgent.from_dict(support_report_agent_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


