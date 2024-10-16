from django.db import models

from abstract_models.base_model import BaseModel
from django_ckeditor_5.fields import CKEditor5Field


class FAQ(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class AboutUs(BaseModel):
    title = models.CharField(max_length=200)
    description = CKEditor5Field()

    def __str__(self):
        return self.title


class AdditionalLinks(BaseModel):
    short_description = models.CharField(max_length=500)
    link = models.URLField()
    image = models.ImageField(upload_to='additional_links/')

    def __str__(self):
        return str(self.id) or ''


class ContactUs(BaseModel):
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id) or ''
