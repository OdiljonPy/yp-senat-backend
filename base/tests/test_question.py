from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from base.models import Poll, Question
from django.urls import reverse

class QuestionViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.poll = Poll.objects.create(title='Poll 1', description='Sample poll')
        self.question1 = Question.objects.create(poll=self.poll, text='What is your name?')
        self.question2 = Question.objects.create(poll=self.poll, text='What is your surname?')

    def test_next_question(self):
        url = reverse('next_question', args=[self.question1.id])
        response = self.client.get(url)
        next_question = Question.objects.filter(id__gt=self.question1.id).order_by('id').first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next_question.text, 'What is your surname?')

    def test_next_question_negative(self):
        self.question2.delete()
        url = reverse('next_question', args=[self.question1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
