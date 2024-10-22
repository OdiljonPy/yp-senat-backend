
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from ..models import Banner
from ..views import BannerViewSet, RegionViewSet

class BannerAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BannerViewSet.as_view({'get': 'banner_list'})
        self.url = reverse('banner')
        Banner.objects.create(title='Banner', image='banner1.png')
        Banner.objects.create(image='banner1.png')

    def test_get(self):
        assert isinstance(self.url, object)
        request = self.factory.get(self.url)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
