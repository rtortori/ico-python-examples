import credentials
from intersight.api import workflow_api
from intersight.rest import ApiException

# Variables. Change accordingly
workflow_moid = '62473732696f6e2d315a0379'

# Authenticate
api_client = credentials.config_credentials()

#### Sample JSON Payload for Reference ####
"""

Create the rollback workflow

{
    "PrimaryWorkflow":
    {
        "ObjectType":"workflow.WorkflowInfo",
        "Moid":"{{execution-moid}}"
    },
    "Action":"Create"
}

Start the rollback workflow

{
    "PrimaryWorkflow":
    {
        "ObjectType": "workflow.WorkflowInfo",
        "Moid": "{{execution-moid}}"
    },
    "Action": "Start",
    "ContinueOnTaskFailure": true,
    "SelectedTasks":
    []
}

"""

create_rb_action = {
    "PrimaryWorkflow":
    {
        "ObjectType":"workflow.WorkflowInfo",
        "Moid":workflow_moid
    },
    "Action":"Create"
}

start_rb_action = {
    "PrimaryWorkflow":
    {
        "ObjectType": "workflow.WorkflowInfo",
        "Moid": workflow_moid
    },
    "Action": "Start",
    "ContinueOnTaskFailure": True,
    "SelectedTasks":
    []
}

def execute_rollback(api_client):
    """ Execute a Workflow """
    api_instance = workflow_api.WorkflowApi(api_client)

    try:
        api_instance.create_workflow_rollback_workflow(workflow_rollback_workflow=create_rb_action,_check_return_type=False)
        start_rb = api_instance.create_workflow_rollback_workflow(workflow_rollback_workflow=start_rb_action,_check_return_type=False)
        print('Rolling back Workflow with Moid {0}'.format(workflow_moid))
        print('Rollback execution Moid: is {0}'.format(start_rb.rollback_workflows[0]['Moid']))
        print('Status: {0}'.format(start_rb.status))
        # Uncomment the following to show the full response
        #print(start_rb) 
    
    except ApiException as e:
        print("Exception when Rolling Back Workflow: %s\n" % e)

# Rollback the Workflow
execute_rollback(api_client)
