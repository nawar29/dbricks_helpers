# Databricks notebook source
# DBTITLE 1,Environment Variables
import os

# local variables
os.environ["ENVIRONMENT"] = "dev"
os.environ["LOCAL_DATA_FOLDER"] = "data"

# databricks environment variables
os.environ["DATABRICKS_INSTANCE"] = "e2-demo-field-eng.cloud.databricks.com"
os.environ["DATABRICKS_PAT"] = "dapi23d691db7dfa7c2fd59b6ceed1678d57"
os.environ["DATABRICKS_MIGRATION_INSTANCE"] = "adb-7331524806598396.16.azuredatabricks.net"
os.environ["DATABRICKS_MIGRATION_PAT"] = "dapi268b99fffeb917c8e5d6201551f38a4e-3"

# azure environment variables - storage account
os.environ["AZURE_STORAGE_ACCOUNT_NAME"] = f'rastorageaccount{os.environ["ENVIRONMENT"]}'
os.environ["AZURE_STORAGE_ACCOUNT_CONTAINER"] = "bronze"
os.environ["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"] = f'databricks/{os.environ["DATABRICKS_INSTANCE"]}/secret_scopes'
os.environ["AZURE_STORAGE_ACCOUNT_FILE_NAME"] = "secret_scopes.json"
os.environ["AZURE_STORAGE_ACCOUNT_KEY"] = "7xrtGkhGYqwbfDCU+yUypV5pHml04nUVB2GCcXbBiqZa1cnoTeGYVyyVc/91AzvPfO/8A8e5iQ8H+AStW8a/VQ=="
os.environ["AZURE_STORAGE_ACCOUNT_CONN"] = f'DefaultEndpointsProtocol=https;AccountName={os.environ["AZURE_STORAGE_ACCOUNT_NAME"]};AccountKey={os.environ["AZURE_STORAGE_ACCOUNT_KEY"]};EndpointSuffix=core.windows.net'
