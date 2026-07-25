import subprocess # 터미널 명령어 python에서 실행 가능하게 해주는 라이브러리
import boto3 # aws 연동해서 콘솔에서 말고 코드로 제어 가능하게 해주는 라이브러리

command = ["terraform", "output", "instance_id"] # 말 그대로 터미널 command

result = subprocess.run( # subprocess.run은 실헹
    command, # 위에 썼던 command
    capture_output = True, # 터미널 출력값을 캡쳐해서 python으로 가져오기
    text = True, # 출력값을 문자열로 받기 안하면 byte로 나옴
    check = True,
    cwd = "terraform" # 폴더 지정
)

instance_id = result.stdout.strip().replace('"', '') # 따옴표 제거

print(instance_id)

ec2 = boto3.client('ec2', region_name='ap-northeast-2') # ec2 가져오기

response = ec2.describe_instances(InstanceIds=[instance_id]) # 앞선 instance_id 써서 반복문 없이 딕셔너리 구조 가져오기

instance = response["Reservations"][0]["Instances"][0] # 딕셔너리 구조 변수에 가져오기 [0]은 EC2 서버가 1개만 있는게 아니라서 순서 지정
print(f" Instance ID: {instance['InstanceId']} ") # Id 출력
print(f" Instance Type: {instance['InstanceType']}") # Type 출력
print(f" Instance State: {instance['State']['Name']}") # State 출력

tags = instance["Tags"] # Tags 가져오기
for tag in tags:
    if tag['Key'] == 'Name': # Key 가져와서 
        print(f"Name: {tag['Value']}") # Value 출력