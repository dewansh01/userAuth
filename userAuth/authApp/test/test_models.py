"""
Tests for models
"""

from django.test import TestCase
from  django.contrib.auth import get_user_model
class modelTests(TestCase):
    """
    Tests for models
    """
    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """
        Test the email for a new user is normalized
        """
        sample_emails = [
            ['test1@EXAMPLE.COM','test1@example.com'],
            ['Test2@example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
        ]
        for email , expected in sample_emails:
            user = get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,expected)


    def test_new_user_without_email_raises_error(self):
        """
            Test that creating user without email raises value error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','sample123')

    def test_create_superuser(self):
        """
            Test creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'sample123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)