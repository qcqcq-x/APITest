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


class TestOperchain(unittest.TestCase):
    def setUp(self):
        self.token = get_token()

    def test_B1(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
                   }
        chain_url = "http://chain.repchain.net.cn/uct/api/v1/data/oper_chain"
        chain_payload = {
            "token": "3864bb814fc64e605cf9dedf58a06e44",
            "data": "0a206136386239613737376663623436373462373435653135343834303\
            06633306610021a130a0f4465706f736974436f6e747261637410012a550a07646570\
            6f736974124a7b22756e697175654964223a2263356536666162312d666338352d343\
            138342d393832662d346430646562623864306461222c22636f6e74656e74223a2274\
            6573745f76616c7565227d3a730a1b0a123132313030303030356c33353132303435361\
            2056e6f646531120b08c5eeb69906108085d41b1a47304502202463276c202f45cc526\
            2a00f9729db36017e348adc2cc532b8f292b678313134022100a32175649376dc50fe8\
            4e47206172b9bc3a86cbab17033fa5c75e33ba6199772",
            "callbackIp": "http://192.168.19.121:9003/api/front/pushChain/callback",
            "chainKey": "123121"
        }

        response = requests.post(chain_url, json=chain_payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_B2(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
        }
        chain_url = "http://chain.repchain.net.cn/uct/api/v1/data/oper_chain"
        chain_payload = {
            "token": "3864bb814fc64e605cf9dedf58a06e44",
            "data": "null",
            "callbackIp": "http://192.168.19.121:9003/api/front/pushChain/callback",
            "chainKey": "123121"
        }

        response = requests.post(chain_url, json=chain_payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("data不正确", response.text)

    def test_B3(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
        }
        chain_url = "http://chain.repchain.net.cn/uct/api/v1/data/oper_chain"
        chain_payload = {
            "token": "3864bb814fc64e605cf9dedf58a06e44",
            "data": "0a206136386239613737376663623436373462373435653135343834303\
                   06633306610021a130a0f4465706f736974436f6e747261637410012a550a07646570\
                   6f736974124a7b22756e697175654964223a2263356536666162312d666338352d343\
                   138342d393832662d346430646562623864306461222c22636f6e74656e74223a2274\
                   6573745f76616c7565227d3a730a1b0a123132313030303030356c33353132303435361\
                   2056e6f646531120b08c5eeb69906108085d41b1a47304502202463276c202f45cc526\
                   2a00f9729db36017e348adc2cc532b8f292b678313134022100a32175649376dc50fe8\
                   4e47206172b9bc3a86cbab17033fa5c75e33ba6199772",
            "callbackIp": "null",
            "chainKey": "123121"
        }

        response = requests.post(chain_url, json=chain_payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("callbackIp不正确", response.text)

    def test_B4(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {self.token}"
        }
        chain_url = "http://chain.repchain.net.cn/uct/api/v1/data/oper_chain"
        chain_payload = {
            "token": "3864bb814fc64e605cf9dedf58a06e44",
            "data": "0a206136386239613737376663623436373462373435653135343834303\
                           06633306610021a130a0f4465706f736974436f6e747261637410012a550a07646570\
                           6f736974124a7b22756e697175654964223a2263356536666162312d666338352d343\
                           138342d393832662d346430646562623864306461222c22636f6e74656e74223a2274\
                           6573745f76616c7565227d3a730a1b0a123132313030303030356c33353132303435361\
                           2056e6f646531120b08c5eeb69906108085d41b1a47304502202463276c202f45cc526\
                           2a00f9729db36017e348adc2cc532b8f292b678313134022100a32175649376dc50fe8\
                           4e47206172b9bc3a86cbab17033fa5c75e33ba6199772",
            "callbackIp": "http://192.168.19.121:9003/api/front/pushChain/callback",
            "chainKey": "null"
        }

        response = requests.post(chain_url, json=chain_payload, headers=headers)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("callbackIp不正确", response.text)


if __name__ == '__main__':
    unittest.main()
