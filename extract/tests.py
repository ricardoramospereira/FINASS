from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ExtractURLsTest(TestCase):
    def test_extract_url_is_correct(self):
        self.ass