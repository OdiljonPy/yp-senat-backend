from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, AdditionalLinks, FAQ, ContactUs, Poll, Question, Option


class AboutUsTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


class AdditionalLinksTranslationOptions(TranslationOptions):
    fields = ('title',)


class FAQTranslationOption(TranslationOptions):
    fields = ('question', 'answer')


class ContactUsTranslationOption(TranslationOptions):
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
translator.register(ContactUs, ContactUsTranslationOption)
translator.register(Poll, PollTranslationOption)
translator.register(Question, QuestionTranslationOption)
translator.register(Option, OptionTranslationOption)
