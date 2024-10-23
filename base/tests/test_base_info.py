from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from base.models import BaseInfo


class BaseInfoViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('base_info_us')

        self.info1 = BaseInfo.objects.create(email='test1@example.com', address="Address 1",
                                             phone_number="+998934567289", latitude=2938.394982, longitude=9383.293839,
                                             telegram_url='telegram.org', instagram_url='instagram.com',
                                             facebook_url='facebook.com', youtube_url='youtube.com')
        self.info2 = BaseInfo.objects.create(email='test2@example.com', address="Address 2",
                                             phone_number="+998934567289", latitude=2938.394982, longitude=9383.293839,
                                             telegram_url='telegram.org', instagram_url='instagram.com',
                                             facebook_url='facebook.com', youtube_url='youtube.com')

    def test_base_info_get_positive(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['address'], "Address 2")

    def test_base_info_get_negative_no_data(self):
        self.info2.delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['result']['email'], "test2@example.com")
