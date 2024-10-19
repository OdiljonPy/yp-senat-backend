from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import (Banner, Region, CommissionCategory,
                     CommissionMember, Projects, Post)
from .repository.get_posts_list import get_post_list
from .repository.get_project_filter import get_projects_filter
from .serializers import (
    BannerSerializer, RegionSerializer, CommissionMemberSerializer, ProjectsSerializer, CommissionCategorySerializer,
    AppealSerializer, ParamValidateSerializer, PostSerializer, PostFilterSerializer
)
from django.db.models import Count
# from .utils import get_ip


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
        responses={200: PostSerializer()},
        tags=['Post']
    )
    def post_list(self, request):
        posts = Post.objects.all().annotate(view_count=Count('visitor_activity'))
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Post detail",
        operation_description="Post detail",
        responses={200: PostSerializer()},
        tags=['Post']
    )
    def post_detail(self, request, pk):
        post = Post.objects.annotate(view_count=Count('visitor_activity')).filter(id=pk).first()
        if not post:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = PostSerializer(post, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


# class ViewsCountViewSet(ViewSet):
#     @swagger_auto_schema(
#         operation_summary='count posts',
#         operation_description='count posts',
#         tags=['Views count']
#     )
#     def count_views(self, request, pk=None):
#         obj = Post.objects.filter(id=pk).first()
#         user_ip = request.META.get('REMOTE_ADDR')
#         if not obj:
#             raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)
#
#         viewed_posts = request.COOKIES.get('viewed_posts', '')
#         if viewed_posts:
#             viewed_posts = viewed_posts.split(',')
#         else:
#             viewed_posts = []
#
#         if f"{obj.id}-{user_ip}" not in viewed_posts:
#             obj.views_count += 1
#             obj.save()
#             viewed_posts.append(f"{obj.id}-{user_ip}")
#         serializer = PostSerializer(obj)
#         response = Response(serializer.data)
#         response.set_cookie('viewed_articles', ','.join(viewed_posts), max_age=3600 * 24 * 30)  # 30 days
#
#         return response


class FilteringViewSet(ViewSet):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='q', in_=openapi.IN_QUERY, description='Search q', type=openapi.TYPE_STRING),
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, description='Page', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, description='Page size', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='member', in_=openapi.IN_QUERY, description='Page size', type=openapi.TYPE_INTEGER),

        ],
        operation_summary='Posts filter ',
        operation_description="Posts filter",
        responses={200: PostSerializer()},
        tags=['Post'])
    def filtering_by_post(self, request):
        serializer_params = PostFilterSerializer(data=request.query_params.copy(), context={'request': request})
        if not serializer_params.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer_params.errors)
        member = serializer_params.validated_data.get('member', '')
        q = serializer_params.validated_data.get('q', '')
        filter_ = Q()
        if q:
            filter_ &= (Q(short_description__icontains=q) | Q(description__icontains=q))

        if 'member' in serializer_params.data:
            filter_ &= Q(commission_member=member)

        posts = Post.objects.filter(filter_).order_by('-created_at')
        response = get_post_list(context={'request': request, 'query': posts},
                                 page=serializer_params.data.get('page', 1),
                                 page_size=serializer_params.data.get('page_size', 10))

        return Response(data={'result': response, 'ok': True}, status=status.HTTP_200_OK)


