from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from apps.users.models import User


CREATE_USER_URL = reverse('users:register')
TOKEN_OBTAIN_URL = reverse('token_obtain_pair')
TOKEN_REFRESH_URL = reverse('token_refresh')


class PublicUserViewTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {'email': 'test@marsimon.com', 'password': 'a;d+-394hasldf0)'}

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_exists(self):
        """Test creating user that already exists"""
        payload = {'email': 'test@marsimon.com', 'password': 'a;d+-394hasldf0)'}
        User.objects.create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_password_too_short_fails(self):
        """Test that the password must be more than 5 characters"""
        payload = {'email': 'test@marsimon.com', 'password': 'pw'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_password_too_common_fails(self):
        """Test that the password must not be a common password"""
        payload = {'email': 'test@marsimon.com', 'password': 'testing123'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_password_only_digits_fails(self):
        """Test that the password must not contain only digits"""
        payload = {'email': 'test@marsimon.com', 'password': '32198413216541984321654'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_password_email_similar_fails(self):
        """Test that the password must not contain only digits"""
        payload = {'email': 'ihavebluehair@marsimon.com', 'password': 'ihavebluehair@marsimon'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_obtain_token_pair_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@marsimon.com', 'password': 'a;d+-394hasldf0)'}
        User.objects.create_user(**payload)

        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that a token is not created if invalid credentials are given"""
        User.objects.create_user(email='test@marsimon.com', password='a;d+-394hasldf0)')
        payload = {'email': 'test@marsimon.com', 'password': 'wrongpassword'}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_no_user(self):
        """Test that token is not created when user does not exist"""
        payload = {'email': 'test@marsimon.com', 'password': 'a;d+-394hasldf0)'}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_OBTAIN_URL, {'password': 'a;d+-394hasldf0)'})

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh_token(self):
        """Test that refresh token works properly"""
        payload = {'email': 'test@marsimon.com', 'password': 'password123'}
        User.objects.create_user(**payload)
        res = self.client.post(TOKEN_OBTAIN_URL, payload)

        refreh_token = res.data['refresh']
        res2 = self.client.post(TOKEN_REFRESH_URL, {'refresh': refreh_token})
        self.assertIn('access', res2.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_refresh_token_invalid(self):
        """Test that refresh token returns 401 when invalid"""
        payload = {'refresh': 'some_invalid_token'}
        res = self.client.post(TOKEN_REFRESH_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', res.data)
