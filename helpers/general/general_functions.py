# Databricks notebook source
# DBTITLE 1,Library Imports
# MAGIC %run "./libraries"

# COMMAND ----------

# DBTITLE 1,Create an MD5 Hash out of a Python String
def str_to_md5_hash(inputstr = None):
  """encoding GeeksforGeeks using md5 hash"""
  return hashlib.md5(inputstr.encode())
