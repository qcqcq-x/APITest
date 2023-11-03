import unittest
import requests


def get_token():
    login_url = "http://chain.repchain.net.cn/uct/api/v1/gateway/login"
    login_payload = {
        "username": "710601443331",
        "password": "a123456",
        "clientId": "aa02cf9a-d010-4e50-9c32-5ff1fc1043a9"
    }
    headers: dict[str, str] = {"Content-Type": "application/json"}
    # 发送获取token请求
    response = requests.post(login_url, json=login_payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    token = data.get("datas")
    return token


class Testquery(unittest.TestCase):
    def setUp(self):
        self.token = get_token()

    def test_C1(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
        }
        query_url = "http://chain.repchain.net.cn/uct/api/v1/data/query"
        query_payload = {
            "txId": "759c892a-5eea-4dea-9863-acdf991e0432"
        }

        response = requests.post(query_url, json=query_payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_C2(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
        }
        query_url = "http://chain.repchain.net.cn/uct/api/v1/data/query"
        query_payload = {
            "txId": "null"
        }

        response = requests.post(query_url, json=query_payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("txid不正确", response.text)


if __name__ == '__main__':
    unittest.main()
