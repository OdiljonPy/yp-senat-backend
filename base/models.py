from django.db import models

from abstract_models.base_model import BaseModel


class FAQ(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class AboutUs(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class AdditionalLinks(BaseModel):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title


class ContactUs(BaseModel):
    title = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.title
