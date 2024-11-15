from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ..models import Post, CommissionMember, Region, CommissionCategory


class PostViewSetTestCase(APITestCase):
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

        self.post1 = Post.objects.create(title='Test Post_1', short_description='Test short description number one',
                                         description='Test description number one',
                                         commission_member=self.commission_member1, )
        self.post2 = Post.objects.create(title='Test Post_2', short_description='Test short description number two',
                                         description='Test description number two')

    def test_post_list_by_member_has(self):
        url = reverse('post_by_member')
        query_params = {'q': 'test', 'post_member_exist': False}
        response = self.client.get(url, query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list_by_member_null(self):
        url = reverse('post_by_member')
        query_params = {'q': 'test', 'post_member_exist': True}
        response = self.client.get(url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


