import credentials
from intersight.api import workflow_api
from intersight.rest import ApiException

# Query Options
filter_query="(Properties.ExternalMeta eq true) and (Name ne 'DeployHyperFlexSDWAN') and (DefaultVersion eq true)"

# Get Data Types
def get_data_types(api_client):
    """ Gets the list of data types """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_response = api_instance.get_workflow_custom_data_type_definition_list(top=0,_check_return_type=False)
        print(api_response.results)
    except ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_custom_data_type_definition_list: %s\n" % e)

# Authenticate
api_client = credentials.config_credentials()


# Get Data Types Stats
data_types = get_data_types(api_client)