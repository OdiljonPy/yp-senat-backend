from django.db import models
from abstract_models.base_model import BaseModel

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
)

PROJECT_STATUS = (
    (1, "Finished"),
    (2, "In_proces"),
)

class Region(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class CommissionCategory(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class CommissionMember(BaseModel):
    commission_category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.CharField(max_length=80)
    birthdate = models.DateTimeField()
    nation = models.CharField(max_length=100)
    education_degree = models.CharField(max_length=100)
    speciality = models.CharField(max_length=150)
    email = models.EmailField()
    membership = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Projects(BaseModel):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="project/")
    status = models.PositiveIntegerField(choices=PROJECT_STATUS, default=2)

    def __str__(self):
        return self.name

class ProjectComment(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.project.name


class AppealType(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appeal(BaseModel):
    commission_member = models.ForeignKey(CommissionMember, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    appeal_category = models.ForeignKey(AppealType, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    message = models.TextField()
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    gender = models.PositiveIntegerField(choices=GENDER, default=1)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class News(BaseModel):
    image = models.ImageField(upload_to='news/')
    short_description = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.short_description

class PollQuestion(BaseModel):
    question = models.CharField(max_length=600)

class PollAnswer(BaseModel):
    answer = models.CharField(max_length=600)
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    is_true = models.BooleanField(default=False)


class Opinion(BaseModel):
    full_name = models.CharField(max_length=150)
    text = models.TextField()
