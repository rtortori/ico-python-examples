import credentials
from intersight.api import workflow_api
from intersight.rest import ApiException

# Moid of the Data Type
moid="60cbf3d7696f6e2d30957aa2"

# Get Data Types
def get_data_types(api_client):
    """ Gets the list of data types """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_custom_data_type_definition_by_moid(moid=moid,_check_return_type=False)
        print(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_custom_data_type_definition_by_moid: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()

# Get Data Type
get_data_types(api_client)