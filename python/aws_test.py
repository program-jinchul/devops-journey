import boto3

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

response = ec2.describe_instances()



action = input('start or stop:')
if action == 'start':
    print('EC2를 실행합니다.')
    start = ec2.start_instances(InstanceIds=['i-0e36eada750cf6cab'])
else:
    print('EC2를 중지합니다.')
    stop = ec2.stop_instances(InstanceIds=['i-0e36eada750cf6cab'])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"인스턴스 ID: {instance['InstanceId']}")
        print(f"상태: {instance['State']['Name']}")
        print(f"타입: {instance['InstanceType']}")
        print("-" * 30)