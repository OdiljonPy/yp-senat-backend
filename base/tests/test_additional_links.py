from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from base.models import AdditionalLinks


class AdditionalLinksViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('additional_links')

        self.link1 = AdditionalLinks.objects.create(title="Link 1", link="http://link1.com",
                                                    image='additional_links/image1.jpg', is_visible=True)
        self.link2 = AdditionalLinks.objects.create(title="Link 2", link="http://link2.com",
                                                    image='additional_links/image2.png', is_visible=True)
        self.link3 = AdditionalLinks.objects.create(title="Link 3", link="http://link3.com",
                                                    image='additional_links/image3.jpeg', is_visible=False)

    def test_additional_links_get_positive(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 2)
        self.assertEqual(response.data['result'][0]['title'], "Link 2")
        self.assertEqual(response.data['result'][1]['title'], "Link 1")

    def test_additional_links_get_negative_no_visible_links(self):
        AdditionalLinks.objects.filter(is_visible=True).delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 0)
