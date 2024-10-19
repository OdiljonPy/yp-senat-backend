from datetime import timedelta, datetime, date
from django.utils import timezone
from .models import FAQ, AboutUs, AdditionalLinks, ContactUs, Poll, Question, Option, PollResult, PollAnswer, VisitorActivity
from .serializers import (
    FAQSerializer, AdditionalLinksSerializer, AboutUsSerializer, ContactUsSerializer, PollSerializer,
    QuestionSerializer, OptionSerializer, PollResultSerializer, PollAnswerSerializer, VisitorActivitySerializer
)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from drf_yasg.utils import swagger_auto_schema


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


class ContactUsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Contact Us',
        operation_description='Contact Us',
        responses={200: ContactUsSerializer()},
        tags=['Contact Us']
    )
    def contact_us_get(self, request):
        data = ContactUs.objects.order_by('-created_at').first()
        return Response(
            data={'result': ContactUsSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class PollViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Polls',
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
    def get_poll_detail(self, request, pk):
        poll = Poll.objects.filter(id=pk).first()
        if not poll:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = PollSerializer(poll, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

class VisitorActivityViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Visitor Activity',
        operation_description='Visitor Activity',
        responses={200: VisitorActivitySerializer()},
        tags = ['Visitors']
    )
    def get_visitor_activity(self, request):
        start_date = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
        start_date_aware = timezone.make_aware(start_date)

        monthly_visitors = VisitorActivity.objects.filter(
            created_at__gte=start_date_aware,
            created_at__lt=timezone.now()
        )
        return Response(
            data={'result': VisitorActivitySerializer(monthly_visitors, many=True).data, 'visitors_count':monthly_visitors.count(), 'ok': True}, status=status.HTTP_200_OK
        )