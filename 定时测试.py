import sched
import time
import subprocess
import os
from datetime import datetime, timedelta

test_commands = [
    "python 选择测试.py test_Token",
    "python 选择测试.py test_Opearchain",
    "python 选择测试.py test_Query",
    "python 选择测试.py test_Value"
]

working_directory = r"C:\Users\86182\PycharmProjects\pythonProject"
# 定义每日执行测试的时间
# 格式: (小时, 分钟, 秒)
test_time = (13, 59, 00)
scheduler = sched.scheduler(time.time, time.sleep)


def run_tests(sc):
    now = datetime.now().time()

    if now.hour == test_time[0] and now.minute == test_time[1] and now.second == test_time[2]:
        print(f"Running tests at {now}")
        os.chdir(working_directory)
        for cmd in test_commands:
            full_command = f" {cmd}"
            result = subprocess.call(full_command, shell=True)
            if result == 0:
                print(f"Test successful: {full_command}")
            else:
                print(f"Test failed: {full_command}")
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    else:
        print(f"Waiting for {test_time[0]}:{test_time[1]}:{test_time[2]}")

    current_datetime = datetime.now()
    next_test_time = current_datetime.replace(hour=test_time[0], minute=test_time[1], second=test_time[2])

    if current_datetime > next_test_time:
        next_test_time = next_test_time + timedelta(days=1)

    wait_time = (next_test_time - current_datetime).total_seconds()
    print(f"Next test in {wait_time} seconds")
    sc.enter(wait_time, 1, run_tests, (sc,))


scheduler.enter(0, 1, run_tests, (scheduler,))
scheduler.run()
