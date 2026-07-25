import boto3

s3 = boto3.client('s3', region_name='ap-northeast-2') # boto3로 S3 클라이언트 생성

s3.upload_file('python/test.txt', 'jinchul-devops-bucket', 'test.txt') # S3에 파일 업로드

response = s3.list_objects_v2(Bucket='jinchul-devops-bucket') # bucket list 가져오기
# response = s3.delete_object(
#     Bucket = 'jinchul-devops-bucket',
#     Key = 'test.txt'
# ) 요기 주석은 S3에 있는 test.txt 파일을 삭제하는 코드

if 'Contents' in response: # Contents는 S3 파일 리스트 보면 if 조건문 사용 있을 때만 작동
    for obj in response['Contents']: # Contents 안에 있는 파일들을 반복문으로 가져옴
        print(f"파일명: {obj['Key']}, 크기: {obj['Size']} bytes") # 파일명이랑 크기 가져오기
#print("삭제 완료", response)
print("업로드 완료!")