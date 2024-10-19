from django.urls import path
from .views import FAQViewSet, AboutUsViewSet, AdditionalLinksViewSet, ContactUsViewSet, VisitorActivityViewSet

urlpatterns = [
    path('faq/', FAQViewSet.as_view({'get': 'faq_get'}), name='faq'),
    path('about/', AboutUsViewSet.as_view({'get': 'about_us_get'}), name='about_us'),
    path('additional/', AdditionalLinksViewSet.as_view({'get': 'additional_links_get'}), name='additional_links'),
    path('contact/', ContactUsViewSet.as_view({'get': 'contact_us_get'}), name='contact_us'),
    path('viewcount/', VisitorActivityViewSet.as_view({'get': 'get_visitor_activity'}), name='view_count'),
]
