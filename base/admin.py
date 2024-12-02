from django.contrib import admin
from .models import (FAQ, AboutUs,
                     AdditionalLinks, BaseInfo,
                     Poll, AboutUsImage)

@admin.register(AboutUsImage)
class AboutUsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_us')
    list_display_links = ('id', 'about_us')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('answer', 'question')
    list_filter = ('is_visible',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('description', 'short_description')


@admin.register(AdditionalLinks)
class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_visible')
    search_fields = ('title',)
    list_filter = ('is_visible',)


@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email')
    list_display_links = ('id', 'phone_number')
    search_fields = ('phone_number', 'email', 'address')


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'started_at', 'ended_at', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('status',)
