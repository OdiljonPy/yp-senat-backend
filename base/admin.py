from django.contrib import admin
from .models import FAQ, AboutUs, AdditionalLinks, ContactUs, Poll, Question, Option, PollResult, PollAnswer


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(AdditionalLinks)
class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email')
    list_display_links = ('id',)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll', 'type')
    list_display_links = ('id', 'poll')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')
    list_display_links = ('id', 'question')


class PollAnswerTabularInline(admin.TabularInline):
    model = PollAnswer
    extra = 0


@admin.register(PollResult)
class PollResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'poll')
    list_display_links = ('id', 'user')
    inlines = [PollAnswerTabularInline]
