# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %run "./libraries"

# COMMAND ----------

# DBTITLE 1,Import Environment Variables
# MAGIC %run "./.env"

# COMMAND ----------

# DBTITLE 1,Import Generic Functions
# MAGIC %run "./general_functions"

# COMMAND ----------

# DBTITLE 1,Import Azure Functions
# MAGIC %run "../azure/main"

# COMMAND ----------

class Config:
# configuration class definition

    # class constructor    
    def __init__(self):

        # local variables
        self.DATABRICKS_INSTANCE = str(os.getenv('DATABRICKS_INSTANCE'))
        self.DATABRICKS_PAT = str(os.getenv('DATABRICKS_PAT'))
        self.DATABRICKS_MIGRATION_INSTANCE = str(os.getenv('DATABRICKS_MIGRATION_INSTANCE'))
        self.DATABRICKS_MIGRATION_PAT = str(os.getenv('DATABRICKS_MIGRATION_PAT'))
        self.AZURE_STORAGE_ACCOUNT_NAME = str(os.getenv('AZURE_STORAGE_ACCOUNT_NAME'))
        self.AZURE_STORAGE_ACCOUNT_CONTAINER = str(os.getenv('AZURE_STORAGE_ACCOUNT_CONTAINER'))
        self.AZURE_STORAGE_ACCOUNT_FOLDER_PATH = str(os.getenv('AZURE_STORAGE_ACCOUNT_FOLDER_PATH'))
        self.AZURE_STORAGE_ACCOUNT_FILE_NAME = str(os.getenv('AZURE_STORAGE_ACCOUNT_FILE_NAME'))
        self.AZURE_STORAGE_ACCOUNT_KEY = str(os.getenv('AZURE_STORAGE_ACCOUNT_KEY'))
        self.AZURE_STORAGE_ACCOUNT_CONN = str(os.getenv('AZURE_STORAGE_ACCOUNT_CONN'))
        self.format_config_vars()
        

    def format_config_vars(self):
        """
        additional formatting for configuration variables
        this function is optional if you need it
        """
        return None


    def get_config_vars(self):
        # get class configuration variables
        config = Config()
        return vars(config)


    def print_config_vars(self):
        # get configuration variables in a python dictionary
        variables = self.get_config_vars()
        print("configuration variables:")
        vars_list = []
        for key, val in variables.items():
            print(f"{key}: {val}")
        print("\n")

# COMMAND ----------

# DBTITLE 1,Variables Initialization

# configuration class object
config = Config()
# print configuration variables
config.print_config_vars()


# get configuration variables
config = config.get_config_vars()


# databricks instance address
databricks_instance = config["DATABRICKS_INSTANCE"]
# databricks personal access token
databricks_pat = config["DATABRICKS_PAT"]
# databricks migration instance address
databricks_migration_instance = config["DATABRICKS_MIGRATION_INSTANCE"]
# databricks migration personal access token
databricks_migration_pat = config["DATABRICKS_MIGRATION_PAT"]


# az storage account name
azsa_name = config["AZURE_STORAGE_ACCOUNT_NAME"]
# az storage account container
azsa_container = config["AZURE_STORAGE_ACCOUNT_CONTAINER"]
# az storage account folder path
azsa_folderpath = config["AZURE_STORAGE_ACCOUNT_FOLDER_PATH"]
# az storage account file name
azsa_filename = config["AZURE_STORAGE_ACCOUNT_FILE_NAME"]
# az storage account key
azsa_key = config["AZURE_STORAGE_ACCOUNT_KEY"]
# az storage account connection string
azsa_conn = config["AZURE_STORAGE_ACCOUNT_CONN"]

# COMMAND ----------

# DBTITLE 1,Class Objects Initialization
# az storage account class object
storage_account_obj = azurestorageaccount(config)
