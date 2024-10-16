from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Banner, Region, CommissionCategory, CommissionMember, Projects, AppealMember, Appeal, News, Opinion
from .serializers import BannerSerializer, RegionSerializer, CommissionMemberSerializer, ProjectsSerializer, \
    CommissionCategorySerializer, AppealSerializer, AppealMemberSerializer, NewsSerializer, OpinionSerializer


class BannerViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Banners',
        operation_description='List of banners',
        responses={200: BannerSerializer()},
        tags=['Banner']
    )
    def banner_list(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class RegionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Regions',
        operation_description='List of regions',
        responses={200: RegionSerializer()},
        tags=['Region']
    )
    def region_list(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class CommissionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Commission Members',
        operation_description='List of commission members',
        responses={200: CommissionMemberSerializer()},
        tags=['Commission']
    )
    def commission_member_list(self, request):
        members = CommissionMember.objects.all()
        serializer = CommissionMemberSerializer(members, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Detail Of Commission Member',
        operation_description='Detail of commission member',
        responses={200: CommissionMemberSerializer()},
        tags=['Commission']
    )
    def commission_member_detail(self, request, pk):
        member = CommissionMember.objects.filter(id=pk).first()
        if not member:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)
        serializer = CommissionMemberSerializer(member, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='List Of Commission Categories',
        operation_description='List of commission categories',
        responses={200: CommissionCategorySerializer()},
        tags=['Commission']
    )
    def commission_category_list(self, request):
        categories = CommissionCategory.objects.all()
        serializer = CommissionCategorySerializer(categories, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class ProjectViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Projects',
        operation_description='List of projects',
        responses={200: ProjectsSerializer()},
        tags=['Project']
    )
    def projects_list(self, request):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class AppealViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=AppealSerializer(),
        operation_summary='Create Appeal',
        operation_description='Create appeal',
        responses={201: AppealSerializer()},
        tags=['Appeal']
    )
    def create_appeal(self, request):
        data = request.data
        serializer = AppealSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=AppealMemberSerializer(),
        operation_summary='Create Appeal Member',
        operation_description='Create appeal member',
        responses={201: AppealMemberSerializer()},
        tags=['Appeal']
    )
    def create_appeal_member(self, request):
        data = request.data
        serializer = AppealMemberSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)


class NewsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of News',
        operation_description='List of news',
        responses={200: NewsSerializer()},
        tags=['News']
    )
    def news_list(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class OpinionViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=OpinionSerializer(),
        operation_summary='Create Opinion',
        operation_description='Create opinion',
        responses={201: OpinionSerializer()},
        tags=['Opinion']
    )
    def create_opinion(self, request):
        data = request.data
        serializer = OpinionSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)
