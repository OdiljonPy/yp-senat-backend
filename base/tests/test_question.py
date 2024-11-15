from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from base.models import Poll, Question, Option, PollAnswer, PollResult, Visitors
from django.urls import reverse


class QuestionViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.poll1 = Poll.objects.create(title='Poll 1', description='Sample poll 1')
        self.poll2 = Poll.objects.create(title='Poll 2', description='Sample poll 2')
        self.question1 = Question.objects.create(poll=self.poll1, text='What is your name?')
        self.question2 = Question.objects.create(poll=self.poll2, text='What is your surname?')
        self.question3 = Question.objects.create(poll=self.poll1, text='What is your fullname?')
        self.option1 = Option.objects.create(question=self.question3, text='Option 1')
        self.option2 = Option.objects.create(question=self.question3, text='Option 2')
        self.visitor = Visitors.objects.create(name='mozilla', ip='127.0.0.1')
        self.result = PollResult.objects.create(user=self.visitor, poll=self.poll1)
        self.answer1 = PollAnswer.objects.create(question=self.question1, result=self.result)
        self.answer1.answer.set([self.option1])
        self.answer2 = PollAnswer.objects.create(question=self.question1, result=self.result)
        self.answer2.answer.set([self.option2])


    def test_next_question(self):
        url = reverse('next_question', args=[self.question1.id])
        response = self.client.get(url)
        next_question = Question.objects.filter(id__gt=self.question1.id, poll_id=self.question1.poll.id).order_by('id').prefetch_related(
            'options').first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next_question.text, 'What is your fullname?')

    def test_next_question_negative(self):
        self.question3.delete()
        url = reverse('next_question', args=[self.question1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
