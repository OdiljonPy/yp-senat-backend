from datetime import date
from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .utils import get_ip

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .repository.get_posts_list import get_post_list
from .repository.get_project_filter import get_projects_filter
from .models import (Region, CommissionCategory,
                     CommissionMember, Projects,
                     Post, Visitors,
                     AppealStat, MandatCategory)
from .serializers import (
    RegionSerializer, CommissionMemberSerializer,
    ProjectsSerializer, CommissionCategorySerializer,
    AppealSerializer, ParamValidateSerializer,
    PostSerializer, PostFilterSerializer,
    AppealStatSerializer, MandatCategorySerializer
)


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
        manual_parameters=[openapi.Parameter(name='region_id', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                                             description='Region id')],
        operation_description='List of commission members by region id',
        responses={200: CommissionMemberSerializer(many=True)},
        tags=['Commission']
    )
    def commission_member_by_region(self, request):
        param = request.query_params.get('region_id')
        if param:
            if not str(param).isdigit():
                raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message='region id must be integer')

            commission_members = CommissionMember.objects.filter(region_id=param)
            return Response(
                data={'result': CommissionMemberSerializer(commission_members, many=True, context={'request': request}
                                                           ).data, 'ok': True}, status=status.HTTP_200_OK)

        commission_members = CommissionMember.objects.filter(type=1)
        serializer = CommissionMemberSerializer(commission_members, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='List Of Commission Categories',
        manual_parameters=[
            openapi.Parameter(name='category_id', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='Category id')
        ],
        operation_description='List of commission categories',
        responses={200: CommissionCategorySerializer(many=True)},
        tags=['Commission']
    )
    def commission_category_list(self, request):
        param = request.query_params.get('category_id')
        if param:
            if not str(param).isdigit():
                raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message='category id must be integer')

            members = CommissionMember.objects.filter(commission_category_id=param).select_related(
                'commission_category', 'region')
            serializer = CommissionMemberSerializer(members, many=True, context={'request': request})
            return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

        categories = CommissionCategory.objects.all()
        serializer = CommissionCategorySerializer(categories, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class ProjectViewSet(ViewSet):
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
        operation_summary='Create Appeal, need to give id to commission member if appeal for commission member',
        operation_description='Create appeal, need to give id to commission member if appeal for commission member',
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
        operation_summary='List of posts by commission members',
        operation_description="List of posts by commission members",
        manual_parameters=[
            openapi.Parameter(name='post_member_exist', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN,
                              description='post member exist'),
            openapi.Parameter(
                name='q', in_=openapi.IN_QUERY, description='Search q', type=openapi.TYPE_STRING),
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, description='Page', type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, description='Page size', type=openapi.TYPE_INTEGER),
        ],
        responses={200: PostSerializer(many=True)},
        tags=['Post']
    )
    def post_list_by_members(self, request):
        param = request.query_params
        serializer_params = PostFilterSerializer(data=param, context={'request': request})
        if not serializer_params.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer_params.errors)

        q = serializer_params.validated_data.get('q', '')
        post_member = serializer_params.validated_data.get('post_member_exist')

        filter_ = Q()
        if q:
            filter_ &= (Q(short_description__icontains=q) | Q(description__icontains=q))
        if post_member is True:
            filter_ &= (Q(commission_member__isnull=True, is_published=True))
        if post_member is False:
            filter_ &= (Q(commission_member__isnull=False, is_published=True))

        posts = Post.objects.filter(filter_).order_by('-created_at')
        response = get_post_list(context={'request': request, 'query': posts},
                                 page=serializer_params.data.get('page', 1),
                                 page_size=serializer_params.data.get('page_size', 10))

        return Response(data={'result': response, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Post detail',
        operation_description='Post detail',
        responses={200: PostSerializer()},
        tags=['Post']
    )
    def post_detail(self, request, pk=None):
        obj = Post.objects.filter(id=pk, is_published=True).first()
        current_time = date.today()

        if not obj:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        ip = get_ip(request)

        if Visitors.objects.filter(ip=ip, created_at__day=current_time.day, created_at__month=current_time.month,
                                   created_at__year=current_time.year).exists():
            obj.views.add(Visitors.objects.filter(ip=ip).first())

        else:
            ocj_create = Visitors.objects.create(ip=ip, name=request.META.get('HTTP_USER_AGENT', ''))
            obj.views.add(ocj_create)

        serializer = PostSerializer(obj, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class VisitorsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Visitors',
        operation_description='Visitors',
        tags=['Visitors'])
    def get(self, request):
        return Response(data={'result': Visitors.objects.all().count(), 'ok': True}, status=status.HTTP_200_OK)


class MandatCategoryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Mandat Category',
        operation_description='Mandat Category',
        manual_parameters=[
            openapi.Parameter(name='mandat_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Mandat id')
        ],
        tags=['Mandat'])
    def get(self, request):
        param = request.query_params.get('mandat_id', None)

        filter_ = Q()

        if param and param.isdigit():
            filter_ &= Q(id=param)

        members = MandatCategory.objects.filter(filter_).order_by('created_at')
        serializer = MandatCategorySerializer(members, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class AppealStatViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Get statistics of appeals',
        operation_description='Get statistics of appeals',
        responses={200: AppealStatSerializer()},
        tags=['AppealStat']
    )
    def stats(self, request):
        stats = AppealStat.objects.order_by('-created_at').first()
        return Response(data={'result': AppealStatSerializer(stats, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)
