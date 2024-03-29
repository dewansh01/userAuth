"""
Tests for user API
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('authApp:create')
TOKEN_URL=reverse('authApp:token')
ME_URL = reverse('authApp:me')

def create_user(**params):
    """"
        create a new user
    """
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """
        Test the users API (public)
    """

    def setUp(self):
        self.client = APIClient()
    def test_create_valid_user_success(self):
        """
            Test creating user with valid payload is successful
        """
        payload={
            'email':'test@example.com',
            'name' : 'Test name',
            'password' : 'testpass',
        }
        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)

    def test_user_with_email_exists_error(self):
        """
            Test error returned if user with email already exists
        """
        payload={
            'email':'test@example.com',
            'name' : 'Test name',
            'password' : 'testpass',
        }
        create_user(**payload)
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        #this test is to check if the password is too short
        payload={
            'email':'test@example.com',
            'name' : 'Test name',
            'password' : 'test',
        }
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

        def test_update_user_profile(self):
            """
            Test updating the user profile for the authenticated user.
            """
            payload ={
            'email':'test2@example.com',
            'name' : 'Test name2',
            'password' : 'test@222',
            }
            res = self.client.patch(ME_URL,payload)

            self.user.refresh_from_db()
            self.assertEqual(self.user.name,payload['name'])
            self.assertTrue(self.user.check_password(payload['password']))
            self.assertEqual(res.status_code,status.HTTP_200_OK)