from modeltranslation.translator import translator, TranslationOptions
from .models import (AboutUs, AdditionalLinks,
                     FAQ, Poll,
                     BaseInfo)


class AboutUsTranslationOption(TranslationOptions):
    fields = ("short_description", 'description',)


class AdditionalLinksTranslationOptions(TranslationOptions):
    fields = ('title',)


class FAQTranslationOption(TranslationOptions):
    fields = ('question', 'answer')


class BaseInfoTranslationOption(TranslationOptions):
    fields = ('address',)


class PollTranslationOption(TranslationOptions):
    fields = ('name', 'result')


translator.register(AboutUs, AboutUsTranslationOption)
translator.register(AdditionalLinks, AdditionalLinksTranslationOptions)
translator.register(FAQ, FAQTranslationOption)
translator.register(BaseInfo, BaseInfoTranslationOption)
translator.register(Poll, PollTranslationOption)
