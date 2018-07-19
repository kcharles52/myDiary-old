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
        self.user_login_data = {
            "email":"kato@gmail.com",
            "password":"123456"
        }
    #User registration tests
    def test_register_user(self):
        response = self.test_client.post('/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Kato has been registered', str(response.data))

    def test_register_user_fail(self):
        """Ensure user registration with incomplete data fails"""
        response = self.test_client.post('/register', data=json.dumps({"name":"kato","email":"","password":"12345"}),content_type='application/json')
        self.assertEqual(response.status_code,400)

    #User login tests
    def test_user_login(self):
        response = self.test_client.post('/login', data=json.dumps(self.user_login_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome Kato. You are logged in",str(response.data))




if __name__=='__main__':
    unittest.main()