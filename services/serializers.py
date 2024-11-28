from rest_framework import serializers

from config import settings
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import (
    Region, CommissionCategory,
    CommissionMember, Projects,
    Post, Appeal, PROJECT_STATUS, Video, MandatCategory)


class VideoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['title'] = serializers.CharField(source=f'title_{language}')

    class Meta:
        model = Video
        fields = ['id', 'title', 'video']


class ParamValidateSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    page_size = serializers.IntegerField(required=False, default=10)

    def validate(self, data):
        if data.get('page_size', 0) < 1 or (data.get('page') and data.get('page') < 1):
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED,
                                     message='page and page_size must be positive integer')
        return data


class ProjectsResponseSerializer(ParamValidateSerializer):
    status = serializers.ChoiceField(choices=PROJECT_STATUS, required=False)


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
        self.fields['description'] = serializers.CharField(source=f'description_{language}')

    class Meta:
        model = CommissionCategory
        fields = ['id', 'name', 'description']


class CategoryImageResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField(read_only=True)


class PostCategory(serializers.Serializer):
    name = serializers.CharField()


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
                  'created_at', 'is_published', 'published_date']





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
        fields = ['id', 'full_name', "image", 'commission_category', 'region', 'type', 'description', 'position', 'birthdate',
                  'nation', 'education_degree', 'speciality', 'email', 'telegram_url', 'facebook_url', 'instagram_url']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['region'] = RegionSerializer(instance.region, context=self.context).data
        data['posts'] = PostSerializer(instance.member_post.filter(is_published=True).order_by('-created_at')[:6],
                                       many=True,
                                       context=self.context).data
        return data


class CommissionCategoryResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    category_image = CategoryImageResponseSerializer(many=True, read_only=True)
    commission_categories = CommissionMemberSerializer(many=True, read_only=True)


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


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'commission_member', 'full_name', 'phone_number', 'email', 'message']


class PostFilterSerializer(ParamValidateSerializer):
    q = serializers.CharField(required=False)
    post_member_exist = serializers.BooleanField(required=False)
    status = serializers.ChoiceField(PROJECT_STATUS, required=False)


class PostCategoryFilterSerializer(ParamValidateSerializer):
    category_id = serializers.IntegerField(required=False)

    def validate(self, data):
        if data.get('category_id') and data.get('category_id') <= 0:
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Category id must be positive integer')
        return data


class MandatFilterSerializer(ParamValidateSerializer):
    id = serializers.IntegerField(required=False)


class AppealStatSerializer(serializers.Serializer):
    incoming_appeals = serializers.IntegerField(required=False, default=0)
    resolved_appeals = serializers.IntegerField(required=False, default=0)
    explained_appeals = serializers.IntegerField(required=False, default=0)
    rejected_appeals = serializers.IntegerField(required=False, default=0)


class CategorySerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)

class MandatCategorySerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    id = serializers.IntegerField()
    name = serializers.CharField()


class MandatCategoryDetailSerializer(MandatCategorySerializer):
    commission_members = CommissionMemberSerializer(many=True)