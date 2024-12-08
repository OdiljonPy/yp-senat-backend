from django.urls import path
from .views import (FAQViewSet, AboutUsViewSet,
                    AdditionalLinksViewSet, BaseInfoViewSet,
                    PollViewSet)

urlpatterns = [
    path('faq/', FAQViewSet.as_view({'get': 'faq_get'}), name='faq'),
    path('about/', AboutUsViewSet.as_view({'get': 'about_us_get'}), name='about_us'),
    path('additional/', AdditionalLinksViewSet.as_view({'get': 'additional_links_get'}), name='additional_links'),
    path('contact/', BaseInfoViewSet.as_view({'get': 'base_info_get'}), name='base_info_us'),
    path('poll/', PollViewSet.as_view({'get': 'poll'}))
]
