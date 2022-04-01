from itertools import count
import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException

# Query Options
filter_query="(Properties.ExternalMeta eq true) and (Name ne 'DeployHyperFlexSDWAN') and (DefaultVersion eq true)"

# Get Workflows Function
def get_workflow_definitions(api_client):
    """ Gets the list of workflows """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_workflow_definition_list(filter=filter_query,top=0,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_definition_list: %s\n" % e)

# Get Requests Function
def get_workflow_requests(api_client):
    """ Gets the list of workflows executions/requests """
    req_filter = "(Type ne 'ANSIBLE_MONITORING') and (Status ne 'TIMED_OUT') and (Status ne 'NotStarted') and (Internal ne true)"
    order_by='CreateTime desc'
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_workflow_info_list(orderby=order_by,filter=req_filter,top=0,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_info_list: %s\n" % e)

# Get Tasks Function 
def get_tasks_definitions(api_client):
    """ Gets the list of tasks """
    api_instance = workflow_api.WorkflowApi(api_client)
    tasks_filter = "(Properties.ExternalMeta eq true) and (DefaultVersion eq true) and (Tags/any(t:t/Key eq 'cisco.meta.taskType' and t/Value eq 'Interface'))"

    try:
        api_response = api_instance.get_workflow_task_definition_list(filter=tasks_filter,top=0,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_definition_list: %s\n" % e)

# Get Data Types
def get_data_types(api_client):
    """ Gets the list of data types """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_custom_data_type_definition_list(top=0,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_custom_data_type_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get workflows stats
wf_definitions = get_workflow_definitions(api_client)
user_wfs = 0
valid_wfs = 0
for wf in wf_definitions:
    if wf['SharedScope'] == '': 
        user_wfs += 1
    if wf['ValidationInformation']['State'] == 'Valid':
        valid_wfs +=1

# Get requests stats
requests = get_workflow_requests(api_client)
success_requests = 0
for request in requests:
    if request['Status'] == 'COMPLETED':
        success_requests +=1


# Get Tasks stats
tasks = get_tasks_definitions(api_client)
system_tasks = 0
for task in tasks:
    if task['SharedScope'] == 'shared':
        system_tasks +=1

# Get Data Types Stats
data_types = get_data_types(api_client)
system_data_types = 0
for dt in data_types:
    if dt['SharedScope'] == 'shared':
        system_data_types +=1

print()
print('### Workflow Designer Statistics ###\n')
print('Total Workflows: {}'.format(len(wf_definitions)))
print('System Workflows: {}'.format(len(wf_definitions) - user_wfs))
print('User Workflows: {}'.format(user_wfs))
print('Valid/Invalid Workflows: {0}/{1}'.format(valid_wfs, len(wf_definitions)-valid_wfs))
print()
print('### Executions Statistics ###\n')
print('Total Executions: {}'.format(len(requests)))
print('Success/Failed Executions: {0}/{1}'.format(success_requests, len(requests)-success_requests))
print('Last Request: \"{0}\", by user {1}, with Moid {2}'. format(requests[0]['Name'], requests[0]['Email'], requests[0]['Moid']))
print()
print('### Task Designer Statistics ###\n')
print('Total Tasks: {}'.format(len(tasks)))
print('System Tasks: {}'.format(system_tasks))
print('Custom Tasks: {}'.format(len(tasks)-system_tasks))
print()
print('### Data Types Statistics ###\n')
print('Total Data Types: {}'.format(len(data_types)))
print('System Data Types: {}'.format(system_data_types))
print('Custom Data Types: {}'.format(len(data_types)-system_data_types))