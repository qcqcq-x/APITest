from Selected import TestRunner


def main():
    test_runner = TestRunner()
    test_runner.add_tests("all")  # 这里可以指定你要运行的测试类
    test_runner.run_tests()


if __name__ == "__main__":
    main()
'''
对于Unix/Linux（使用cron）：
打开终端，运行来编辑你的cron作业表，然后添加以下行：
crontab -e
0 9 * * * /usr/bin/python3 /path/to/your/Datetime.py
这将在每天早上9点运行脚本。确保替换为你的Python脚本的实际路径。
对于Windows：
使用Windows任务计划程序（Task Scheduler）：
打开任务计划程序。
在右侧，选择"创建基本任务"。
按照向导的指示，选择启动程序，并选择Python解释器作为启动程序。
在"添加参数（可选）"中，输入你的的完整路径。Datetime.py
设置触发器为每天早上9点。
完成向导。
'''