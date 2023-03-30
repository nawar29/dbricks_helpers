# library and file imports
import os
from dotenv import load_dotenv


# load .env environment file
load_dotenv()


class Config:
# configuration class definition

    # class constructor    
    def __init__(self):

        # local variables
        self.DATABRICKS_INSTANCE = str(os.getenv('DATABRICKS_INSTANCE'))
        self.DATABRICKS_PAT = str(os.getenv('DATABRICKS_PAT'))
        self.DATABRICKS_MIGRATION_INSTANCE = str(os.getenv('DATABRICKS_MIGRATION_INSTANCE'))
        self.DATABRICKS_MIGRATION_PAT = str(os.getenv('DATABRICKS_MIGRATION_PAT'))
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