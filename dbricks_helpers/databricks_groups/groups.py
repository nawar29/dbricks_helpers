# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions
# MAGIC %run "../general/base"

from general.base import *

# COMMAND ----------

# DBTITLE 1,Get Databricks Rest 2.0 API Action Configurations - Groups
# groups - add member configuration
add_group_member_config = get_api_config(databricks_instance, "groups", "add-member")
print(f"add_group_member_config: {add_group_member_config}\n")

# groups - list member configuration
list_group_member_config = get_api_config(databricks_instance, "groups", "list-members")
print(f"list_group_member_config: {list_group_member_config}\n")

# groups - list all groups configuration
list_all_groups_config = get_api_config(databricks_instance, "groups", "list")
print(f"list_all_groups_config: {list_all_groups_config}\n")

# groups - list all groups a user is in configuration
list_user_groups_config = get_api_config(databricks_instance, "groups", "list-parents")
print(f"list_user_groups_config: {list_user_groups_config}\n")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - List All Groups in Entire Organization
jsondata = {}
response = execute_rest_api_call(get_request, list_all_groups_config, databricks_pat, jsondata)
print(response.text)

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - List Group Members
jsondata = {'group_name': 'dbricks-contributors'}
response = execute_rest_api_call(get_request, list_group_member_config, databricks_pat, jsondata)
print(f"response: {response}; response_text: {response.text}")

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
print(f"response: {response}; response_text: {response.text}")
