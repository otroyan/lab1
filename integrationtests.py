import requests
import unittest
import run
import json
import threading
import os


class IntegrTests(unittest.TestCase):
    listener_process = None

    @classmethod
    def setUpClass(cls):
        cls.listener_process = threading.Thread(target=run.start_service,
                                                kwargs=dict(host='localhost',
                                                            port=12000))
        cls.listener_process.start()

    def test_prime_numbers(self):
        r = requests.get('http://127.0.0.1:12000/isprime?num=11')
        json_obj = json.loads(r.text)
        self.assertTrue(json_obj["is_prime"])

        r = requests.get('http://127.0.0.1:12000/isprime?num=12')
        json_obj = json.loads(r.text)
        self.assertFalse(json_obj["is_prime"])

        r = requests.get('http://127.0.0.1:12000/isprime?num=0')
        json_obj = json.loads(r.text)
        self.assertFalse(json_obj["is_prime"])

    @classmethod
    def tearDownClass(self):
        pass
        #TODO


if __name__ == '__main__':
    unittest.main()
