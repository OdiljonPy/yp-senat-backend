from rest_framework import serializers
from .models import FAQ, AboutUs, AdditionalLinks, ContactUs


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'title', 'description')


class AdditionalLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalLinks
        fields = ('id', 'short_description', 'link')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'email', 'phone_number', 'address')
