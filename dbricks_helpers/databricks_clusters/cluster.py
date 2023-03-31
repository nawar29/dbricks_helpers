# Databricks notebook source
# DBTITLE 1,Get Databricks Rest 2.0 Initial Configuration and Base Functions
# MAGIC %run "../general/base"

# COMMAND ----------

# DBTITLE 1,Get Databricks Rest 2.0 API Action Configurations - Clusters
# clusters - create python 3 cluster
create_cluster_config = get_api_config(databricks_instance, "clusters", "create")
print(f"create_cluster_config: {create_cluster_config}\n")

# clusters - terminate python 3 cluster
terminate_cluster_config = get_api_config(databricks_instance, "clusters", "delete")
print(f"terminate_cluster_config: {terminate_cluster_config}\n")

# clusters - delete python 3 cluster
delete_cluster_config = get_api_config(databricks_instance, "clusters", "permanent-delete")
print(f"delete_cluster_config: {delete_cluster_config}\n")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - Create Cluster
jsondata= {
    "cluster_name": "my-cluster",
    "spark_version": "12.2.x-scala2.12",
    "node_type_id": "Standard_DS4_v2",
    "spark_env_vars": {"PYSPARK_PYTHON": "/databricks/python3/bin/python3"},
    "autoscale": {
        "min_workers": 4,
        "max_workers": 8
    },
    "autotermination_minutes": 120,
    "spark_conf": {
        "spark.databricks.delta.preview.enabled": "true"
    }
}
response = execute_rest_api_call(post_request, create_cluster_config, databricks_pat, jsondata)
clusterid = response.text 
print(f"response: {response}; cluster_id: {clusterid}")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - Terminate Cluster
jsondata = {"cluster_id": "0315-183149-vhl3qthn"}
response = execute_rest_api_call(post_request, terminate_cluster_config, databricks_pat, jsondata)
print(f"response: {response}; response_text: {response.text}")

# COMMAND ----------

# DBTITLE 1,Databricks Rest API 2.0 - Permanently Delete Cluster
jsondata = {"cluster_id": "0315-183149-vhl3qthn"}
response = execute_rest_api_call(post_request, delete_cluster_config, databricks_pat, jsondata)
print(f"response: {response}; response_text: {response.text}")

# COMMAND ----------


