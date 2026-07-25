import subprocess
import boto3

command = ["terraform", "output", "instance_id"]

result = subprocess.run(
    command,
    capture_output = True,
    text = True,
    check = True,
    cwd = "terraform"
)

instance_id = result.stdout.strip().replace('"', '')

print(instance_id)

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

response = ec2.describe_instances(InstanceIds=[instance_id])

instance = response["Reservations"][0]["Instances"][0]
print(f" Instance ID: {instance['InstanceId']} ")
print(f" Instance Type: {instance['InstanceType']}")
print(f" Instance State: {instance['State']['Name']}")

tags = instance["Tags"]
for tag in tags:
    if tag['Key'] == 'Name':
        print(f"Name: {tag['Value']}")