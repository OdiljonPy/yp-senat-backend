from django.urls import path
from .views import (
    RegionViewSet, CommissionViewSet, ProjectViewSet, AppealViewSet,
    PostViewSet, AppealStatViewSet, MandatCategoryViewSet, VideoViewSet,
    ManagementViewSet, NormativeDocumentsViewSet
)

urlpatterns = [
    path('region/', RegionViewSet.as_view({'get': 'region_list'}), name='region'),
    path('projects/', ProjectViewSet.as_view({'get': 'filter_by_query_param'}), name='projects'),
    path('project/<int:pk>/', ProjectViewSet.as_view({'get': 'project_detail'}), name='project_detail'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': "post_detail"}), name='post_detail'),
    path('posts/', PostViewSet.as_view({'get': 'post_list_by_category'}), name='posts_by_category_id'),
    path('categories/', PostViewSet.as_view({'get': 'list'}), name='category_list'),
    path('banner/', PostViewSet.as_view({'get': 'banner'}), name='banner'),

    path('commission/', CommissionViewSet.as_view({'get': 'commission_list'}), name='commission_list'),
    path('commission/category/', CommissionViewSet.as_view({'get': 'commission_category_list'}),
         name='commission_category'),
    path('commission/category/<int:pk>/', CommissionViewSet.as_view({'get': "commission_category_detail"}),
         name='commission_category_detail'),
    path('management/', ManagementViewSet.as_view({'get': 'management_list'}), name='management_members'),
    path('appeal/', AppealViewSet.as_view({'post': 'create_appeal'}), name='appeal'),
    path('statistics/', AppealStatViewSet.as_view({'get': 'stats'}), name='appeal_stat'),
    path('mandat/', MandatCategoryViewSet.as_view({'get': 'mandat_list'}), name='mandat_list'),
    path('mandat/<int:pk>/', MandatCategoryViewSet.as_view({'get': "mandat_detail"}), name="mandat_detail"),
    path('video/', VideoViewSet.as_view({'get': 'video_list'}), name='videos_list'),
    path('documents/', NormativeDocumentsViewSet.as_view({'get': 'list'}), name='list_documents'),
]
