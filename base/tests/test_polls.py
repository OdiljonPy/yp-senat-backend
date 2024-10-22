from rest_framework.test import APITestCase, APIRequestFactory
from base.views import PollViewSet
from base.serializers import PollSerializer, TakePollSerializer
from base.models import Poll, PollResult
from rest_framework import status


class PollTestCase(APITestCase):
    def setUp(self):
        self.poll1 = Poll.objects.create(title='Python', description='Question and answers about Python programming.',
                                    participant_count=50)
        self.poll2 = Poll.objects.create(title='Django', description='Question and answers about Django programming.',
                                    participant_count=20)
        self.poll3 = Poll.objects.create(title='Election', description='Question and answers about election 2024.',
                                    participant_count=10)

        self.factory = APIRequestFactory()

    def test_get_polls(self):
        request = self.factory.get('/polls/')
        polls_view_set = PollViewSet.as_view({'get': 'get_polls'})
        response = polls_view_set(request)
        polls = Poll.objects.all()
        expected_data = {'result': PollSerializer(polls, many=True, context={'request': request}).data, 'ok': True}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_poll_without_result(self):
        request = self.factory.get('/polls/{self.poll1.id}/')
        poll_view_set = PollViewSet.as_view({'get': 'get_poll'})
        response = poll_view_set(request, pk=self.poll1.id)
        expected_data = {'result': PollSerializer(self.poll1, context={'request': request}).data, 'ok': True}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


