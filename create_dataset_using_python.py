from google.cloud import bigquery
import os

# 🔹 Replace this with the actual path where your key is saved
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/user/keys/seb-39-bq.json"

# Initialize BigQuery client
client = bigquery.Client()

# Project and dataset details
project_id = "seb-39"
dataset_id = "python_stg_ds"
dataset_ref = f"{project_id}.{dataset_id}"

# Define dataset
dataset = bigquery.Dataset(dataset_ref)
dataset.location = "US"

# Create dataset if not exists
dataset = client.create_dataset(dataset, exists_ok=True)

print(f"✅ Created dataset {client.project}.{dataset.dataset_id} in {dataset.location}")
