from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTest(TestCase):
    """Sign Up Page Test"""

    def test_url_exist_at_correct_signupview(self):
        """Test url exist at correct location in the sign up view"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """Test signup view name"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """Tet sign up form"""
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        all_users = get_user_model().objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(all_users.count(), 1)
        self.assertEqual(all_users[0].username, "testuser")
        self.assertEqual(all_users[0].email, "testuser@email.com")
