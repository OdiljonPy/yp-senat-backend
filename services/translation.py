from modeltranslation.translator import translator, TranslationOptions
from .models import (Region, CommissionCategory,
                     CommissionMember, Projects,
                     Appeal, Post, Video)


class VideoTranslationOption(TranslationOptions):
    fields = ('title',)

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


class PostTranslationOption(TranslationOptions):
    fields = ('title', 'short_description', 'description')


translator.register(Video, VideoTranslationOption)
translator.register(Region, RegionTranslationOption)
translator.register(Post, PostTranslationOption)
translator.register(CommissionMember, CommissionMemberTranslationOption)
translator.register(CommissionCategory, CommissionCategoryTranslationOption)
translator.register(Projects, ProjectsTranslationOption)
translator.register(Appeal, AppealTranslationOption)
