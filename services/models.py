from ckeditor.fields import RichTextField
from django.db import models

from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
)

PROJECT_STATUS = (
    (1, "Finished"),
    (2, "InProces"),
)

MEMBER_TYPE = (
    (1, 'Constant'),
    (2, "Regional"),
)


class Banner(BaseModel):
    image = models.ImageField(upload_to='banner/', verbose_name='Изображение')
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ('created_at',)


class Region(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Назавние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('created_at',)


class CommissionCategory(BaseModel):
    name = models.CharField(max_length=250, verbose_name='Назавние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория комиссии'
        verbose_name_plural = 'Категория комиссий'
        ordering = ('created_at',)


class CommissionMember(BaseModel):
    commission_category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE, blank=True, null=True,
                                            verbose_name='Категория комиссии')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name='регион')

    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    type = models.PositiveIntegerField(choices=MEMBER_TYPE, default=1, verbose_name='тип')
    description = RichTextField(verbose_name='описание')
    position = models.CharField(max_length=80, verbose_name='позиция')
    birthdate = models.DateTimeField(verbose_name='дата рождения')
    nation = models.CharField(max_length=100, verbose_name='нация')
    education_degree = models.CharField(max_length=100, verbose_name='степень образования')
    speciality = models.CharField(max_length=150, verbose_name='специальность')
    email = models.EmailField(verbose_name='электронная почта')

    telegram_url = models.URLField(default='telegram.org', )
    instagram_url = models.URLField(default='instagram.com')
    facebook_url = models.URLField(default='facebook.com')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'член комиссии'
        verbose_name_plural = 'члены комисси'
        ordering = ('created_at',)


class Projects(BaseModel):
    name = models.CharField(max_length=100, verbose_name='навзание')
    short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = RichTextField(verbose_name='описание')
    file = models.FileField(upload_to="project/", verbose_name='файл')
    status = models.PositiveIntegerField(choices=PROJECT_STATUS, default=2, verbose_name='статус')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'проекты'
        ordering = ('created_at',)


class AppealMember(BaseModel):
    commission_member = models.ForeignKey(CommissionMember, on_delete=models.CASCADE, verbose_name='член комиссии')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='регион')

    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    message = models.TextField(verbose_name='сообщение')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    address = models.CharField(max_length=255, verbose_name='адрес')
    email = models.EmailField(verbose_name='электронная почта')
    gender = models.PositiveIntegerField(choices=GENDER, default=1, verbose_name='пол')
    birthdate = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Запрос член'
        verbose_name_plural = 'Запросы члена'
        ordering = ('created_at',)


class Appeal(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    email = models.EmailField(verbose_name='электронная почта')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
        ordering = ('created_at',)


class News(BaseModel):
    image = models.ImageField(upload_to='news/', verbose_name='Изображение')
    short_description = models.CharField(max_length=200, verbose_name='краткое описания')
    description = RichTextField(verbose_name='Описание')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    telegram_url = models.URLField(default='telegram.org')
    instagram_url = models.URLField(default='instagram.com')
    facebook_url = models.URLField(default='facebook.com')

    def __str__(self):
        return self.short_description

    class Meta:
        verbose_name = 'Новост'
        verbose_name_plural = 'Новости'
        ordering = ('created_at',)


class Opinion(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Мнение'
        verbose_name_plural = 'Мнения'
        ordering = ('created_at',)
