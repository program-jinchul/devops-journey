# CloudWatch

## 개념
AWS 서비스의 모니터링 및 로그 수집 서비스. 장애 감지와 알람 설정이 가능하다.

## 구성 요소

### Metrics
- EC2 CPU, 메모리, 네트워크 등 실시간 수치

### Alarms
- 특정 수치 초과 시 알람 발생
- SNS Topic을 통해 이메일 알림 전송

### Dashboard
- 메트릭을 시각화해서 한눈에 볼 수 있는 대시보드

### Logs
- EC2 로그를 CloudWatch로 전송해서 중앙 관리

## 실습 구성
- CPU 80% 초과 시 이메일 알람 설정
- CloudWatch Dashboard 생성 (CPUUtilization 위젯)
- CloudWatch Agent 설치 및 Nginx access.log 수집

## 트러블슈팅
- 문제: CloudWatch Logs에 로그 안 뜸
- 원인 1: IAM Role에 CloudWatchAgentServerPolicy 없음
- 원인 2: cwagent가 nginx 로그 파일 읽기 권한 없음
- 해결: 권한 추가 + `chmod 644 /var/log/nginx/access.log`