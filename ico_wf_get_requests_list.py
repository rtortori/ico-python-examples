import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException

def get_workflow_requests(api_client):
    """ Gets the list of workflows executions/requests """
    order_by=''
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_workflow_info_list(order_by=order_by,top=0,_check_return_type=False)
        pprint(api_response.results)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_info_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get the list of workflows executions
get_workflow_requests(api_client)