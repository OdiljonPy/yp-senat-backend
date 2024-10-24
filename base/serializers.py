from rest_framework import serializers
from config import settings
from .models import FAQ, AboutUs, AdditionalLinks, Poll, Question, Option, PollResult, PollAnswer, BaseInfo, Banner
from django.db.models import Count


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

    class Meta:
        model = AboutUs
        fields = ('id', 'description')


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
                  'instagram_url', 'facebook_url', 'youtube_url')


class PollSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['title'] = serializers.CharField(source=f'title_{language}')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')

    class Meta:
        model = Poll
        fields = ('id', 'title', 'description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['questions'] = QuestionSerializer(instance.questions, many=True, context=self.context).data
        return data


class QuestionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['text'] = serializers.CharField(source=f'text_{language}')

    class Meta:
        model = Question
        fields = ('id', 'text', 'type')  # 'poll',

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['options'] = OptionSerializer(instance.options, many=True, context=self.context).data
        return data


class OptionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['text'] = serializers.CharField(source=f'text_{language}')

    class Meta:
        model = Option
        fields = ('id', 'question', 'text')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        option_count = PollAnswer.objects.filter(answer__in=[instance.id], question_id=instance.question.id).count()
        total_count = PollAnswer.objects.filter(question_id=instance.question.id).aggregate(num_answers=Count('answer'))
        percentage = 0.0
        if total_count['num_answers'] != 0:
            percentage = option_count * 100 / total_count['num_answers']
        data['percentage_option'] = percentage
        return data


class PollResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResult
        fields = ('id', 'user', 'poll')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['poll'] = PollSerializer(instance.poll, context=self.context).data
        data['answers'] = PollAnswerSerializer(instance.answers, many=True, context=self.context).data
        return data


class PollAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollAnswer
        fields = ('id', 'question', 'answer')

    def validate(self, attrs):
        attrs['result'] = self.context['result']
        return attrs


class TakePollAnswerSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    answer = serializers.ListField(child=serializers.IntegerField())


class TakePollSerializer(serializers.Serializer):
    poll = serializers.IntegerField()
    answers = serializers.ListField(child=TakePollAnswerSerializer())
