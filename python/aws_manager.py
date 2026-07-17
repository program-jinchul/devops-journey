import boto3



class AwsManager:
    def __init__(self, region='ap-northeast-2'):
        self.ec2 = boto3.client('ec2', region_name='ap-northeast-2')
        self.rds = boto3.client('rds', region_name='ap-northeast-2')
        self.s3 = boto3.client('s3', region_name='ap-northeast-2')

    def ec2_monitor(self, action):
        # EC2 monitor
        if action == 'start':
            print('EC2를 실행합니다.')
            self.ec2.start_instances(InstanceIds=['i-0e36eada750cf6cab'])
        else:
            print('EC2를 중지합니다.')
            self.ec2.stop_instances(InstanceIds=['i-0e36eada750cf6cab'])
            
    def rds_monitor(self, action):
        # RDS monitor
        if action == 'start':
            print('RDS를 시작합니다.')
            self.rds.start_db_instance(DBInstanceIdentifier='jinchul-db')
        else:
            print('RDS를 중지합니다.')
            self.rds.stop_db_instance(DBInstanceIdentifier='jinchul-db')

    def s3_monitor(self, action):
        # S3 monitor
        print('bucket를 만드세요!')


manager = AwsManager()

service = input("ec2 / rds / s3: ")
action = input("start / stop: ")

if service == "ec2":
    manager.ec2_monitor(action)
elif service == "rds":
    manager.rds_monitor(action)
elif service == "s3":
    manager.s3_monitor(action)