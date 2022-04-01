# Intersight Cloud Orchestrator 
## Python Examples

This repository contains sample Python code for Intersight Cloud Orchestrator (ICO)<br>
 
### Instructions
1. [Generate an API key and secret from Intersight](https://intersight.com/apidocs/introduction/security/%23generating-api-keys&sa=D&ust=1612024909729000&usg=AOvVaw362rkbFxqhX_Mo8w0xkDJG/#generating-api-keys)
2. Take note of the `API Key ID`, download and store the `Secret Key` in your filesystem
3. Set the `INTERSIGHT_API_KEY_ID` and the `INTERSIGHT_API_PRIVATE_KEY` environment variables with the `Api Key ID` and the `Secret Key` path respectively. The `env-linux-mac-example.sh` file contains an example for Linux and MacOS.
4. (optional) Create a Virtualenv: `python3 -m venv .venv && source .venv/bin/activate`
5. Install Intersight Python SDK: `pip install intersight`

<hr>

### Examples for Workflows

<b>Use Case 1</b>: Get all Workflows<br>
Script: `ico_wf_get_definitions_list.py`<br>
Returns: All workflow definitions data in JSON format<br>

<b>Use Case 2</b>: Get Definition of a Specific Workflow<br>
Script: `ico_wf_get_definition_by_name.py`<br>
Usage: Set the `workflow_name` variable with the workflow name you want to fetch (i.e. "Deploy a Virtual Machine"<br>
Returns: Server response in JSON format of the requested workflow definition<br>

<b>Use Case 3</b>: Get all Requests<br>
Script: `ico_wf_get_requests_list.py`<br>
Returns: All execution requests data in JSON format<br>

<b>Use Case 4</b>: Get a specific Request<br>
Script: `ico_wf_get_request_by_moid.py`<br>
Usage: Set the `moid` variable with the request moid you want to fetch<br>
Returns: Server response in JSON format of the requested workflow execution<br>

<b>Use Case 5</b>: Get Task Outputs of a specific Workflow Execution<br>
Script: `ico_wf_get_request_tasks_outputs_by_moid.py`<br>
Usage: Set the `moid` variable with the request moid you want to fetch<br>
Returns: Outputs of the Task Executed in the specific request<br>

<b>Use Case 6</b>: Execute a Workflow<br>
Script: `ico_wf_execute_by_name.py`<br>
Usage: Set variables based on your workflow definition (see code for examples)<br>
Returns: Server response in JSON format, a summary of the request moid and the user who invoked the execution<br>

<b>Use Case 7</b>: Rollback a Workflow<br>
Script: `ico_wf_rollback_by_moid.py`<br>
Usage: Set the `workflow_moid` variable with the request moid you want to rollback<br>
Returns: Moid of the rollback request, Moid of the rollbacked request and Status<br>

<hr>

### Examples for Tasks

<b>Use Case 1</b>: Get Tasks Definitions <br>
Script: `ico_tasks_get_definitions_list.py`<br>
Returns: All tasks definitions data in JSON format<br>

<b>Use Case 2</b>: Get Task Definition by Name<br>
Script: `ico_tasks_get_definition_by_name.py`<br>
Usage: Set the `name` variable with the task moid you want to fetch<br>
Returns: Server response in JSON format of the requested task definition<br>

<b>Use Case 3</b>: Get Task Definition by Moid<br>
Script: `ico_tasks_get_definition_by_moid.py`<br>
Usage: Set the `moid` variable with the task moid you want to fetch<br>
Returns: Server response in JSON format of the requested task definition<br>

<hr>

### Examples for Data Types

<b>Use Case 1</b>: Get Data Types Definitions <br>
Script: `ico_datatypes_get_definitions_list.py`<br>
Returns: All Data Types definitions data in JSON format<br>

<b>Use Case 2</b>: Get Data Type Definition by Moid<br>
Script: `ico_datatypes_get_definition_by_moid.py`<br>
Usage: Set the `moid` variable with the task moid you want to fetch<br>
Returns: Server response in JSON format of the requested Data Type definition<br>

<hr>

### Example for Summaries

<b>Use Case</b>: Show ICO Workflows, Tasks and Data Types summary stats <br>
Script: `ico_statistics_get.py`<br>
Sample Output:<br>

```
### Workflow Designer Statistics ###

Total Workflows: 157
System Workflows: 29
User Workflows: 128
Valid/Invalid Workflows: 146/11

### Executions Statistics ###

Total Executions: 633
Success/Failed Executions: 387/246
Last Request: "Rollback Deploy a Virtual Machine", by user user@cisco.com, with Moid 624739d1696f6e2d315a1b21

### Task Designer Statistics ###

Total Tasks: 221
System Tasks: 145
Custom Tasks: 76

### Data Types Statistics ###

Total Data Types: 226
System Data Types: 211
Custom Data Types: 15
```

