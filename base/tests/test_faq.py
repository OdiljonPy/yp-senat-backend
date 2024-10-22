from rest_framework.test import APIRequestFactory, APITestCase
from base.models import FAQ
from base.serializers import FAQSerializer
from base.views import FAQViewSet
from rest_framework import status


class FAQTestCase(APITestCase):
    def setUp(self):
        FAQ.objects.create(question='The most popular programming language is ?',
                                  answer='It is absolutely python', is_visible=True)
        FAQ.objects.create(question='Which database do you use ?', answer='SQL', is_visible=True)
        FAQ.objects.create(question='Which language do you use ?', answer='Python', is_visible=False)

        self.factory = APIRequestFactory()

    def test_get_visible_faq(self):
        request = self.factory.get('/faq/')
        faq_view_set = FAQViewSet.as_view({'get': 'faq_get'})
        response = faq_view_set(request)
        visible_faq = FAQ.objects.filter(is_visible=True)
        excepted_data = {'result': FAQSerializer(visible_faq, many=True, context={'request': request}).data, 'ok': True}
        self.assertEqual(response.data, excepted_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
