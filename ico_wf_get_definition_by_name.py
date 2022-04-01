import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException

workflow_name = 'Deploy a Virtual Machine'

def get_workflow_definitions(api_client):
    """ Gets the list of workflows """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        query_filter = "Label eq '{0}'".format(workflow_name)
        api_response = api_instance.get_workflow_workflow_definition_list(filter=query_filter,top=0,_check_return_type=False)
        return api_response.results[0]
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get the list of Workflows
pprint(get_workflow_definitions(api_client))