from drf_yasg import openapi
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Banner, Region, CommissionCategory, CommissionMember, Projects, AppealMember, Appeal, Post, Opinion
from .serializers import (
    BannerSerializer, RegionSerializer, CommissionMemberSerializer, ProjectsSerializer, CommissionCategorySerializer,
    AppealSerializer, AppealMemberSerializer, NewsSerializer, OpinionSerializer, FilterSerializer
)


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
        news = Post.objects.all()
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


class ViewsCountViewSet(ViewSet):
    # @swagger_auto_schema(
    #     operation_summary='count news',
    #     operation_description='count news',
    #     tags=['Commission']
    # )
    # def count_views(self, request, pk=None):
    #     obj = News.objects.filter(id=pk).first()
    #     if obj:
    #         obj.counts_view()
    #         serializer = NewsSerializer(obj)
    #         return Response(data={'data': serializer.data, 'ok': False}, status=status.HTTP_200_OK)
    #     raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

    @swagger_auto_schema(
        operation_summary='count news',
        operation_description='count news',
        tags=['Views count']
    )
    def count_views(self, request, pk=None):
        obj = Post.objects.filter(id=pk).first()
        user_ip = request.META.get('REMOTE_ADDR')
        print(request.COOKIES)

        viewed_news = request.COOKIES.get('viewed_news', '')
        print('first', viewed_news)
        if viewed_news:
            viewed_news = viewed_news.split(',')
        else:
            viewed_news = []

        print(viewed_news)

        if f"{obj.id}-{user_ip}" not in viewed_news:
            obj.views_count += 1
            obj.save()
            viewed_news.append(f"{obj.id}-{user_ip}")
        serializer = NewsSerializer(obj)
        response = Response(serializer.data)
        response.set_cookie('viewed_articles', ','.join(viewed_news), max_age=3600 * 24 * 30)  # 30 days

        return response


class FilteringViewSet(ViewSet):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='q', in_=openapi.IN_QUERY, description='Search q', type=openapi.TYPE_STRING),
        ],
        operation_summary='News filter ',
        operation_description="News filter",
        responses={200: NewsSerializer()},
        tags=['News'])
    def filtering_by_news(self, request):
        serializer_params = FilterSerializer(data=request.query_params.copy(), context={'request': request})
        if not serializer_params.is_valid():
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        q = serializer_params.validated_data.get('q', '')
        filter_ = Q()
        if q:
            filter_ &= (Q(short_description__icontains=q) | Q(description__icontains=q))

        news = Post.objects.filter(filter_).order_by('-created_at')

        return Response(data={'data': NewsSerializer(news, many=True, context={'request': request}).data})
