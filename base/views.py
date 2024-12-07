from datetime import datetime
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from services.models import PROJECT_STATUS
from .models import FAQ, AboutUs, AdditionalLinks, BaseInfo, Poll
from .repository.poll_paginator import get_poll_list
from .serializers import (
    FAQSerializer, AdditionalLinksSerializer,
    AboutUsSerializer, BaseInfoSerializer,
    PollSerializer, PollParamSerializer
)


class FAQViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='FAQ',
        operation_description='Frequently Asked Questions',
        responses={200: FAQSerializer(many=True)},
        tags=['Base']
    )
    def faq_get(self, request):
        faqs = FAQ.objects.filter(is_visible=True)
        return Response(data={'result': FAQSerializer(faqs, many=True, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)


class AboutUsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='About Us',
        operation_description='About Us',
        responses={200: AboutUsSerializer()},
        tags=['Base']
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
        tags=['Base']
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
        tags=['Base']
    )
    def base_info_get(self, request):
        data = BaseInfo.objects.order_by('-created_at').first()
        return Response(
            data={'result': BaseInfoSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class PollViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Poll',
        operation_description='Poll',
        manual_parameters=[
            openapi.Parameter(name="page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter(name="page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter(name='poll_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Poll Name'),
            openapi.Parameter(name='poll_status', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='Poll Status, receive 1-active or 2-finished'),
        ],
        responses={200: PollSerializer()},
        tags=['Base']
    )
    def poll(self, request):
        from .google_sheets import get_google_sheet_data
        from .utils import process_poll_data, is_valid_sheet_data, validate_and_extract_sheet_id

        param_serializer = PollParamSerializer(data=request.query_params, context={"request": request})
        if not param_serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=param_serializer.errors)

        param = param_serializer.validated_data.get('poll_name')
        status_ = param_serializer.validated_data.get('poll_status')
        filter_ = Q()
        if param:
            filter_ &= Q(name__icontains=param)
        if status_:
            filter_ &= Q(status=status_)

        Poll.objects.filter(ended_at__lt=datetime.now().date()).update(status=2)



        polls = Poll.objects.filter(filter_).order_by('-created_at')

        for poll in polls:
            print(poll)

            if poll.status == 1 and poll.ended_at:
                continue
            sheet_id = validate_and_extract_sheet_id(poll.sheet_url)
            if not sheet_id:
                print(f"Invalid sheet URL for poll {poll.id}")
                continue


            sheet_data = get_google_sheet_data(sheet_id)
            if not is_valid_sheet_data(sheet_data):
                print(f"Invalid or empty data for poll {poll.id}")
                continue

            formatted_result = process_poll_data(sheet_data)
            poll.result_en = formatted_result
            poll.result_uz = formatted_result
            poll.result_ru = formatted_result
            poll.save()


        return Response(
            data={'result': get_poll_list(context={"request": request}, request_data=polls,
                                          page=param_serializer.validated_data.get('page'),
                                          page_size=param_serializer.validated_data.get('page_size')),'ok': True},
            status=status.HTTP_200_OK)
