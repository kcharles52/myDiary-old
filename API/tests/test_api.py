import json
import pytest
import unittest

from api.views import app


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client =app.test_client()
        self.user_data = {
            "name":"Kato",
            "email":"kato@gmail.com",
            "password":"123456"
        }
    def test_register_user(self):
        response = self.test_client.post('/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Kato has been registered', str(response.data))


if __name__=='__main__':
    unittest.main()