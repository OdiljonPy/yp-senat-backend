from rest_framework import serializers
from config import settings
from .models import FAQ, AboutUs, AdditionalLinks, ContactUs, Poll, Question, Option, PollResult, PollAnswer


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
        self.fields['title'] = serializers.CharField(source=f'title_{language}')
        self.fields['description'] = serializers.CharField(source=f'description_{language}')

    class Meta:
        model = AboutUs
        fields = ('id', 'title', 'description', 'telegram_url', 'instagram_url', 'facebook_url', 'youtube_url', 'is_video', 'file')


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


class ContactUsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['address'] = serializers.CharField(source=f'address_{language}')

    class Meta:
        model = ContactUs
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
        data['questions'] = QuestionSerializer(Question.objects.filter(poll_id=instance.id), many=True).data
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
        fields = ('id', 'text', 'type')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['options'] = OptionSerializer(Option.objects.filter(question_id=instance.id), many=True).data
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


class PollResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResult
        fields = ('id', 'user', 'poll')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['answers'] = PollAnswerSerializer(PollAnswer.objects.filter(result_id=instance.id), many=True).data
        return data


class PollAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollAnswer
        fields = ('id', 'result', 'question', 'answer')


class TakePollAnswerSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    answer = serializers.ListField(child=serializers.IntegerField())


class TakePollSerializer(serializers.Serializer):
    poll = serializers.IntegerField()
    answers = serializers.ListField(child=TakePollAnswerSerializer())
