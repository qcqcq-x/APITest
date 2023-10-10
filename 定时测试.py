import unittest
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from 正式链获取Token import TestToken
from 正式链上链 import TestOperchain
from 根据txid查询链上数据 import Testquery
from 根据Key查询value import Testvalue

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
SMTP_USERNAME = "2727687501@qq.com"
SMTP_PASSWORD = "uxdzfyzmwftqddaf"
EMAIL_FROM = "2727687501@qq.com"
EMAIL_TO = "694578311@qq.com"


def send_email(subject, message, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject

    body = MIMEText(message, 'plain')
    msg.attach(body)

    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
            msg.attach(part)

    # 连接到SMTP服务器并发送邮件
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())


def run_selected_test_suite(test_suite, test_case_name):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test_suite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 检查测试结果并发送邮件报警
    if not result.wasSuccessful():
        subject = f'Test Failure: {test_suite.__name__}.{test_case_name}'
        message = 'The following test(s) failed:\n\n'
        for failure in result.failures:
            test, trace = failure
            message += f'Test Case: {test.id()}\n{trace}\n\n'
        send_email(subject, message)


def main():
    parser = argparse.ArgumentParser(description="Run selected unit tests")
    parser.add_argument("test_file", help="Name of the test file (without '.py')")
    parser.add_argument("test_case_name", nargs="?", help="Name of the test case to run (optional)")

    args = parser.parse_args()
    test_suite = None
    if args.test_file == "test_module1":
        test_suite = TestToken
    elif args.test_file == "test_module2":
        test_suite = TestOperchain
    elif args.test_file == "test_module3":
        test_suite = Testquery
    elif args.test_file == "test_module4":
        test_suite = Testvalue

    if args.test_case_name:
        run_selected_test_suite(test_suite, args.test_case_name)
    else:
        if test_suite:
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromTestCase(test_suite)
            runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suite)
        else:
            print("Invalid test file name provided.")


if __name__ == "__main__":
    main()
