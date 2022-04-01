from itertools import count
import credentials
from pprint import pprint
from intersight.api import workflow_api
from intersight.rest import ApiException
import sys

# The MOID of the request we want details for
moid = '62473732696f6e2d315a0379'

def get_workflow_request_details(api_client):
    """ Gets the details of a workflow execution """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_workflow_info_by_moid(moid=moid,_check_return_type=False)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_workflow_info_by_moid: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get details on a workflow execution/request
get_workflow_request_details(api_client)