from itertools import count
import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException
import sys


# The MOID of the request we want details for
moid = '62473732696f6e2d315a0379'
query_filter = "WorkflowInfo.Moid eq '{0}'".format(moid)

def get_workflow_request_details(api_client):
    """ Gets the details of a workflow execution """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_task_info_list(filter=query_filter,_check_return_type=False)
        return api_response.results
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_info_by_moid: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get details on a workflow execution/request
tasks = get_workflow_request_details(api_client)

for task in tasks:
    if task['Internal'] == False:
        print()
        print('### Task {} Output ###\n'.format(task['Label']))
        print(task['Output'])