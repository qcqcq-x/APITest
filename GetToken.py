import unittest
import requests

url = "http://chain.repchain.net.cn/uct/api/v1/gateway/login"
headers = {"Content-Type": "application/json"}


class TestToken(unittest.TestCase):

    def test_A1(self):
        payload = {
            "username": "710601443331",
            "password": "a123456",
            "clientId": "aa02cf9a-d010-4e50-9c32-5ff1fc1043a9"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_A2(self):
        payload = {
            "username": "username",
            "password": "password",
            "clientId": "aa02cf9a-d010-4e50-9c32-5ff1fc1043a9"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("用户名或密码无效", response.text)

    def test_A3(self):
        payload = {
            "username": "username",
            "clientId": "aa02cf9a-d010-4e50-9c32-5ff1fc1043a9"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("缺少必要参数", response.text)

    def test_A4(self):
        payload = {
            "username": "username",
            "password": "password",
            "clientId": "null"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("用户名或密码无效", response.text)


if __name__ == '__main__':
    unittest.main()
