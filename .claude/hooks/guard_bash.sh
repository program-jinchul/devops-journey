#!/usr/bin/env bash
# PreToolUse 가드: 위험한 Bash 명령을 코드로 차단
# exit 2 = 차단 (stderr 메시지가 Claude에게 전달됨), exit 0 = 통과
cmd=$(jq -r '.tool_input.command // empty')

block() { echo "BLOCKED by guard_bash.sh: $1" >&2; exit 2; }

[[ "$cmd" =~ terraform[[:space:]]+(apply|destroy|import) ]] && block "terraform 변경 명령은 사용자가 직접 실행"
[[ "$cmd" =~ terraform[[:space:]]+state[[:space:]]+(rm|mv|push) ]] && block "terraform state 변경 금지"
[[ "$cmd" =~ aws[[:space:]].*[[:space:]](delete|terminate|remove|create|put|run|stop|start|modify|update|attach|detach|reboot)- ]] && block "AWS 리소스 변경 API 금지"
[[ "$cmd" =~ aws[[:space:]]+s3[[:space:]]+(rm|rb|mb|mv|cp|sync) ]] && block "S3 쓰기 명령 금지"
[[ "$cmd" =~ (^|[^a-zA-Z0-9_.-])aws[[:space:]] && ! "$cmd" =~ --profile[[:space:]=]+claude-readonly([^-a-zA-Z0-9_]|$) ]] && block "aws 명령은 --profile claude-readonly 필수"
[[ "$cmd" =~ python3?[[:space:]]+(\./)?python/ ]] && block "python/ 스크립트는 실제 AWS를 건드리므로 사용자가 직접 실행"
[[ "$cmd" =~ rm[[:space:]]+-[a-zA-Z]*(rf|fr) ]] && block "rm -rf 금지"
[[ "$cmd" =~ git[[:space:]]+push ]] && block "push는 사용자가 직접"
[[ "$cmd" =~ (^|[[:space:];&|])gh[[:space:]]+(api|.*[[:space:]](create|edit|close|delete|merge|comment|reopen|review|run|set|archive|rename|fork|enable|disable)) ]] && block "gh 쓰기 명령은 사용자가 직접"

exit 0
