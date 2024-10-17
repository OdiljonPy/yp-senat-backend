from math import trunc

from django.db import models

from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation
from ckeditor.fields import RichTextField


class FAQ(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class AboutUs(BaseModel):
    title = models.CharField(max_length=200)
    description = RichTextField()

    telegram_url = models.URLField(default='telegram.org')
    instagram_url = models.URLField(default='instagram.com')
    facebook_url = models.URLField(default='facebook.com')

    def __str__(self):
        return self.title


class AdditionalLinks(BaseModel):
    title = models.CharField(max_length=250)
    link = models.URLField()
    image = models.ImageField(upload_to='additional_links/')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) or ''


class ContactUs(BaseModel):
    email = models.EmailField()
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation])
    address = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id) or ''
