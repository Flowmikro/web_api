from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='existingpassword'
        )

    def test_user_registration(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_add'))
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())

    def test_user_login(self):
        response = self.client.post(self.login_url, data={'username': 'existinguser', 'password': 'existingpassword'})
        self.assertEqual(response.status_code, 302)

    def test_user_logout(self):
        self.client.login(username='existinguser', password='existingpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
