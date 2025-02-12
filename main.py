import logging
from s3_handler import list_csv_files, read_csv_from_s3
from dynamodb_handler import create_dynamodb_table, sanitize_table_name, insert_data_into_dynamodb
from utlis import DEFAULT_KEYS


BUCKET_NAME = 'raw-target-staging'

def main(event=None, context=None):
    csv_files = list_csv_files(BUCKET_NAME)
    
    for file_key in csv_files:
        attributes,items = read_csv_from_s3(BUCKET_NAME, file_key)
        
        partition_key = DEFAULT_KEYS.get(file_key, list(attributes.keys())[0])
        key_type = attributes.get(partition_key, 'S')
        
        table_name = sanitize_table_name(file_key)
        create_dynamodb_table(table_name, partition_key, key_type)

        insert_data_into_dynamodb(table_name, items)


if __name__ == "__main__":
    main()
