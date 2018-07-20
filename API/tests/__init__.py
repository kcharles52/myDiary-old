from api.views import app
from api.models import entries
import pytest
import unittest

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        entries.clear
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
        self.entry_data={
            "title":"wedding Dm",
            "date":"1/2/2017",
            "entryBody":"This some message for the entry in the diary",
            "entry_id":"1"
        }

    def tearDown(self):
        entries.clear

if __name__ == "__main__":
    unittest.main()
