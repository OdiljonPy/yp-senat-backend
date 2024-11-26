from django.contrib import admin
from .models import FAQ, AboutUs, AdditionalLinks, BaseInfo, Banner, Poll

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('title',)
    list_filter = ('is_published',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('answer', 'question')
    list_filter = ('is_visible',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('description',)


@admin.register(AdditionalLinks)
class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('title',)
    list_filter = ('is_visible',)


@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email')
    list_display_links = ('id', 'phone_number')
    search_fields = ('phone_number', 'email', 'address')

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
