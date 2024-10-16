from random import choices

from django.db import models
from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
)

PROJECT_STATUS = (
    (1, "Finished"),
    (2, "In_proces"),
)

MEMBER_TYPE = (
    (1, 'Constant'),
    (2, "Regional"),
)


class Banner(BaseModel):
    image = models.ImageField(upload_to='banner/')
    short_description = models.CharField(max_length=350)

    def __str__(self):
        return str(self.id) or ''


class Region(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class CommissionCategory(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class CommissionMember(BaseModel):
    commission_category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100)
    type = models.PositiveIntegerField(choices=MEMBER_TYPE, default=1)
    description = models.TextField()
    position = models.CharField(max_length=80)
    birthdate = models.DateTimeField()
    nation = models.CharField(max_length=100)
    education_degree = models.CharField(max_length=100)
    speciality = models.CharField(max_length=150)
    email = models.EmailField()

    telegram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Projects(BaseModel):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    file = models.FileField(upload_to="project/")
    status = models.PositiveIntegerField(choices=PROJECT_STATUS, default=2)

    def __str__(self):
        return self.name


class AppealMember(BaseModel):
    commission_member = models.ForeignKey(CommissionMember, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=120)
    message = models.TextField()
    phone_number = models.CharField(max_length=14, validators=phone_number_validation)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    gender = models.PositiveIntegerField(choices=GENDER, default=1)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Appeal(BaseModel):
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=14, validators=phone_number_validation)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name


class News(BaseModel):
    image = models.ImageField(upload_to='news/')
    short_description = models.CharField(max_length=300)
    description = models.TextField()

    telegram_url = models.URLField()
    instagram_url = models.URLField()
    facebook_url = models.URLField()

    def __str__(self):
        return self.short_description


class PollQuestion(BaseModel):
    question = models.CharField(max_length=600)


class PollAnswer(BaseModel):
    answer = models.CharField(max_length=600)
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    is_true = models.BooleanField(default=False)


class Opinion(BaseModel):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, validators=phone_number_validation)
    message = models.TextField()

    def __str__(self):
        return self.full_name
