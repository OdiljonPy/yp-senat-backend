from services.utils import get_ip
from .models import FAQ, AboutUs, AdditionalLinks, BaseInfo, Poll, Question, PollResult, Banner
from .serializers import (
    FAQSerializer, AdditionalLinksSerializer, AboutUsSerializer, BaseInfoSerializer, PollSerializer,
    QuestionSerializer, PollResultSerializer, PollAnswerSerializer, TakePollSerializer, BannerSerializer
)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from drf_yasg.utils import swagger_auto_schema


class BannerViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Banners',
        operation_description='List of banners',
        responses={200: BannerSerializer(many=True)},
        tags=['Banner']
    )
    def banner_list(self, request):
        banners = Banner.objects.filter(is_published=True).order_by('-created_at')[:3]
        serializer = BannerSerializer(banners, many=True, context={'request': request})

        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

class FAQViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='FAQ',
        operation_description='Frequently Asked Questions',
        responses={200: FAQSerializer(many=True)},
        tags=['FAQ']
    )
    def faq_get(self, request):
        faqs = FAQ.objects.filter(is_visible=True)
        return Response(data={'result': FAQSerializer(faqs, many=True, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)


class AboutUsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='About Us',
        operation_description='Data About Us',
        responses={200: AboutUsSerializer()},
        tags=['About Us']
    )
    def about_us_get(self, request):
        data = AboutUs.objects.order_by('-created_at').first()
        return Response(
            data={'result': AboutUsSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class AdditionalLinksViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Additional Links',
        operation_description='Additional Links',
        responses={200: AdditionalLinksSerializer(many=True)},
        tags=['Additional Links']
    )
    def additional_links_get(self, request):
        links = AdditionalLinks.objects.filter(is_visible=True)
        return Response(
            data={'result': AdditionalLinksSerializer(links, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class BaseInfoViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Contact Us',
        operation_description='Contact Us',
        responses={200: BaseInfoSerializer()},
        tags=['Contact Us']
    )
    def base_info_get(self, request):
        data = BaseInfo.objects.order_by('-created_at').first()
        return Response(
            data={'result': BaseInfoSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class PollViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List of Polls',
        operation_description='List of polls',
        responses={200: PollSerializer(many=True)},
        tags=['Poll']
    )
    def get_polls(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Detail Poll',
        operation_description='Detail poll',
        responses={200: PollSerializer()},
        tags=['Poll']
    )
    def get_poll(self, request, pk):
        user = get_ip(request)
        poll = Poll.objects.filter(id=pk).first()
        if not poll:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        result = PollResult.objects.filter(poll_id=poll.id, user=user).first()
        if result:
            serializer = PollResultSerializer(result, context={'request': request})
            return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

        serializer = PollSerializer(poll, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=TakePollSerializer(),
        operation_summary='Take Poll',
        operation_description='Take poll',
        responses={200: PollResultSerializer()},
        tags=['Poll']
    )
    def take_poll(self, request):
        data = request.data
        user = get_ip(request)

        serializer = TakePollSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        poll = Poll.objects.filter(id=data.get('poll')).first()
        if not poll:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        result = PollResult.objects.filter(poll_id=poll.id, user=user).first()
        if result:
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT)

        result = PollResult.objects.create(user=user, poll=poll)
        result.save()

        answers = [{**answer, 'result': result.id} for answer in data['answers']]

        serializer = PollAnswerSerializer(data=answers, many=True, context={'request': request})
        if not serializer.is_valid():
            result.delete()
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message=serializer.errors)

        serializer.save()
        poll.participant_count += 1
        poll.save()

        return Response(data={'result': PollResultSerializer(result, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_201_CREATED)


class QuestionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Get Questions By Poll Id',
        operation_description='Get questions by poll id',
        responses={200: QuestionSerializer(many=True)},
        tags=['Question']
    )
    def get_questions(self, request):
        data = request.GET
        questions = Question.objects.filter(poll_id=data.get('poll'))
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Get One Question',
        operation_description='Get one question',
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def get_question(self, request, pk):
        question = Question.objects.filter(id=pk).first()
        if not question:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = QuestionSerializer(question, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Get Next Question',
        operation_description='Get next question',
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def get_next_question(self, request, pk):
        question = Question.objects.filter(id=pk).first()
        if not question:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        question = Question.objects.filter(id=question.id + 1, poll_id=question.poll_id).first()
        if not question:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = QuestionSerializer(question, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)
