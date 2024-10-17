from modeltranslation.translator import translator, TranslationOptions
from .models import Banner, Region, News, CommissionCategory, CommissionMember, Projects, AppealMember, Appeal, Opinion


class BannerTranslationOption(TranslationOptions):
    fields = ('short_description',)


class RegionTranslationOption(TranslationOptions):
    fields = ('name',)


class NewsTranslationOption(TranslationOptions):
    fields = ('short_description', 'description',)


class CommissionCategoryTranslationOption(TranslationOptions):
    fields = ('name',)


class CommissionMemberTranslationOption(TranslationOptions):
    fields = ('full_name', 'description', 'position', 'nation', 'education_degree', 'speciality')


class ProjectsTranslationOption(TranslationOptions):
    fields = ('name', 'short_description', 'description')


class AppealMemberTranslationOption(TranslationOptions):
    fields = ('full_name', 'message', 'address', 'gender',)


class AppealTranslationOption(TranslationOptions):
    fields = ('full_name', 'message')


class OpinionTranslationOption(TranslationOptions):
    fields = ('full_name', 'message')


translator.register(Banner, BannerTranslationOption)
translator.register(Region, RegionTranslationOption)
translator.register(News, NewsTranslationOption)
translator.register(CommissionMember, CommissionMemberTranslationOption)
translator.register(CommissionCategory, CommissionCategoryTranslationOption)
translator.register(Projects, ProjectsTranslationOption)
translator.register(AppealMember, AppealMemberTranslationOption)
translator.register(Appeal, AppealTranslationOption)
translator.register(Opinion, OpinionTranslationOption)
