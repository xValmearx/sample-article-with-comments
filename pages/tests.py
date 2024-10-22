from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):
    """Home Page Test"""

    def test_url_exis_at_correct_location_homepage(self):
        """test url eist at the correct location in the homepage"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
