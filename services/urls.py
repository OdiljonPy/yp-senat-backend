from django.urls import path

from .views import (
    BannerViewSet, RegionViewSet, CommissionViewSet, ProjectViewSet, AppealViewSet, PostViewSet,
    ViewsCountViewSet, SearchingViewSet
)

urlpatterns = [
    path('banner/', BannerViewSet.as_view({'get': 'banner_list'}), name='banner'),
    path('region/', RegionViewSet.as_view({'get': 'region_list'}), name='region'),
    path('project/', ProjectViewSet.as_view({'get': 'projects_list'}), name='project'),
    path('projects/', ProjectViewSet.as_view({'get': 'filter_by_query_param'}), name='projects'),
    path('post/', PostViewSet.as_view({'get': 'post_list'}), name='news'),

    path('commission/', CommissionViewSet.as_view({'get': 'commission_member_list'}), name='commission_list'),
    path('commission/<int:pk>/', CommissionViewSet.as_view({'get': 'commission_member_detail'}),
         name='commission_detail'),
    path('region/commissions/<int:pk>/', CommissionViewSet.as_view({'get': 'commission_member_by_region'}),
         name='region_commission'),
    path('category/commission/<int:pk>/', CommissionViewSet.as_view({'get': 'commission_members_by_category'}),
         name='commission_member_by_category_id'),
    path('commission/category/', CommissionViewSet.as_view({'get': 'commission_category_list'}),
         name='commission_category'),

    path('appeal/', AppealViewSet.as_view({'post': 'create_appeal'}), name='appeal'),
    path('view/<int:pk>/', ViewsCountViewSet.as_view({'get': 'count_views'}), name='count_views'),
    path('filtering/', SearchingViewSet.as_view({'get': 'search_by_post'}), name='search_by_post')
]
