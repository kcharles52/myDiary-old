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

    #tests for diary entries
    def test_create_entry(self):
        """ Tests whether a user can create a an entry successfully """
        response = self.test_client.post('/api/v1/users/entries', data=json.dumps(self.entry_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You have successfully created your entry",str(response.data))

    def test_create_entry_without_title(self):
        """ Tests whether a user can not create a an entry without a title """
        response = self.test_client.post('/api/v1/users/entries',data=json.dumps({"title":"","date":"2/2/2017","entryBody":"Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertIn('title is required',str(response.data))

    def test_create_entry_without_date(self):
        """ Tests whether a user can not create a an entry without a date """
        response = self.test_client.post('/api/v1/users/entries',data=json.dumps({"title":"Weed","date":"","entryBody":"Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertIn('date is required',str(response.data))

    # def test_get_all_entries_empty(self):
    #     """ Tests whether a user can't fetch entries when none exists """
    #     response = self.test_client.get('/api/v1/users/entries', data=json.dumps(self.entry_data), content_type='application/json')
    #     self.assertEqual(response.status_code,404)
    #     self.assertIn('You have no entries',str(response.data))

    def test_get_all_entries(self):
        """ Tests whether a user can get all entries """
        response = self.test_client.post('/api/v1/users/entries',data=json.dumps(self.entry_data), content_type='application/json')
        response = self.test_client.get('/api/v1/users/entries', data=json.dumps(self.entry_data), content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_get_single_entry(self):
        """ Tests  whether a entry can be returned by id successfully """
        response = self.test_client.post('/api/v1/users/entries',data=json.dumps(self.entry_data), content_type='application/json')
        response = self.test_client.get('/api/v1/users/entries/1', data=json.dumps(self.entry_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    # def test_modify_empty_entry(self):
    #     """ Tests whether a user can modify when there are no entries """
    #     response = self.test_client.put('/api/v1/users/entries/1', data=json.dumps({self.entry_data}), content_type='application/json')
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn("You have no entries to modify", str(response.data))

    def test_modify_entry(self):
        """ Tests whether a user can modify an entry successfully """
        response = self.test_client.post('/api/v1/users/entries',data=json.dumps(self.entry_data), content_type='application/json')
        response = self.test_client.put('/api/v1/users/entries/1', data=json.dumps(self.entry_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You successfully modified your entry",str(response.data))
