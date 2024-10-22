from rest_framework.test import APITestCase, APIRequestFactory
from base.models import AboutUs
from rest_framework import status
from base.views import AboutUsViewSet
from base.serializers import AboutUsSerializer


class AboutUsTestCase(APITestCase):
    def setUp(self):
        AboutUs.objects.create(title='Python', description='It is the best programming language',
                               file='about_us/file1.jpg', is_video=False, telegram_url='telegram.org',
                               instagram_url='instagram.com', facebook_url='facebook.com', youtube_url='youtube.com')
        AboutUs.objects.create(title='Django', description='It is the best python framework', file='about_us/file2.mp4',
                               is_video=True, telegram_url='telegram.org', instagram_url='instagram.com',
                               facebook_url='facebook.com', youtube_url='youtube.com')
        AboutUs.objects.create(title='SQL', description='It is the best database', file='about_us/file3.png',
                               is_video=False, telegram_url='telegram.org', instagram_url='instagram.com',
                               facebook_url='facebook.com', youtube_url='youtube.com')

        self.factory = APIRequestFactory()

    def test_about_us(self):
        request = self.factory.get('/about/')
        about_us_view_set = AboutUsViewSet.as_view({'get': 'about_us_get'})
        response = about_us_view_set(request)
        last_data = AboutUs.objects.order_by('-created_at').first()
        excepted_data = {'result': AboutUsSerializer(last_data, context={'request': request}).data,
                         'ok': True}
        self.assertEqual(response.data, excepted_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
