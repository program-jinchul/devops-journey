import boto3 # aws 콘솔에서 말고 python 코드로 rds를 제어할 수 있게 해주는 라이브러리

rds = boto3.client('rds', region_name = 'ap-northeast-2') # boto3로 rds 클라이언트 생성

#start = rds.start_db_instance(DBInstanceIdentifier='jinchul-db') DBInstance 시작
stop = rds.stop_db_instance(DBInstanceIdentifier='jinchul-db') # DBInstance 중지

response = rds.describe_db_instances() # rds 인스턴스 정보를 가져오는 API 호출


for database in response['DBInstances']: # rds 인스턴스 정보를 반복문으로 가져옴
    print(f"DB 식별자: {database['DBInstanceIdentifier']}")  # 이건 DB Instance Identifier
    print(f"상태: {database['DBInstanceStatus']}")  # 이건 DB Instance Status
    print("-" * 30)