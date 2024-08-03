from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserAuthTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
            email='testuser@example.com'
        )

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirection
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Check for redirection
        self.assertTrue(self.client.session.get('_auth_user_id'))

    def test_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Check for redirection
        self.assertIsNone(self.client.session.get('_auth_user_id'))
