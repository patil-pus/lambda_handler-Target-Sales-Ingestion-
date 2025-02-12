import boto3
import io
import logging
from utlis import infer_data_type
import csv


s3_client=boto3.client('s3')

def list_csv_files(bucket_name):
    response=s3_client.list_objects_v2(Bucket=bucket_name)
    return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.csv')]

def read_csv_from_s3(bucket_name, file_key):
    logging.info(f"Reading file: {file_key}")
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    body = response['Body'].read().decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(body))
    first_row = next(csv_reader)
    attributes = {col: infer_data_type(value) for col, value in first_row.items()}
    items=[rows for rows in csv_reader]
    return attributes, items



