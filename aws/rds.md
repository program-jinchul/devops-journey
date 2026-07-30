# RDS (Relational Database Service)

## 개념
AWS에서 제공하는 관리형 관계형 데이터베이스 서비스. 백업, 패치, 모니터링을 AWS가 자동으로 처리해준다.

## 구성 요소

### DB Engine
- MySQL, PostgreSQL, MariaDB 등 선택 가능
- 실습에서 사용: MySQL 8.4

### Instance Type
- `db.t4g.micro`: 프리티어 적용 (2vCPU, 1GB RAM)

### DB Subnet Group
- RDS가 사용할 서브넷을 정의하는 그룹
- 최소 2개의 가용영역(AZ) 필요

### Public Access
- `No` 설정 시 인터넷에서 직접 접근 불가
- EC2를 통해서만 접근 가능

## 실습 구성
- Private Subnet에 RDS 배치
- EC2에서 MySQL 클라이언트로 RDS 접속
- `jinchuldb` 데이터베이스 생성 및 SQL 실습

## Security Group
- `jinchul-db-sg` 에 3306 포트 인바운드 규칙 추가
- Source: EC2 Security Group (`jinchul-sg`)
- EC2에서만 RDS 접근 가능하도록 제한

## 트러블슈팅
- 문제: EC2에서 RDS 접속 안 됨
- 원인: Security Group에 3306 포트 규칙 없음
- 해결: `jinchul-db-sg`에 EC2 Security Group 소스로 인바운드 규칙 추가