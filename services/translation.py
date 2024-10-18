from modeltranslation.translator import translator, TranslationOptions
from .models import Banner, Region, CommissionCategory, CommissionMember, Projects, Appeal


class BannerTranslationOption(TranslationOptions):
    fields = ('short_description',)


class RegionTranslationOption(TranslationOptions):
    fields = ('name',)


class CommissionCategoryTranslationOption(TranslationOptions):
    fields = ('name',)


class CommissionMemberTranslationOption(TranslationOptions):
    fields = ('full_name', 'description', 'position', 'nation', 'education_degree', 'speciality')


class ProjectsTranslationOption(TranslationOptions):
    fields = ('name', 'short_description', 'description')


class AppealTranslationOption(TranslationOptions):
    fields = ('full_name', 'message')


translator.register(Banner, BannerTranslationOption)
translator.register(Region, RegionTranslationOption)
translator.register(CommissionMember, CommissionMemberTranslationOption)
translator.register(CommissionCategory, CommissionCategoryTranslationOption)
translator.register(Projects, ProjectsTranslationOption)
translator.register(Appeal, AppealTranslationOption)
