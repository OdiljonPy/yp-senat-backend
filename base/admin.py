from django.contrib import admin
from .models import FAQ, AboutUs, AdditionalLinks, BaseInfo, Banner, Poll, Question, Option, PollResult, PollAnswer

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
    search_fields = ('title', 'description')


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
    list_display = ('id', 'title', 'participant_count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll', 'type')
    list_display_links = ('id', 'poll')
    search_fields = ('text',)
    list_filter = ('type',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')
    search_fields = ('question', 'text')


class PollAnswerTabularInline(admin.TabularInline):
    model = PollAnswer
    extra = 0


@admin.register(PollResult)
class PollResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'poll')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('poll',)
    inlines = [PollAnswerTabularInline]
