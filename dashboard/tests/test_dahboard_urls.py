from django.test import TestCase
from django.urls import reverse


# Verifica a url
class DashboardURLsTest(TestCase):
    def test_dashboard_url_is_correct(self):
        index_url = reverse('index')
        self.assertEqual(index_url, '/')