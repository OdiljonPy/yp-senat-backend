from django.contrib import admin
from .models import Banner, Region, CommissionCategory, CommissionMember, Projects, AppealMember, Appeal, News, Opinion


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CommissionCategory)
class CommissionCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CommissionMember)
class CommissionMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_display_links = ('id', 'name')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')


@admin.register(AppealMember)
class AppealMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('id', 'name')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name')
