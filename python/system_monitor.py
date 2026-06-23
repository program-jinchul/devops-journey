import psutil # 파이썬 라이브러리, cpu ram disk 사용량 측정 목적으로 사용
import time

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("C:\\")
        print(f"cpu 사용량: {cpu}%")
        print(f"ram 사용량: {ram}%")
        print(f"disk 사용량: {disk.percent}%")
        print("-" * 20)

        time.sleep(5)

except KeyboardInterrupt:
    print("모니터링 종료")