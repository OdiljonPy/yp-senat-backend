from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Region, CommissionCategory, CommissionMember,
    Projects, Appeal, Post, Video, PostCategory,
    MandatCategory, Management, NormativeDocuments
)


class MandatCategoryTranslationOption(TranslationOptions):
    fields = ('name',)


class VideoTranslationOption(TranslationOptions):
    fields = ('title',)


class RegionTranslationOption(TranslationOptions):
    fields = ('name',)


class CommissionCategoryTranslationOption(TranslationOptions):
    fields = ('name', "description",)


class CommissionMemberTranslationOption(TranslationOptions):
    fields = ('full_name', 'description',)


class ProjectsTranslationOption(TranslationOptions):
    fields = ('name', 'short_description', 'description')


class AppealTranslationOption(TranslationOptions):
    fields = ('full_name', 'message')


class PostTranslationOption(TranslationOptions):
    fields = ('title', 'short_description', 'description')


class PostCategoryTranslationOption(TranslationOptions):
    fields = ('name',)


class ManagementTranslationOption(TranslationOptions):
    fields = ('full_name', 'description', 'position')

class NormativeDocumentsTranslationOption(TranslationOptions):
    fields = ('name',)


translator.register(MandatCategory, MandatCategoryTranslationOption)
translator.register(NormativeDocuments, NormativeDocumentsTranslationOption)
translator.register(Video, VideoTranslationOption)
translator.register(Region, RegionTranslationOption)
translator.register(Post, PostTranslationOption)
translator.register(CommissionMember, CommissionMemberTranslationOption)
translator.register(CommissionCategory, CommissionCategoryTranslationOption)
translator.register(Projects, ProjectsTranslationOption)
translator.register(Appeal, AppealTranslationOption)
translator.register(PostCategory, PostCategoryTranslationOption)
translator.register(Management, ManagementTranslationOption)
