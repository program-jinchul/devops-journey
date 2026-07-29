# EC2 (Elastic Compute Cloud)

## 개념
AWS에서 제공하는 가상 서버. 온디맨드로 서버를 생성하고 삭제할 수 있어 유연한 인프라 구성이 가능하다.

## 구성 요소

### AMI (Amazon Machine Image)
- EC2 인스턴스의 운영체제 이미지
- Amazon Linux, Ubuntu 등 선택 가능
- 실습에서 사용한 AMI: `ami-062cf18d655c0b1e8` (Amazon Linux 2023)

### Instance Type
- CPU, 메모리 사양을 정의하는 타입
- `t3.micro`: 2vCPU, 1GB RAM (프리티어 적용)

### Key Pair
- SSH 접속 시 사용하는 인증 키
- `.pem` 파일로 발급되며 분실 시 재발급 불가
- 접속 명령어:# EC2 (Elastic Compute Cloud)

## 개념
AWS에서 제공하는 가상 서버. 온디맨드로 서버를 생성하고 삭제할 수 있어 유연한 인프라 구성이 가능하다.

## 구성 요소

### AMI (Amazon Machine Image)
- EC2 인스턴스의 운영체제 이미지
- Amazon Linux, Ubuntu 등 선택 가능
- 실습에서 사용한 AMI: `ami-062cf18d655c0b1e8` (Amazon Linux 2023)

### Instance Type
- CPU, 메모리 사양을 정의하는 타입
- `t3.micro`: 2vCPU, 1GB RAM (프리티어 적용)

### Key Pair
- SSH 접속 시 사용하는 인증 키
- `.pem` 파일로 발급되며 분실 시 재발급 불가
- 접속 명령어: `ssh -i "키파일.pem" ec2-user@퍼블릭IP`

### Security Group
- EC2 인스턴스 단위의 방화벽
- SSH(22), HTTP(80) 포트 인바운드 허용

## 실습 구성
- VPC의 Public Subnet에 EC2 배치
- Nginx 웹서버 설치 및 커스텀 HTML 페이지 배포
- CloudWatch Agent 설치로 로그 수집

## Terraform 코드
```hcl
resource "aws_instance" "main" {
  ami                    = "ami-062cf18d655c0b1e8"
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.main_subnet.id
  vpc_security_group_ids = [aws_security_group.main_security_group.id]

  tags = {
    Name = "jinchul-ec2-tf"
  }
}
```