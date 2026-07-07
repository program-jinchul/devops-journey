import boto3

rds = boto3.client('rds', region_name = 'ap-northeast-2')

#start = rds.start_db_instance(DBInstanceIdentifier='jinchul-db')
stop = rds.stop_db_instance(DBInstanceIdentifier='jinchul-db')

response = rds.describe_db_instances()


for database in response['DBInstances']:
    print(f"DB 식별자: {database['DBInstanceIdentifier']}")
    print(f"상태: {database['DBInstanceStatus']}")
    print("-" * 30)