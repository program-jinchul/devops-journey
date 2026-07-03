import boto3

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"인스턴스 ID: {instance['InstanceId']}")
        print(f"상태: {instance['State']['Name']}")
        print(f"타입: {instance['InstanceType']}")
        print("-" * 30)