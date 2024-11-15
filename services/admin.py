from django.contrib import admin

from .models import Region, CommissionCategory, CommissionMember, Projects, Appeal, Post, Visitors


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
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'short_description')
    list_filter = ('is_published',)


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'created_at')
    list_display_links = ('id', 'ip', 'name')
