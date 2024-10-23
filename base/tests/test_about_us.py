from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from base.models import AboutUs
from django.urls import reverse


class AboutUsViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('about_us')
        self.about1 = AboutUs.objects.create(description='About Us 1')
        self.about2 = AboutUs.objects.create(description='About Us 2')

    def test_about_us_get_positive(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['description'], 'About Us 2')

    def test_about_us_get_negative(self):
        self.about2.delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['description'], 'About Us 1')
