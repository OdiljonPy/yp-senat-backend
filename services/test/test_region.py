
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from ..models import Region
from ..views import RegionViewSet


class RegionAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RegionViewSet.as_view({'get': 'region_list'})
        self.url = reverse('region')
        Region.objects.create(name='test')

    def test_get(self):
        assert isinstance(self.url, object)
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'][0]['name'], 'test')
