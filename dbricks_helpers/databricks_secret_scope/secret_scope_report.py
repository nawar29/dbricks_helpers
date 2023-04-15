# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions
# MAGIC %run "./secret_scope_base"

# COMMAND ----------

# DBTITLE 1,Read All Secret Scopes in Workspace
# if 'secret_scope_name' is 'None' then it will process all workspace secret scopes
instructions = get_secret_scope_report(databricks_instance, databricks_pat, read_scope_user = "robert.altmiller@databricks.com", read_scope_user_perms = "READ", secret_scope_name = None)
print(instructions)

# COMMAND ----------

# DBTITLE 1,Write Secret Scope Instructions to DBFS (Local) and Azure Storage Account (External)
# write secret scope results to DBFS
schema_secretscope = StructType(
  [
    StructField('payload', StringType(), True)
  ]
)
df_secret_scope = spark.createDataFrame(data = [[instructions]], schema = schema_secretscope)
dbfsfilepath = f'{storage_account_obj.config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"]}/{storage_account_obj.config["AZURE_STORAGE_ACCOUNT_FILE_NAME"]}'
# clean up old dbfs secret scope results
dbutils.fs.rm(dbfsfilepath, True)
df_secret_scope.coalesce(1).write.mode("overwrite").format('json').save(dbfsfilepath)


# write secret scopes to azure storage account
storage_account_obj.upload_blob_from_local(
  storageacctname = storage_account_obj.config["AZURE_STORAGE_ACCOUNT_NAME"], 
  container = "secret-scopes",
  localfilepath = f'/dbfs/{dbfsfilepath}/{get_dbfs_file_name(dbfsfilepath, ".json")}', 
  blobfilepath = dbfsfilepath, 
  overwrite = True
)

# finally remove new dbfs secret scope results
dbutils.fs.rm(dbfsfilepath, True)
