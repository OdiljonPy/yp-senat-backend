from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from base.models import FAQ
from django.urls import reverse


class FAQViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('faq')
        self.faq1 = FAQ.objects.create(question='What is X?', answer='X is answer of Y', is_visible=True)
        self.faq2 = FAQ.objects.create(question='What is Y?', answer='Y is answer of Z', is_visible=False)

    def test_faq_get_positive(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 1)
        self.assertEqual(response.data['result'][0]['question'], 'What is X?')

    def test_faq_get_negative(self):
        FAQ.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 0)
