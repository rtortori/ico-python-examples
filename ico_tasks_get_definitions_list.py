import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException

def get_tasks_definitions(api_client):
    """ Gets the list of tasks """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_task_definition_list(top=0,_check_return_type=False)
        pprint(api_response.results)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get the list of Tasks
get_tasks_definitions(api_client)