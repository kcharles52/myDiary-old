from api.views import app
import pytest
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client =app.test_client()
        self.user_data = {
            "name":"Kato",
            "email":"kato@gmail.com",
            "password":"123456"
        }
        self.user_login_data = {
            "email":"kato@gmail.com",
            "password":"123456"
        }


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()