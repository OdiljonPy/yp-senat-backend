from django.contrib import admin
from .models import (Region, CommissionCategory,
                     CommissionMember, Projects,
                     Appeal, Post, PostCategory,
                     Visitors, MandatCategory,
                     AppealStat, Video)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CommissionMemberTabularInline(admin.TabularInline):
    model = CommissionMember
    extra = 0


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('region',)
    inlines = [CommissionMemberTabularInline]


@admin.register(CommissionCategory)
class CommissionCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(CommissionMember)
class CommissionMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'type')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'description')
    list_filter = ('type',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'short_description', 'description')
    list_filter = ('status', 'is_published')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'commission_member', 'phone_number', 'is_resolved')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'phone_number', 'email')
    list_filter = ('is_resolved',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'view_count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'short_description')
    list_filter = ('is_published',)

    def view_count(self, obj):
        return obj.views.count()

    view_count.short_description = 'Количество просмотров'


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'created_at')
    list_display_links = ('id', 'ip', 'name')


@admin.register(MandatCategory)
class MandatCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)


@admin.register(AppealStat)
class AppealStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'incoming_appeals', 'resolved_appeals', 'explained_appeals', 'rejected_appeals')


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
