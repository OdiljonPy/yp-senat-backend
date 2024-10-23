from django.urls import path
from .views import FAQViewSet, AboutUsViewSet, AdditionalLinksViewSet, BaseInfoViewSet, PollViewSet, QuestionViewSet, \
    BannerViewSet

urlpatterns = [
    path('banner/', BannerViewSet.as_view({'get': 'banner_list'}), name='banner'),
    path('faq/', FAQViewSet.as_view({'get': 'faq_get'}), name='faq'),
    path('about/', AboutUsViewSet.as_view({'get': 'about_us_get'}), name='about_us'),
    path('additional/', AdditionalLinksViewSet.as_view({'get': 'additional_links_get'}), name='additional_links'),
    path('contact/', BaseInfoViewSet.as_view({'get': 'base_info_get'}), name='base_info_us'),

    # poll
    path('polls/', PollViewSet.as_view({'get': 'get_polls'}), name='polls'),
    path('polls/<int:pk>/', PollViewSet.as_view({'get': 'get_poll'}), name='poll'),
    path('polls/take/', PollViewSet.as_view({'post': 'take_poll'}), name='take_poll'),
    path('polls/question/next/<int:pk>/', QuestionViewSet.as_view({'get': 'get_next_question'}), name='next_question'),
]
