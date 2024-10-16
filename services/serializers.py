from rest_framework.serializers import ModelSerializer
from .models import (Banner, Region, CommissionCategory, CommissionMember, Projects, News, AppealMember, Appeal, Opinion)


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'short_description', 'created_at']


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class CommissionCategorySerializer(ModelSerializer):
    class Meta:
        model = CommissionCategory
        fields = ['id', 'name']


class CommissionMemberSerializer(ModelSerializer):
    class Meta:
        model = CommissionMember
        fields = ['id', 'name', 'commission_category', 'region', 'type', 'description', 'position', 'birthdate',
                  'nation', 'education_degree', 'speciality', 'email', 'telegram_url', 'youtube_url', 'instagram_url']


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'short_description', 'description', 'file', 'status']


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'short_description', 'description', 'telegram_url', 'youtube_url', 'instagram_url']


class AppealMemberSerializer(ModelSerializer):
    class Meta:
        model = AppealMember
        fields = ['id', 'commission_member', 'region', 'name', 'message', 'phone_number', 'address', 'email', 'gender', 'birthdate']


class AppealSerializer(ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'full_name', 'phone_number', 'email', 'message']


class OpinionSerializer(ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id', 'full_name', 'phone_number', 'message']
