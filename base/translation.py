from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, AdditionalLinks, FAQ, Poll, Question, Option, BaseInfo, Banner


class BannerTranslationOption(TranslationOptions):
    fields = ('title',)

class AboutUsTranslationOption(TranslationOptions):
    fields = ('description',)


class AdditionalLinksTranslationOptions(TranslationOptions):
    fields = ('title',)


class FAQTranslationOption(TranslationOptions):
    fields = ('question', 'answer')


class BaseInfoTranslationOption(TranslationOptions):
    fields = ('address',)


class PollTranslationOption(TranslationOptions):
    fields = ('title', 'description')


class QuestionTranslationOption(TranslationOptions):
    fields = ('text',)


class OptionTranslationOption(TranslationOptions):
    fields = ('text',)


translator.register(AboutUs, AboutUsTranslationOption)
translator.register(AdditionalLinks, AdditionalLinksTranslationOptions)
translator.register(FAQ, FAQTranslationOption)
translator.register(BaseInfo, BaseInfoTranslationOption)
translator.register(Poll, PollTranslationOption)
translator.register(Question, QuestionTranslationOption)
translator.register(Option, OptionTranslationOption)
translator.register(Banner, BannerTranslationOption)
