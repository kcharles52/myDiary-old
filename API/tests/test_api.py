import json
from tests import BaseTestCase

from api.views import app


class ApiTestCase(BaseTestCase):

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
        self.assertIn("Welcome. You are logged in",str(response.data))

    def test_login_without_password(self):
        response = self.test_client.post('/login', data=json.dumps({"email":"kato@gmail.com", "password":" "}), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('password  is required',str(response.data))

    def test_login_without_email(self):
        response = self.test_client.post('/login', data=json.dumps({"email":" ", "password":"123456"}), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('email is required',str(response.data))
