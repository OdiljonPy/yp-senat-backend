from rest_framework.test import APITestCase, APIRequestFactory
from base.models import ContactUs
from base.serializers import ContactUsSerializer
from rest_framework import status
from base.views import ContactUsViewSet


class ContactUsTestCase(APITestCase):
    def setUp(self):
        ContactUs.objects.create(email='menotabek0@gamil.com', phone_number='+998938340103', address='flowers 5',
                                 latitude=83.8273, longitude=92.2882, telegram_url='telegram.org',
                                 instagram_url='instagram.com', facebook_url='facebook.com', youtube_url='youtube.com')
        ContactUs.objects.create(email='menotabek1@gamil.com', phone_number='+998938340103', address='flowers 5',
                                 latitude=83.8273, longitude=92.2882, telegram_url='telegram.org',
                                 instagram_url='instagram.com', facebook_url='facebook.com', youtube_url='youtube.com')
        ContactUs.objects.create(email='menotabek2@gamil.com', phone_number='+998938340103', address='flowers 5',
                                 latitude=83.8273, longitude=92.2882, telegram_url='telegram.org',
                                 instagram_url='instagram.com', facebook_url='facebook.com', youtube_url='youtube.com')

        self.factory = APIRequestFactory()

    def test_last_contact_us_data(self):
        request = self.factory.get('/contact/')
        contact_us_view_set = ContactUsViewSet.as_view({'get': 'contact_us_get'})
        response = contact_us_view_set(request)
        last_contact_us_data = ContactUs.objects.order_by('-created_at').first()
        excepted_data = {'result': ContactUsSerializer(last_contact_us_data, context={'request': request}).data,
                         'ok': True}
        self.assertEqual(response.data, excepted_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
