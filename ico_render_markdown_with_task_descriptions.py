import credentials
from intersight.api import workflow_api
from intersight.rest import ApiException
import re

markdown_header = '''| Task Name | Category | Description | Targets |
|---|---|---|---|'''

def get_tasks_definitions(api_client):
    """ Gets the list of tasks """
    api_instance = workflow_api.WorkflowApi(api_client)
    filter_query='(Properties.ExternalMeta eq true) and (DefaultVersion eq true) and (SharedScope eq shared)'
    select_query = 'Label,Description,Tags'
    orderby_query = 'Label'
    try:
        api_response = api_instance.get_workflow_task_definition_list(filter=filter_query, select=select_query, orderby=orderby_query, top=0,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get the list of Tasks
tasks = get_tasks_definitions(api_client)


# Render Markdown
print(markdown_header)
for task in tasks:
    target_list = []
    desc = task['Description']
    label = task['Label']
    for tag in task['Tags']:
        if re.search(r'platformType', tag['Key']):
            target_list.append(tag['Key'].split('.')[1])
        if tag['Key'] == 'category':
            category = tag['Value'] 
    target_list_str = ""
    for i in target_list:
        target_list_str += i+" "
    print('| {} | {} | {} | {} |'.format(label, category, " ".join(desc.splitlines()), target_list_str))