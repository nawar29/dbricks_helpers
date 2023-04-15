# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions
# MAGIC %run "./secret_scope_base"

# COMMAND ----------

# DBTITLE 1,Notebook Parameters Initialization
# delete secret scope report from azure storage account (False or True)
delete_ss_report_from_azsa = False

# recreate all secret scopes (False or True)
recreate_all_secret_scopes = True

# secret scopes to re-create
recreate_secret_scopes_list = ["adnan"]
if len(recreate_secret_scopes_list) > 0: recreate_all_secret_scopes = False

# COMMAND ----------

# DBTITLE 1,Deploy Secret Scopes From Old Workspace to New Workspace
container_name = "secret-scopes"
dbfsfilepath = storage_account_obj.download_blob_write_locally(
    storageacctname = storage_account_obj.config["AZURE_STORAGE_ACCOUNT_NAME"],
    container = container_name, 
    folderpath = storage_account_obj.config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"],
    filename = storage_account_obj.config["AZURE_STORAGE_ACCOUNT_FILE_NAME"]
)

# get secret scope deploy instructions for new workspace
with open(dbfsfilepath) as fp:
    data = json.load(fp)
deploy_instructions = data["payload"]
if deploy_instructions != None:
  deploy_instructions_json = json.loads(deploy_instructions)


if delete_ss_report_from_azsa == True:
  # remove local copied secret scope folder and delete container
  shutil.rmtree(f'./{storage_account_obj.config["LOCAL_DATA_FOLDER"]}', ignore_errors = True)
  storage_account_obj.delete_container(container_name)

# COMMAND ----------

# DBTITLE 1,Print All Secret Scopes for Migration to New Workspace
allscopes = []
for jsonrecord in deploy_instructions_json:
    allscopes.append(jsonrecord["secret_scope_name"])
print(allscopes)

# COMMAND ----------

# DBTITLE 1,Recreate Single Secret Scope or All Secret Scopes
if recreate_all_secret_scopes == True:
  deploy_instructions_final = deploy_instructions
else: # get subset of secret scopes based on deploy_instructions
  scopes_subset = []
  for scope in recreate_secret_scopes_list:
    for jsonrecord in deploy_instructions_json:
      if jsonrecord["secret_scope_name"] == scope:
        scopes_subset.append(jsonrecord)
  deploy_instructions_final = json.dumps(scopes_subset)
print(deploy_instructions_final)

# COMMAND ----------

# recreate secret scopes in new workspace (works across cloud environments too)cccccbeutijibvgtgficignibvknlctnelkdjgnvltbe
recreate_all_secret_scopes(databricks_migration_instance, databricks_migration_pat, deploy_instructions_final, write_scope_user = "robert.altmiller@databricks.com", write_scope_user_perms = "Write", new_secret_scope_name = None)

# COMMAND ----------

# DBTITLE 1,Validate Secrets Scopes Migrated to New Workspace Successfully
# if 'secret_scope_name' is 'None' then it will process all workspace secret scopes
instructions = get_secret_scope_report(databricks_migration_instance, databricks_migration_pat, read_scope_user = "robert.altmiller@databricks.com", read_scope_user_perms = "READ", secret_scope_name = None)
print(instructions)

