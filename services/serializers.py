from rest_framework import serializers

from config import settings
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import (
    Region, CommissionCategory,
    CommissionMember, Projects,
    Post, Appeal, PROJECT_STATUS)


class ParamValidateSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    page_size = serializers.IntegerField(required=False, default=10)
    status = serializers.ChoiceField(PROJECT_STATUS, required=False)

    def validate(self, data):
        if (data.get('page_size') and data.get('page_size') < 1) or (data.get('page') and data.get('page') < 1):
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED,
                                     message='page and page_size must be positive integer')
        return data


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category_name'] = CommissionCategorySerializer(instance.commission_category,
                                                             context=self.context).data
        data['region'] = RegionSerializer(instance.region, context=self.context).data
        data['posts'] = PostSerializer(instance.member_post.filter(is_published=True).order_by('-created_at')[:6],
                                       many=True,
                                       context=self.context).data  # here cannot be used select_related because it's cannot refer to the model through related_name.
        return data


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
        fields = ['id', 'name', 'short_description', 'image', 'description', 'file', 'status', 'created_at',
                  'is_published']


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

    views_count = serializers.IntegerField(source='views.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'views_count', 'image', 'short_description', 'description', 'commission_member',
                  'created_at',
                  'is_published']


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'commission_member', 'full_name', 'phone_number', 'email', 'message']


class PostFilterSerializer(ParamValidateSerializer):
    q = serializers.CharField(required=False)
    post_member_exist = serializers.BooleanField(required=False)


class MandatCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    mandats = CommissionMemberSerializer(many=True)


class AppealStatSerializer(serializers.Serializer):
    incoming_appeals = serializers.IntegerField(required=False, default=0)
    resolved_appeals = serializers.IntegerField(required=False, default=0)
    explained_appeals = serializers.IntegerField(required=False, default=0)
    rejected_appeals = serializers.IntegerField(required=False, default=0)
