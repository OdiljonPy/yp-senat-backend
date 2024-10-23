from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ..models import Projects


class ProjectViewSetAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.project1 = Projects.objects.create(name='Project 1', short_description='short_d 1',
                                                description='description 1', status=1)

    def test_filter_by_query_params_status_success(self):
        url = reverse('projects')
        query_params = {'page': 1, 'page_size': 10, 'status': self.project1.status}
        response = self.client.get(url, query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_query_params_status_fail(self):
        url = reverse('projects')
        query_params = {'status': 15}
        response = self.client.get(url, query_params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_by_query_params_name_success(self):
        url = reverse('projects')
        query_params = {'name': self.project1.name}

        response = self.client.get(url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['content'][0]['name'], 'Project 1')
