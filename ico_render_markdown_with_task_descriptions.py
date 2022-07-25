import credentials
from intersight.api import workflow_api
from intersight.rest import ApiException

markdown_header = '''| Task Name | Description  |
|---|---|'''

def get_tasks_definitions(api_client):
    """ Gets the list of tasks """
    api_instance = workflow_api.WorkflowApi(api_client)
    filter_query='(Properties.ExternalMeta eq true) and (DefaultVersion eq true) and (SharedScope eq shared)'
    select_query = 'Label,Description'
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
    desc = task['Description']
    label = task['Label']
    print('| {} | {} |'.format(label, " ".join(desc.splitlines())))