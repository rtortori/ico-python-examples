from itertools import count
import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException
import sys

# Specify the MOID here 
moid='6239aab7696f6e2d3118775d'

def get_tasks_definitions(api_client):
    """ Gets the list of tasks """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_task_definition_by_moid(moid=moid,_check_return_type=False)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get the list of Tasks
get_tasks_definitions(api_client)