from django.test import TestCase

from apps.users.models import User


class UserModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Tests if user creation with email is successful"""
        email = 'test@marsimon.com'
        password = 'testpassword123'

        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if the email for a new user is normalized"""
        email = 'Test@MARSIMON.COM'
        user = User.objects.create_user(email, 'test123')
        self.assertEqual(user.email, 'Test@marsimon.com')

    def test_new_user_invalid_email(self):
        """Tests if creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Tests creating a new superuser"""
        user = User.objects.create_superuser(
            'test@marsimon.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
