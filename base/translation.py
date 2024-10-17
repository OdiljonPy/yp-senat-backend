from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, AdditionalLinks, FAQ, ContactUs


class AboutUsTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


class AdditionalLinksTranslationOptions(TranslationOptions):
    fields = ('title',)


class FAQTranslationOption(TranslationOptions):
    fields = ('question', 'answer')


class ContactUsTranslationOption(TranslationOptions):
    fields = ('address',)


translator.register(AboutUs, AboutUsTranslationOption)
translator.register(AdditionalLinks, AdditionalLinksTranslationOptions)
translator.register(FAQ, FAQTranslationOption)
translator.register(ContactUs, ContactUsTranslationOption)
