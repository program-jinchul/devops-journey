#!/bin/bash
name="jinchul"
disk=$(df -h /mnt/c | tail -1)
echo "=== 시스템 모니터링 ==="
echo "날짜: $(date)"
echo "호스트명: $(hostname)"
echo "이름: $name"
echo "디스크: $disk"