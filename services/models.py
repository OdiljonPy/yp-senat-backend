from django.db import models
from tinymce.models import HTMLField

from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation

GENDER = (
    (1, 'Мужчина'),
    (2, 'Женщина'),
)

PROJECT_STATUS = (
    (1, "Оконченный"),
    (2, "В процессе"),
)

MEMBER_TYPE = (
    (1, 'Постоянный'),
    (2, "Региональный"),
)


class Region(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Назавние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('-created_at',)


class CommissionCategory(BaseModel):
    name = models.CharField(max_length=250, verbose_name='Назавние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория комиссии'
        verbose_name_plural = 'Категория комиссий'
        ordering = ('-created_at',)


class CommissionMember(BaseModel):
    commission_category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE,
                                            verbose_name='Категория комиссии')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name='регион')

    image = models.ImageField(upload_to='commission_member/')
    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    type = models.PositiveIntegerField(choices=MEMBER_TYPE, default=1, verbose_name='тип')
    description = HTMLField(verbose_name='описание')
    position = models.CharField(max_length=80, verbose_name='позиция')
    birthdate = models.DateField(verbose_name='дата рождения')
    nation = models.CharField(max_length=100, verbose_name='нация')
    education_degree = models.CharField(max_length=100, verbose_name='степень образования')
    speciality = models.CharField(max_length=150, verbose_name='специальность')
    email = models.EmailField(verbose_name='электронная почта')

    telegram_url = models.URLField(blank=True, null=True, verbose_name="телеграм_url")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="инстаграм_url")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="фэйсбук_url")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'член комиссии'
        verbose_name_plural = 'члены комисси'
        ordering = ('-created_at',)


class Projects(BaseModel):
    name = models.CharField(max_length=100, verbose_name='навзание')
    short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = HTMLField(verbose_name='описание')
    file = models.FileField(upload_to="project/", verbose_name='файл')
    status = models.PositiveIntegerField(choices=PROJECT_STATUS, default=2, verbose_name='статус')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'проекты'
        ordering = ('-created_at',)


class Appeal(BaseModel):
    commission_member = models.ForeignKey(CommissionMember, on_delete=models.CASCADE, blank=True, null=True)

    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    email = models.EmailField(verbose_name='электронная почта')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
        ordering = ('-created_at',)


class Visitors(BaseModel):
    name = models.CharField(max_length=225)
    ip = models.CharField(max_length=225)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Ip адрес'
        verbose_name_plural = 'Ip адресы'
        ordering = ('-created_at',)


class Post(BaseModel):
    commission_member = models.ForeignKey(CommissionMember, on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='member_post',
                                          verbose_name="член комиссии")
    views = models.ManyToManyField(Visitors, blank=True, verbose_name="количество просмотров")

    title = models.CharField(max_length=255, verbose_name="заголовок")
    image = models.ImageField(upload_to='post/', verbose_name="изображение")
    short_description = models.CharField(max_length=200, verbose_name="краткое описание")
    description = HTMLField(verbose_name="описание")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    @property
    def counting(self):
        return self.views.count()
