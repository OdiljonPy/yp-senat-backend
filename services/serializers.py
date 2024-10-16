from rest_framework import serializers
from .models import (Banner, Region, CommissionCategory, CommissionMember, Projects, News, AppealMember, Appeal, Opinion)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'short_description', 'created_at']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class CommissionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionCategory
        fields = ['id', 'name']


class CommissionMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionMember
        fields = ['id', 'full_name', 'commission_category', 'region', 'type', 'description', 'position', 'birthdate',
                  'nation', 'education_degree', 'speciality', 'email', 'telegram_url', 'youtube_url', 'instagram_url']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'short_description', 'description', 'file', 'status']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'short_description', 'description', 'telegram_url', 'youtube_url', 'instagram_url']


class AppealMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppealMember
        fields = ['id', 'commission_member', 'region', 'full_name', 'message', 'phone_number', 'address', 'email', 'gender', 'birthdate']


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'full_name', 'phone_number', 'email', 'message']


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id', 'full_name', 'phone_number', 'message']
