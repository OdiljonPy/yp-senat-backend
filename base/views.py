from .models import FAQ, AboutUs, AdditionalLinks, ContactUs
from .serializers import FAQSerializer, AdditionalLinksSerializer, AboutUsSerializer, ContactUsSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from exceptions import error_messages, exception
from drf_yasg.utils import swagger_auto_schema


class FAQViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='FAQ',
        operation_description='Frequently Asked Questions',
        responses={200: FAQSerializer()},
        tags=['FAQ']
    )
    def faq_get(self, request):
        faqs = FAQ.objects.all()
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
        data = AboutUs.objects.all()
        return Response(
            data={'result': AboutUsSerializer(data, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)


class AdditionalLinksViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Additional Links',
        operation_description='Additional Links',
        responses={200: AdditionalLinksSerializer()},
        tags=['Additional Links']
    )
    def additional_links_get(self, request):
        links = AdditionalLinks.objects.all()
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
        data = ContactUs.objects.all()
        return Response(
            data={'result': ContactUsSerializer(data, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)
