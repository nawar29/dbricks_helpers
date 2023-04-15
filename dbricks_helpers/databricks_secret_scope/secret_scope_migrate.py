# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions
# MAGIC %run "./secret_scope_base"

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



# remove local copied secret scope folder and delete container
shutil.rmtree(dbfsfilepath, ignore_errors = True)
storage_account_obj.delete_container(container_name)

# COMMAND ----------

