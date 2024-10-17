from django.urls import path
from .views import (
    BannerViewSet, RegionViewSet, CommissionViewSet, ProjectViewSet, AppealViewSet, NewsViewSet, OpinionViewSet,
    ViewsCountViewSet, FilteringViewSet
)

urlpatterns = [
    path('banner/', BannerViewSet.as_view({'get': 'banner_list'}), name='banner'),
    path('region/', RegionViewSet.as_view({'get': 'region_list'}), name='region'),
    path('project/', ProjectViewSet.as_view({'get': 'projects_list'}), name='project'),
    path('news/', NewsViewSet.as_view({'get': 'news_list'}), name='news'),
    path('opinion/', OpinionViewSet.as_view({'post': 'create_opinion'}), name='opinion'),

    path('commission/', CommissionViewSet.as_view({'get': 'commission_member_list'}), name='commission_list'),
    path('commission/<int:pk>/', CommissionViewSet.as_view({'get': 'commission_member_detail'}),
         name='commission_detail'),
    path('commission/category/', CommissionViewSet.as_view({'get': 'commission_category_list'}),
         name='commission_category'),

    path('appeal/', AppealViewSet.as_view({'post': 'create_appeal'}), name='appeal'),
    path('appeal/member/', AppealViewSet.as_view({'post': 'create_appeal_member'}), name='appeal_member'),
    path('view/<int:pk>/', ViewsCountViewSet.as_view({'get': 'count_views'}), name='count_views'),
    path('filtering/', FilteringViewSet.as_view({'get': 'filtering_by_news'}), name='filtering_by_news')
]
