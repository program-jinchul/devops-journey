# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal DevOps learning log (Korean-language), not a deployable application. It mixes standalone practice scripts, Terraform IaC, and markdown notes. There is no build system, test suite, linter config, or dependency manifest. Write docs, comments, and TIL entries in Korean to match the existing content.

- `python/` — standalone boto3/psutil/requests scripts, each run directly (`python python/<script>.py`). Most are interactive (`input()`) and act on **real AWS resources** as soon as they run (start/stop EC2 and RDS, S3 upload/delete). Don't execute them to "test" a change without the user's OK.
- `bash/` — small shell practice scripts.
- `terraform/` — root module that calls `modules/vpc` and `modules/ec2`.
- `aws/` — per-service notes (VPC, EC2, RDS, S3, IAM, CloudWatch).
- `TIL/` — daily notes named `YYYY-MM-DD.md` (a multi-day entry uses `YYYY-MM-DD~DD.md`).

## Commands

Run scripts from the repo root. Paths like `python/test.txt` and `cwd="terraform"` in the scripts assume that.

```bash
# Terraform (from terraform/)
terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply      # creates real AWS resources — confirm with the user first
terraform output instance_id

# Python (no requirements file; deps used: boto3, psutil, requests, python-dotenv)
python python/terraform_boto3.py
```

`github_grass.py` reads `GITHUB_TOKEN` from a `.env` file at the repo root. `.env`, `.terraform/`, and tfstate files are gitignored. `.terraform.lock.hcl` is committed and includes linux_amd64 hashes.

## Architecture notes

- **Region:** everything is hardcoded to `ap-northeast-2` (Seoul), both the Terraform provider and every boto3 client.
- **Terraform data flow:** root `main.tf` passes `module.vpc.vpc_id` / `module.vpc.subnet_id` into the `ec2` module. The VPC module builds a single public subnet with an IGW, a route table, and an association. The EC2 module owns its security group (22 and 80 open to 0.0.0.0/0) and a fixed AMI. Modules don't declare their own `terraform`/`provider` blocks. A module variable without a `default` is required and must be passed from the root.
- **Terraform → Python link:** `python/terraform_boto3.py` shells out to `terraform output instance_id` in `terraform/` and then queries that instance with boto3. That only works if the **root** module exposes `instance_id`. Right now `terraform/outputs.tf` is empty, and only `modules/ec2/outputs.tf` defines it. To fix this, re-export it at the root (`value = module.ec2.instance_id`).
- `terraform/variables.tf` holds stale root variables (`instance_type`, plus `subnet_id` with a hardcoded old subnet ID) that `main.tf` doesn't use. `main.tf` passes literals into the modules instead.
- **Hardcoded resource identifiers** across the Python scripts: EC2 `i-0e36eada750cf6cab`, RDS `jinchul-db`, S3 bucket `jinchul-devops-bucket`. Resource `Name` tags follow the `jinchul-<resource>-tf` pattern for Terraform-managed resources.
- `python/system_monitor.py` and `bash/system_monitor.sh` assume Windows/WSL disk paths (`C:\\`, `/mnt/c`).

## Conventions

Commit messages use Conventional Commits prefixes: `feat:`, `docs:`, `refactor:`, `chore:`, `fix:`.

## 규칙
- 커밋 컨벤션: feat / docs / refactor / chore / fix
- 파일·폴더명: 영문_언더바
- 시크릿은 .env에만, 절대 커밋 금지 (.gitignore 확인)
- AWS 리전: ap-northeast-2

## AWS 권한
- 기본 프로필은 claude-readonly (조회 전용)
- jinchul-dev 프로필은 내가 명시적으로 요청할 때만 사용
- terraform apply / destroy, 리소스 생성·삭제는 실행 전 반드시 확인 받기
- python/ 스크립트는 실제 AWS 리소스를 건드리므로 내 승인 없이 실행 금지

## 작업 방식
- 요구사항이 모호하면 코드 작성 전에 질문
- 완료 처리 전에 검증 명령어와 결과 제시
