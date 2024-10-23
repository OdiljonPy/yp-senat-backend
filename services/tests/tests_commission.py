from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ..models import CommissionMember, CommissionCategory, Region


class CommissionViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.region = Region.objects.create(name='Test Region')
        self.category = CommissionCategory.objects.create(name='Test category number one')
        self.commission_member1 = CommissionMember.objects.create(
            commission_category=self.category,
            region=self.region,
            full_name="Test Member",
            position="Test Position",
            birthdate="1990-01-01",
            nation="Test Nation",
            education_degree="Test Degree",
            speciality="Test Speciality",
            email="test@example.com",
            type=1
        )

    def test_commission_member_detail_success(self):
        url = reverse('commission_detail', args=[self.commission_member1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ok'], True)

    def test_commission_member_detail_not_found(self):
        url = reverse('commission_detail', args=[45])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_commission_member_by_region_with_valid_id(self):
        url = reverse('region_commission')
        query_params = {'region_id': self.region.id}
        response = self.client.get(url, query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['result']), 0)

    def test_commission_member_by_region_with_invalid_id(self):
        url = reverse('region_commission')
        query_params = {'region_id': 'invalid'}
        response = self.client.get(url, query_params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_commission_member_by_region_without_id(self):
        url = reverse('region_commission')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ok'], True)
        self.assertEqual(len(response.data['result']), 1)
        self.assertGreater(len(response.data['result']), 0)

