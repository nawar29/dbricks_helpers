# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions (Groups)
# MAGIC %run "./groups_base"

# COMMAND ----------

# DBTITLE 1,Read All Groups or Single Group in Workspace
# if 'group_name' is 'None' then it will process all workspace groups
group_instructions = get_groups_report(databricks_instance, databricks_pat, group_name = None)

# COMMAND ----------

# DBTITLE 1,Write Groups Instructions to DBFS (Local) and Azure Storage Account (External)
def upload_to_dbfs_and_azure_storage(azstorageobj, instructions):
  # write secret scope results to DBFS
  schema = StructType(
    [
      StructField('payload', StringType(), True)
    ]
  )
  df = spark.createDataFrame(data = [[instructions]], schema = schema)


  dbfsfilepath = f'{azstorageobj.config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"]}/{azstorageobj.config["AZURE_STORAGE_ACCOUNT_SUBFOLDER_PATH"]}/{azstorageobj.config["AZURE_STORAGE_ACCOUNT_FILE_NAME"]}'
  # clean up old dbfs secret scope results
  dbutils.fs.rm(dbfsfilepath, True)
  df.coalesce(1).write.mode("overwrite").format('json').save(dbfsfilepath)


  # write secret scopes to azure storage account
  azstorageobj.upload_blob_from_local(
    storageacctname = azstorageobj.config["AZURE_STORAGE_ACCOUNT_NAME"], 
    container = azstorageobj.config["AZURE_STORAGE_ACCOUNT_CONTAINER"],
    localfilepath = f'/dbfs/{dbfsfilepath}/{get_dbfs_file_name(dbfsfilepath, ".json")}', 
    blobfilepath = dbfsfilepath, 
    overwrite = True
  )
  # finally remove new dbfs secret scope results
  dbutils.fs.rm(dbfsfilepath, True)


# set override variables (user defined)
storage_account_obj.set_azure_storage_acct_container_name_override("dbricks-groups")
storage_account_obj.set_azure_storage_acct_subfolder_path_override("groups")
storage_account_obj.set_azure_storage_acct_file_name_override("groups.json")

# write out groups to azure storage account
upload_to_dbfs_and_azure_storage(storage_account_obj, group_instructions)
