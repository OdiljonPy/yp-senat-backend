from datetime import date

from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import (Banner, Region, CommissionCategory,
                     CommissionMember, Projects, Post, Visitors)
from .repository.get_posts_list import get_post_list
from .repository.get_project_filter import get_projects_filter
from .serializers import (
    BannerSerializer, RegionSerializer, CommissionMemberSerializer, ProjectsSerializer, CommissionCategorySerializer,
    AppealSerializer, ParamValidateSerializer, PostSerializer, PostFilterSerializer
)
from .utils import get_ip


class BannerViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Banners',
        operation_description='List of banners',
        responses={200: BannerSerializer(many=True)},
        tags=['Banner']
    )
    def banner_list(self, request):
        banners = Banner.objects.filter(is_published=True)
        serializer = BannerSerializer(banners, many=True, context={'request': request})

        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class RegionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Regions',
        operation_description='List of regions',
        responses={200: RegionSerializer(many=True)},
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
        responses={200: CommissionMemberSerializer(many=True)},
        tags=['Commission']
    )
    def commission_member_list(self, request):
        members = CommissionMember.objects.all()
        serializer = CommissionMemberSerializer(members, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='List Of Commission Members By Category ID',
        operation_description='List of commission members by category id',
        responses={200: CommissionMemberSerializer(many=True)},
        tags=['Commission']
    )
    def commission_members_by_category(self, request, pk):
        members = CommissionMember.objects.filter(commission_category_id=pk)
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
        operation_summary='Commission members by region id',
        operation_description='List of commission members by region id',
        responses={200: CommissionMemberSerializer(many=True)},
        tags=['Commission']
    )
    def commission_member_by_region(self, request, pk):
        commission_members = CommissionMember.objects.filter(region_id=pk)
        return Response(
            data={'result': CommissionMemberSerializer(commission_members, many=True, context={'request': request}
                                                       ).data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='List Of Commission Categories',
        operation_description='List of commission categories',
        responses={200: CommissionCategorySerializer(many=True)},
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
        responses={200: ProjectsSerializer(many=True)},
        tags=['Project']
    )
    def projects_list(self, request):
        projects = Projects.objects.filter(is_published=True)
        serializer = ProjectsSerializer(projects, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, description='Page number', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, description='Page size', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='status', in_=openapi.IN_QUERY, description='Status', type=openapi.TYPE_INTEGER)
        ],
        operation_summary='List of projects by type',
        operation_description='List of projects by type',
        responses={200: ProjectsSerializer(many=True)},
        tags=['Project']
    )
    def filter_by_query_param(self, request):
        serializer = ParamValidateSerializer(data=request.query_params, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, serializer.errors)
        status_ = serializer.validated_data.get('status')
        page_size = serializer.validated_data.get('page_size')
        page = serializer.validated_data.get('page')
        query = Q()
        if status_:
            query &= Q(status=status_)
        projects = Projects.objects.filter(query, is_published=True).order_by('id')
        response = get_projects_filter(
            context={'request': request, 'project_param': projects}, page=page, page_size=page_size)
        return Response(data={'result': response, 'ok': True}, status=status.HTTP_200_OK)


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
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)


class PostViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='List Of Posts',
        operation_description='List of Posts',
        responses={200: PostSerializer(many=True)},
        tags=['Post']
    )
    def post_list(self, request):
        posts = Post.objects.filter(commission_member__is_null=True)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='List of posts by commission members',
        operation_description="List of posts by commission members",
        responses={200: PostSerializer(many=True)},
        tags=['Post']
    )
    def post_list_by_members(self, request):
        posts = Post.objects.filter(commission_member__is_null=False)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Post detail',
        operation_description='Post detail',
        tags=['Post']
    )
    def post_detail(self, request, pk=None):
        obj = Post.objects.filter(id=pk, is_published=True).first()
        current_time = date.today()

        if not obj:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        ip = get_ip(request)
        name = request.META.get('HTTP_USER_AGENT', '')

        if Visitors.objects.filter(ip=ip, created_at__day=current_time.day, created_at__month=current_time.month,
                                   created_at__year=current_time.year).exists():
            obj.views.add(Visitors.objects.filter(ip=ip).first())
        else:
            Visitors.objects.create(ip=ip, name=name)
            obj.views.add(
                Visitors.objects.filter(ip=ip, created_at__day=current_time.day, created_at__month=current_time.month,
                                        created_at__year=current_time.year).first())

        serializer = PostSerializer(obj, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class SearchingViewSet(ViewSet):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='q', in_=openapi.IN_QUERY, description='Search q', type=openapi.TYPE_STRING),
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, description='Page', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, description='Page size', type=openapi.TYPE_INTEGER),
        ],
        operation_summary='Posts filter ',
        operation_description="Posts filter",
        responses={200: PostSerializer()},
        tags=['Post'])
    def search_by_post(self, request):
        serializer_params = PostFilterSerializer(data=request.query_params.copy(), context={'request': request})
        if not serializer_params.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer_params.errors)
        q = serializer_params.validated_data.get('q', '')
        filter_ = Q()
        if q:
            filter_ &= (Q(short_description__icontains=q) | Q(description__icontains=q))

        posts = Post.objects.filter(filter_).order_by('-created_at')
        response = get_post_list(context={'request': request, 'query': posts},
                                 page=serializer_params.data.get('page', 1),
                                 page_size=serializer_params.data.get('page_size', 10))

        return Response(data={'result': response, 'ok': True}, status=status.HTTP_200_OK)


class VisitorsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Visitors',
        operation_description='Visitors',
        tags=['Visitors'])
    def get(self, request):
        return Response(data={'result': Visitors.objects.all().count()}, status=status.HTTP_200_OK)
