from django.contrib import admin
from .models import FAQ, AboutUs, AdditionalLinks, ContactUs


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_display_links = ('id', 'question', 'answer')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')


@admin.register(AdditionalLinks)
class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description', 'link', 'image')
    list_display_links = ('id', 'short_description', 'link', 'image')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email')
    list_display_links = ('id', 'phone_number', 'email')
