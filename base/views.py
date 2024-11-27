from datetime import timezone, datetime

from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import FAQ, AboutUs, AdditionalLinks, BaseInfo, Banner, Poll
from .serializers import (
    FAQSerializer, AdditionalLinksSerializer,
    AboutUsSerializer, BaseInfoSerializer,
    BannerSerializer, PollSerializer
)


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
        operation_summary='Poll',
        operation_description='Poll',
        manual_parameters=[
            openapi.Parameter(name='poll_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Poll Name'),
            openapi.Parameter(name='poll_status', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN,
                              description='Poll Status'),
        ],
        responses={200: PollSerializer()},
        tags=['Poll']
    )
    def poll(self, request):

        param = request.query_params.get('poll_name', None)
        status_ = request.query_params.get('poll_status', '')

        filter_ = Q()
        if param:
            filter_ &= Q(name__icontains=param)
        if status_.lower() == 'true':
            filter_ &= Q(status=1)
        if status_.lower() == 'false':
            filter_ &= Q(status=2)

        polls = Poll.objects.filter(filter_).order_by('-created_at')

        Poll.objects.filter(ended_at__lt=datetime.now().date()).update(status=2)

        return Response(data={'result': PollSerializer(polls, many=True).data, 'ok': True}, )
