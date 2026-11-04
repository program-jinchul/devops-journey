import boto3 # aws를 코드로 제어할 수 있게 해주는 라이브러리

ec2 = boto3.client('ec2', region_name='ap-northeast-2') # boto3로 EC2 클라이언트 생성

action = input('start or stop:') # start / stop 제어

if action == 'start':
    print('EC2를 실행합니다.')
    start = ec2.start_instances(InstanceIds=['i-0e36eada750cf6cab']) # InstanceIds를 받아서 시작
else:
    print('EC2를 중지합니다.')
    stop = ec2.stop_instances(InstanceIds=['i-0e36eada750cf6cab']) # InstanceIds를 받아서 중지

response = ec2.describe_instances() # EC2 인스턴스 정보를 가져오는 API 호출

for reservation in response['Reservations']: # 예약된 인스턴스를 반복문으로 가져옴
    for instance in reservation['Instances']: # 인스턴스 정보를 반복문으로 가져옴
        print(f"인스턴스 ID: {instance['InstanceId']}") # 이건 Instance Id
        print(f"상태: {instance['State']['Name']}") # 이건 Instance State
        print(f"타입: {instance['InstanceType']}") # 이건 Instance Type
        print("-" * 30)