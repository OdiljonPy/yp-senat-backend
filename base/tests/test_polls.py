from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from base.models import Poll, PollResult, Visitors
from django.urls import reverse


class PollViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.visitor = Visitors.objects.create(name='mozilla', ip='127.0.0.1')
        self.poll = Poll.objects.create(title='Poll 1', description='Sample poll', participant_count=5)
        self.poll_result = PollResult.objects.create(poll=self.poll, user=self.visitor)

    def test_get_polls_positive(self):
        url = reverse('polls')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 1)
        self.assertEqual(response.data['result'][0]['title'], 'Poll 1')

    def test_get_polls_negative(self):
        Poll.objects.all().delete()
        url = reverse('polls')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['result']), 0)

    def test_get_poll_positive(self):
        self.poll = Poll.objects.create(title='Poll one', description='Sample poll', participant_count=5)
        url = reverse('poll', kwargs={'pk': self.poll.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result']['title'], 'Poll one')

    def test_get_poll_negative(self):
        self.poll.delete()
        url = reverse('poll', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data['result']), 0)
