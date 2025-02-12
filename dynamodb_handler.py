import boto3
import logging

dynamodb = boto3.resource('dynamodb')

def table_exists(table_name):
    try:
        table = dynamodb.Table(table_name)
        table.load()
        logging.info(f"Table '{table_name}' already exists.")
        return True
    except Exception:
        return False

def create_dynamodb_table(table_name, key_name, key_type='S'):
    if table_exists(table_name):
        return

    try:
        table = dynamodb.create_table(
            TableName=table_name,
            AttributeDefinitions=[
                {'AttributeName': key_name, 'AttributeType': key_type}
            ],
            KeySchema=[
                {'AttributeName': key_name, 'KeyType': 'HASH'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logging.info(f"Table '{table_name}' created successfully. Waiting for activation...")
        table.wait_until_exists()
        logging.info(f"Table '{table_name}' is now active.")
    except Exception as e:
        logging.error(f"Error creating table '{table_name}': {e}")

def insert_data_into_dynamodb(table_name, items):
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
    logging.info(f"Inserted {len(items)} records into '{table_name}'.")


def sanitize_table_name(file_key):
    return file_key.replace('/', '_').replace('.csv', 'Table')

