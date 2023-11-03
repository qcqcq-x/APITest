from test_suite import TestToken, TestOperchain, Testquery, Testvalue
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


email_config = {
    'sender_email': '2727687501@qq.com',
    'receiver_email': '694578311@qq.com',
    'password': 'uxdzfyzmwftqddaf',
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 587,
}


class TestRunner:
    def __init__(self):
        self.loader = unittest.TestLoader()
        self.suite = unittest.TestSuite()

    def add_tests(self, test_classes, test_name=None):
        if test_classes == "all":
            self.suite.addTests(self.loader.loadTestsFromTestCase(TestToken))
            self.suite.addTests(self.loader.loadTestsFromTestCase(TestOperchain))
            self.suite.addTests(self.loader.loadTestsFromTestCase(Testquery))
            self.suite.addTests(self.loader.loadTestsFromTestCase(Testvalue))
        elif test_classes == "TestToken":
            if test_name is None:
                self.suite.addTests(self.loader.loadTestsFromTestCase(TestToken))
            else:
                self.suite.addTest(TestToken(test_name))
        elif test_classes == "TestOperchain":
            if test_name is None:
                self.suite.addTests(self.loader.loadTestsFromTestCase(TestOperchain))
            else:
                self.suite.addTest(TestOperchain(test_name))
        elif test_classes == "Testquery":
            if test_name is None:
                self.suite.addTests(self.loader.loadTestsFromTestCase(Testquery))
            else:
                self.suite.addTest(Testquery(test_name))
        elif test_classes == "Testvalue":
            if test_name is None:
                self.suite.addTests(self.loader.loadTestsFromTestCase(Testvalue))
            else:
                self.suite.addTest(Testvalue(test_name))
        else:
            print("Invalid test class.")

    def run_tests(self):
        runner = unittest.TextTestRunner(stream=open("test_results.txt", "w"))
        result = runner.run(self.suite)
        if result.wasSuccessful():
            print("test was successful")
        else:
            subject = "Test Failure Alert"
            body = "Some tests have failed. Please check the attached test results."

            msg = MIMEMultipart()
            msg['From'] = email_config['sender_email']
            msg['To'] = email_config['receiver_email']
            msg['Subject'] = subject

            text = MIMEText(body)
            msg.attach(text)
            test_results = "test_results.txt"

            with open(test_results, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype="txt")
                attachment.add_header('Content-Disposition', 'attachment', filename=test_results)
                msg.attach(attachment)

            # 发送邮件
            try:
                server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
                server.starttls()
                server.login(email_config['sender_email'], email_config['password'])
                server.sendmail(email_config['sender_email'], email_config['receiver_email'], msg.as_string())
                server.quit()
                print("Email alert sent successfully.")
            except Exception as e:
                print(f"Email alert could not be sent. Error: {str(e)}")


if __name__ == '__main__':
    test_runner = TestRunner()

    print("Select a test class to run:")
    print("1. TestToken")
    print("2. TestOperchain")
    print("3. Testquery")
    print("4. Testvalue")
    print("5. Run all tests")
    print("6. Run specific test case")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        test_runner.add_tests("TestToken")
        test_runner.run_tests()
    elif choice == "2":
        test_runner.add_tests("TestOperchain")
        test_runner.run_tests()
    elif choice == "3":
        test_runner.add_tests("Testquery")
        test_runner.run_tests()
    elif choice == "4":
        test_runner.add_tests("Testvalue")
        test_runner.run_tests()
    elif choice == "5":
        test_runner.add_tests("all")
        test_runner.run_tests()
    elif choice == "6":
        print("Select a test class:")
        print("1. TestToken")
        print("2. TestOperchain")
        print("3. Testquery")
        print("4. Testvalue")

        test_class_choice = input("Enter your choice: ")

        if test_class_choice == "1":
            test_class = "TestToken"
        elif test_class_choice == "2":
            test_class = "TestOperchain"
        elif test_class_choice == "3":
            test_class = "Testquery"
        elif test_class_choice == "4":
            test_class = "Testvalue"
        else:
            print("Invalid choice. Please enter a valid option.")
            exit()

        print(f"Select a test case in {test_class}:")
        test_case_names = {
            "TestToken": ["test_A1", "test_A2", "test_A3", "test_A4"],
            "TestOperchain": ["test_B1", "test_B2", "test_B3", "test_B4"],
            "Testquery": ["test_C1", "test_C2"],
            "Testvalue": ["test_D1", "test_D2"],
        }

        for i, test_case in enumerate(test_case_names[test_class], start=1):
            print(f"{i}. {test_case}")

        test_case_choice = input("Enter your choice: ")

        try:
            selected_test_case = test_case_names[test_class][int(test_case_choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid option.")
            exit()

        test_runner.add_tests(test_class, selected_test_case)
        test_runner.run_tests()

    elif choice == "7":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a valid option.")
