# Databricks notebook source
# DBTITLE 1,Library Imports
import requests, os

# COMMAND ----------

# DBTITLE 1,Environment Variables
# databricks instance address
databricks_instance = "adb-7331524806598396.16.azuredatabricks.net"
# databricks personal access token
databricks_pat = "dapi*******"

# COMMAND ----------

# DBTITLE 1,SCIM API Post Requests Functions
# get requests parameters
def get_params():
    params = {}
    return params


# get requests headers
def get_headers(token = None):
    headers = {'Authorization': 'Bearer %s' % token}
    return headers


# post request
def post_request(url = None, headers = None, params = None, data = None):
    if params != None:
        return requests.post(url, params = params, headers = headers, json = data)
    else: return requests.post(url, headers = headers, json = data)


# get request
def get_request(url = None, headers = None, params = None, data = None):
    if params != None:
        return requests.get(url, params = params, headers = headers, json = data)
    else: return requests.get(url, headers = headers, json = data)

# COMMAND ----------

# DBTITLE 1,Databricks SCIM Groups Configuration
/accounts/{account_id}/workspaces/{workspace_id}/	
/api/2.0/previewpermissionassignments/principals/{principal_id}
def get_api_config(dbricks_id = None, dbricks_ws_id = None, dbricks_instance = None, api_topic = None, api_call_type = None):
    config = {
        # databricks account id
        "databricks_account_id": dbricks_id,
        "databricks_workspace_id": dbricks_ws_id,
        # databricks workspace instance
        "databricks_ws_instance": dbricks_instance,
        # databricks rest api version
        "api_version": "api/2.0/preview",
        # databricks rest api service call
        "api_topic": api_topic,
        # databricks api call type
        "api_call_type": api_call_type
    }
    config["databricks_host"] = "https://" + config["databricks_ws_instance"]
    config["api_full_url"] = config["databricks_host"] + "/" + config["api_version"] + "/" + config["api_topic"] + "/" + config["api_call_type"]
    return config

# COMMAND ----------

# DBTITLE 1,Get Databricks SCIM API Action Configurations - Groups
# scim groups configuration - create or update workspace permissions for a princple

#/api/2.0/preview/accounts/{account_id}/workspaces/{workspace_id}/permissionassignments/principals/{principal_id}
add_group_member_config = get_api_config(databricks_instance, "previewpermissionassignments/principals", "add-member")
print(f"add_group_member_config: {add_group_member_config}\n")

# COMMAND ----------

# DBTITLE 1,Execute Databricks Rest API 2.0 Call (Generic)
# execute rest api call
# call_type variable is 'get' or 'post'
def execute_rest_api_call(function_call_type, config = None, token = None, jsondata = None):
    headers = get_headers(token)
    response = function_call_type(url = config["api_full_url"], headers = headers, data = jsondata)
    return response

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - List All Groups in Entire Organization
jsondata = {}
response = execute_rest_api_call(get_request, list_all_groups_config, databricks_pat, jsondata)
print(response.text)

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - List Group Members
jsondata = {'group_name': 'dbricks-contributors'}
response = execute_rest_api_call(get_request, list_group_member_config, databricks_pat, jsondata)
print(response.text)

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - Add User to a Group
# this jsondata below adds a user to a group
jsondatalist = [
    {'user_name': 'robert.altmiller@databricks.com', 'parent_name': 'dbricks-readers'},
    {'user_name': 'robert.altmiller@databricks.com', 'parent_name': 'dbricks-contributors'},
    {'user_name': 'robert.altmiller@databricks.com', 'parent_name': 'users'},
    {'user_name': 'robert.altmiller@databricks.com', 'parent_name': 'admin'}
]

# add all the members to groups
for jsondata in jsondatalist:
    response = execute_rest_api_call(post_request, add_group_member_config, databricks_pat, jsondata)
    print(f"{jsondata}: {response}")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - Add Group to a Group
# this jsondata below adds a group to a group
# in this case 'dbricks_contributors' gets added to 'dbricks-readers'
jsonlist = [
    {'group_name': 'dbricks_contributors', 'parent_name': 'dbricks-readers'},
    {'group_name': 'admin', 'parent_name': 'dbricks-readers'},
    {'group_name': 'users', 'parent_name': 'dbricks-readers'}
]

# add the groups to groups
for jsondata in jsondatalist:
    response = execute_rest_api_call(post_request, add_group_member_config, databricks_pat, jsondata)
    print(f"{jsondata}: {response}")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - List All the Groups a User is in
jsondata = {'user_name': 'robert.altmiller@databricks.com'}
response = execute_rest_api_call(get_request, list_user_groups_config, databricks_pat, jsondata)
print(response.text)

# COMMAND ----------


