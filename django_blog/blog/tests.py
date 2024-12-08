from django.test import TestCase
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def test_user_registration(self):
        response = self.client.post("/register/", {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "strongpassword",
            "password2": "strongpassword",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

    def test_user_login(self):
        User.objects.create_user("testuser", "testuser@example.com", "strongpassword")
        response = self.client.post("/login/", {
            "username": "testuser",
            "password": "strongpassword",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
# Create your tests here.
