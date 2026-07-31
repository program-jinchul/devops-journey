# IAM (Identity and Access Management)

## 개념
AWS 리소스에 대한 접근을 안전하게 제어하는 서비스. 누가 무엇을 할 수 있는지 권한을 관리한다.

## 구성 요소

### User
- AWS 콘솔에 로그인하는 사람
- 실습에서 사용: `jinchul-dev`

### Role
- AWS 서비스가 다른 서비스에 접근할 때 사용하는 권한
- 실습: EC2에 `jinchul-ec2-s3-role` 붙여서 S3, CloudWatch 접근 권한 부여

### Policy
- 실제 권한 내용을 JSON 형식으로 정의
- 실습에서 사용: `AmazonS3FullAccess`, `CloudWatchAgentServerPolicy`

## 실습 구성
- EC2용 IAM Role 생성
- S3FullAccess + CloudWatchAgentServerPolicy 연결
- EC2에 Role 붙이기