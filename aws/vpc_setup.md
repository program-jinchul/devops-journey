# VPC (Virtual Private Cloud)

## 개념
AWS 안에 만드는 나만의 가상 네트워크 공간. EC2, RDS 같은 서버들을 올려두는 독립된 네트워크 환경이다.

## Public vs Private Subnet
| 구분 | Public Subnet | Private Subnet |
|------|--------------|----------------|
| 인터넷 접근 | 가능 | 불가능 |
| 용도 | EC2 웹서버 | RDS 데이터베이스 |
| 외부 접근 | 직접 가능 | EC2 통해서만 가능 |

## 구성 요소

### CIDR (Classless Inter-Domain Routing)
- IP 주소 범위를 표현하는 방식
- `10.0.0.0/16` → 65,536개 IP 사용 가능
- `/16` 클수록 범위 큼, `/24` 작을수록 범위 좁음

### Subnet
- VPC를 용도별로 나눈 네트워크 구역
- Public Subnet: 인터넷 직접 통신 가능
- Private Subnet: 외부 접근 차단, 내부에서만 접근 가능

### Internet Gateway (IGW)
- VPC와 인터넷을 연결하는 통로
- VPC에 Attach 해야 인터넷 통신 가능

### Route Table
- 네트워크 트래픽 경로를 정의하는 이정표
- `10.0.0.0/16 → local` : VPC 내부 통신
- `0.0.0.0/0 → IGW` : 인터넷 통신

### Security Group
- 인스턴스 단위의 가상 방화벽
- 인바운드: 들어오는 트래픽 제어 (SSH 22, HTTP 80)
- 아웃바운드: 나가는 트래픽 제어


## 실습 구성
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24) → EC2
└── Private Subnet (10.0.2.0/24) → RDS

## Terraform 코드
## Terraform 코드
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "jinchul-vpc-tf"
  }
}
```