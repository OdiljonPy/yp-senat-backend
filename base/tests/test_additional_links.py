from rest_framework.test import APIRequestFactory, APITestCase
from base.models import AdditionalLinks
from base.serializers import AdditionalLinksSerializer
from rest_framework import status
from base.views import AdditionalLinksViewSet


class AdditionalLinksTestCase(APITestCase):
    def setUp(self):
        AdditionalLinks.objects.create(title='telegram_url', link='telegram.org', image='add_links/image1.jpg', is_visible=True)
        AdditionalLinks.objects.create(title='instagram_url', link='instagram.com', image='add_links/image2.png', is_visible=True)
        AdditionalLinks.objects.create(title='youtube_url', link='youtube.com', image='add_links/image3.jpeg', is_visible=False)

        self.factory = APIRequestFactory()

    def test_additional_links(self):
        request = self.factory.get('/additional/')
        additional_links_view_set = AdditionalLinksViewSet.as_view({'get': 'additional_links_get'})
        response = additional_links_view_set(request)
        visible_data = AdditionalLinks.objects.filter(is_visible=True)
        excepted_data = {'result': AdditionalLinksSerializer(visible_data, many=True, context={'request': request}).data, 'ok': True}
        self.assertEqual(response.data, excepted_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

