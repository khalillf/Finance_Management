from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'phone_number': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_user_profile(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')