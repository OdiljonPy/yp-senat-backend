import os
from django.db import models
from tinymce.models import HTMLField
from abstract_models.base_model import BaseModel
from services.utils import validate_file_type_and_size
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
    (1, "Постоянный"),
    (2, "Региональный"),
    (3, "Руководство")
)

DOC_TYPE_CHOICES = (
    ('PDF', 'PDF'),
    ('DOCX', 'Word'),
    ('XLS', 'Excel'),
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
    name = models.CharField(max_length=250, verbose_name='назавние')
    description = models.TextField(verbose_name='описание')
    icon = models.ImageField(upload_to='commission/category/', verbose_name="иконка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория комиссии'
        verbose_name_plural = 'Категория комиссий'
        ordering = ('-created_at',)


class CategoryImage(BaseModel):  # with pagination
    image = models.ImageField(upload_to='category_image/', verbose_name='изображение')
    category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE, related_name='category_image',
                                 verbose_name='категория')

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'изображение категории'
        verbose_name_plural = 'изображение категорий'
        ordering = ('-created_at',)


class CommissionMember(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    description = models.CharField(max_length=255, verbose_name="описание")
    commission_category = models.ForeignKey(CommissionCategory, on_delete=models.CASCADE,
                                            verbose_name='Категория комиссии', related_name='commission_categories')
    mandat = models.ForeignKey(to='MandatCategory', on_delete=models.CASCADE, related_name='mandat', null=True,
                               blank=True, verbose_name='мандат')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name='регион')
    order = models.PositiveIntegerField(default=1, verbose_name="порядковый номер")
    image = models.ImageField(upload_to='commission_member/', verbose_name="изображение")

    phone_number = models.CharField(max_length=14, verbose_name='номер телефона', blank=True, null=True)
    facebook = models.URLField(default='facebook.com', verbose_name="фэйсбук_url")
    linkedin = models.URLField(default='linkedin.com', verbose_name="линкедин_url")
    twitter = models.URLField(default='twitter.com', verbose_name="твиттер_url")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'член комиссии'
        verbose_name_plural = 'члены комисси'
        ordering = ('order',)


class MandatCategory(BaseModel):
    name = models.CharField(max_length=250, verbose_name='Назавние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория мандата'
        verbose_name_plural = 'Категория мандатов'
        ordering = ('-created_at',)


class Projects(BaseModel):
    name = models.CharField(max_length=100, verbose_name='навзание')
    short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = HTMLField(verbose_name='описание')
    image = models.ImageField(upload_to='project/', verbose_name='изображение')
    file = models.FileField(upload_to="project/", verbose_name='файл', validators=[validate_file_type_and_size])
    status = models.PositiveIntegerField(choices=PROJECT_STATUS, default=2, verbose_name='статус')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'проекты'
        ordering = ('-created_at',)


class Appeal(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя', null=True, blank=True)
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    email = models.EmailField(verbose_name='электронная почта', null=True, blank=True)
    message = models.TextField(verbose_name='сообщение', null=True, blank=True)
    is_resolved = models.BooleanField(default=False, verbose_name="решено")

    def __str__(self):
        return self.phone_number

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


class PostCategory(BaseModel):
    name = models.CharField(max_length=225, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория постов"
        verbose_name_plural = "Категории постов"
        ordering = ('-created_at',)


class Post(BaseModel):
    views = models.ManyToManyField(Visitors, blank=True, verbose_name="количество просмотров")
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="категория")
    title = models.CharField(max_length=255, verbose_name="заголовок")
    image = models.ImageField(upload_to='post/', verbose_name="изображение")
    short_description = models.CharField(max_length=200, verbose_name="краткое описание")
    description = HTMLField(verbose_name="описание")
    published_date = models.DateField(verbose_name="дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    is_banner = models.BooleanField(default=False, verbose_name='это баннер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)


class AppealStat(BaseModel):
    incoming_appeals = models.PositiveIntegerField(default=0, verbose_name='полученные обращения')
    resolved_appeals = models.PositiveIntegerField(default=0, verbose_name='решенные обращения')
    explained_appeals = models.PositiveIntegerField(default=0, verbose_name='объясненные обрашения')
    rejected_appeals = models.PositiveIntegerField(default=0, verbose_name='отклоненные обрашения')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Статистика обрашения'
        verbose_name_plural = 'Статистики обрашений'
        ordering = ('-created_at',)


class Video(BaseModel):
    title = models.CharField(max_length=150, verbose_name='название')
    video = models.URLField(verbose_name='видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ('-created_at',)


class NormativeDocuments(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='название')
    file = models.FileField(upload_to='normative/', verbose_name='файл', null=True, blank=True,
                            validators=[validate_file_type_and_size])
    doc_type = models.CharField(max_length=5, choices=DOC_TYPE_CHOICES, editable=False, verbose_name="тип документа")

    def save(self, *args, **kwargs):
        if self.file:
            # Extract file extension
            ext = os.path.splitext(self.file.name)[1].lower()

            # Set doc_type based on file extension
            if ext in ['.doc', '.docx']:
                self.doc_type = 'DOCX'
            elif ext in ['.xls', '.xlsx']:
                self.doc_type = 'XLS'
            elif ext == '.pdf':
                self.doc_type = 'PDF'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'нормативный документ'
        verbose_name_plural = 'нормативные документы'
        ordering = ('-created_at',)


class Management(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    description = models.CharField(max_length=300, verbose_name='описание')
    phone_number = models.CharField(max_length=15, verbose_name="номер телефона")
    position = models.CharField(max_length=150, verbose_name='позиция')
    twitter_url = models.URLField(blank=True, null=True, verbose_name="телеграм_url")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="инстаграм_url")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="фейсбук_url")
    order = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='managements/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управлении'
        ordering = ('order',)
