from django.urls import path

from .views import (
    RegionViewSet, CommissionViewSet,
    ProjectViewSet, AppealViewSet,
    PostViewSet, VisitorsViewSet,
    AppealStatViewSet, MandatCategoryViewSet, VideoViewSet, CategoryViewSet
)

urlpatterns = [
    path('region/', RegionViewSet.as_view({'get': 'region_list'}), name='region'),
    path('projects/', ProjectViewSet.as_view({'get': 'filter_by_query_param'}), name='projects'),
    path('post/member/', PostViewSet.as_view({'get': 'post_list_by_members'}), name='post_by_member'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': "post_detail"}), name='post_detail'),
    path('post/category/', PostViewSet.as_view({'get': 'post_list_by_category'}), name='posts_by_category_id'),
    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name='category_list'),
    path('banner/', PostViewSet.as_view({'get': 'banner'}), name='banner'),

    path('commission/<int:pk>/', CommissionViewSet.as_view({'get': 'commission_member_detail'}),
         name='commission_detail'),
    path('region/commissions/', CommissionViewSet.as_view({'get': 'commission_member_by_region'}),
         name='region_commission'),
    path('commission/category/', CommissionViewSet.as_view({'get': 'commission_category_list'}),
         name='commission_category'),
    path('commission/images/<int:pk>/', CommissionViewSet.as_view({'get': 'image_list'}), name='images_of_category'),

    path('management/', CommissionViewSet.as_view({'get': 'management_members'}), name='management_members'),
    path('appeal/', AppealViewSet.as_view({'post': 'create_appeal'}), name='appeal'),
    path('visitors/', VisitorsViewSet.as_view({'get': 'get'}), name='visitors'),
    path('statistics/', AppealStatViewSet.as_view({'get': 'stats'}), name='appeal_stat'),
    path('mandat/', MandatCategoryViewSet.as_view({'get': 'get'}), name='mandat_category'),
    path('video/', VideoViewSet.as_view({'get': 'video_list'}), name='videos_list')
]
