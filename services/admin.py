from django.contrib import admin
from .models import Banner, Region, CommissionCategory, CommissionMember, Projects, AppealMember, Appeal, News, \
    PollQuestion, PollAnswer, Opinion


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description', 'image')
    list_display_links = ('id', 'short_description')


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
    list_display_links = ('id', 'name', 'type')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'status', 'file')
    list_display_links = ('id', 'name', 'short_description', 'status',)


@admin.register(AppealMember)
class AppealMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'commission_member', 'prone_number')
    list_display_links = ('id', 'name', 'commission_member', 'prone_number')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name', 'phone_number')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description', 'image')
    list_display_links = ('id', 'short_description', 'image')


@admin.register(PollQuestion)
class PollQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(PollAnswer)
class PollAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_true')
    list_display_links = ('id', 'is_true')


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name', 'phone_number')
