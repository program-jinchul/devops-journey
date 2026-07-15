import boto3

s3 = boto3.client('s3', region_name='ap-northeast-2')

s3.upload_file('python/test.txt', 'jinchul-devops-bucket', 'test.txt')

response = s3.list_objects_v2(Bucket='jinchul-devops-bucket')

if 'Contents' in response:
    for obj in response['Contents']:
        print(f"파일명: {obj['Key']}, 크기: {obj['Size']} bytes")

print("업로드 완료!")