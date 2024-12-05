from config import settings
from rest_framework import serializers
from services.serializers import ParamValidateSerializer
from .models import (FAQ, AboutUs,
                     AdditionalLinks, Poll,
                     BaseInfo, STATUS_POLL, AboutUsImage)


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('id', 'image', 'about_us')


class PollParamSerializer(ParamValidateSerializer):
    poll_name = serializers.CharField(max_length=150, required=False)
    poll_status = serializers.ChoiceField(choices=STATUS_POLL, required=False)


class FAQSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['question'] = serializers.CharField(source=f'question_{language}')
        self.fields['answer'] = serializers.CharField(source=f'answer_{language}')

    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer', 'is_visible')


class AboutUsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')
        self.fields['short_description'] = serializers.CharField(source=f'short_description_{language}')

    class Meta:
        model = AboutUs
        fields = ('id', "short_description", 'description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = AboutUsImageSerializer(instance.about_image.all(), many=True, context=self.context).data
        return data


class AdditionalLinksSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['title'] = serializers.CharField(source=f'title_{language}')

    class Meta:
        model = AdditionalLinks
        fields = ('id', 'title', 'link', 'is_visible')


class BaseInfoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['address'] = serializers.CharField(source=f'address_{language}')

    class Meta:
        model = BaseInfo
        fields = ('id', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'telegram_url',
                  'instagram_url', 'facebook_url', 'youtube_url', 'twitter_url', 'linkedin_url')


class PollSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f'name_{language}')
        self.fields['result'] = serializers.CharField(source=f'result_{language}')

    class Meta:
        model = Poll
        fields = ('id', 'name', 'status', 'started_at', 'ended_at', 'result', 'link_to_poll')
