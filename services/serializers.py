from rest_framework import serializers
from config import settings
from .models import (
    Banner, Region, CommissionCategory, CommissionMember, Projects, Post, Appeal, PROJECT_STATUS)
from exceptions.exception import CustomApiException
from exceptions.error_messages import ErrorCodes


class ParamValidateSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    page_size = serializers.IntegerField(required=False, default=10)
    status = serializers.ChoiceField(PROJECT_STATUS, required=False)

    def validate(self, data):
        if (data.get('page_size') and data.get('page_size') < 1) or (data.get('page') and data.get('page') < 1):
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED,
                                     message='page and page_size must be positive integer')
        return data


class BannerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['title'] = serializers.CharField(source=f'title_{language}')

    class Meta:
        model = Banner
        fields = ['id', 'image', 'title', 'created_at', 'is_published']


class RegionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = Region
        fields = ['id', 'name']


class CommissionCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = CommissionCategory
        fields = ['id', 'name']


class CommissionMemberSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['full_name'] = serializers.CharField(source=f'full_name_{language}')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')
        self.fields['position'] = serializers.CharField(source=f'position_{language}')
        self.fields['nation'] = serializers.CharField(source=f'nation_{language}')
        self.fields['education_degree'] = serializers.CharField(source=f'education_degree_{language}')
        self.fields['speciality'] = serializers.CharField(source=f'speciality_{language}')

    class Meta:
        model = CommissionMember
        fields = ['id', 'full_name', 'commission_category', 'region', 'type', 'description', 'position', 'birthdate',
                  'nation', 'education_degree', 'speciality', 'email', 'telegram_url', 'facebook_url', 'instagram_url']


class ProjectsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')
        self.fields['short_description'] = serializers.CharField(source=f'short_description_{language}')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')

    class Meta:
        model = Projects
        fields = ['id', 'name', 'short_description', 'description', 'file', 'status', 'created_at', 'is_published']


class PostSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['title'] = serializers.CharField(source=f'title_{language}')
        self.fields['short_description'] = serializers.CharField(source=f'short_description_{language}')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')

    class Meta:
        model = Post
        fields = ['id', 'image', 'short_description', 'description', 'commission_member', 'telegram_url',
                  'instagram_url', 'facebook_url', 'created_at', 'is_published']


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'full_name', 'phone_number', 'email', 'message']


class PostFilterSerializer(ParamValidateSerializer):
    q = serializers.CharField(required=False)
