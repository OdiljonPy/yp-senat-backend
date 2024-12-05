from django.db import models
from tinymce.models import HTMLField
from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation

POLL_TYPES = (
    (1, 'Единственный выбор'),
    (2, 'Множественный выбор')
)

STATUS_POLL = (
    (1, 'Активный'),
    (2, 'Завершено')
)


class FAQ(BaseModel):
    question = models.TextField(max_length=700, verbose_name='вопрос')
    answer = models.TextField(max_length=1000, verbose_name='ответ')
    is_visible = models.BooleanField(default=True, verbose_name='опубликован')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ('-created_at',)


class AboutUs(BaseModel):
    short_description = models.CharField(max_length=300, verbose_name="краткое описание", blank=True, null=True)
    description = HTMLField(verbose_name="описание")

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ('-created_at',)


class AboutUsImage(BaseModel):
    image = models.ImageField(upload_to='about_us/', verbose_name='Изоражение')
    about_us = models.ForeignKey(AboutUs, on_delete=models.SET_NULL, null=True, related_name='about_image',
                                 verbose_name="о нас")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Изображение о нас"
        verbose_name_plural = "изображения о нас"
        ordering = ('-created_at',)


class AdditionalLinks(BaseModel):
    title = models.CharField(max_length=250, verbose_name='название')
    link = models.URLField(verbose_name='ссылка')
    image = models.ImageField(upload_to='additional_links/', verbose_name='изображение')
    is_visible = models.BooleanField(default=True, verbose_name='опубликован')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Дополнительные ссылка'
        verbose_name_plural = 'Дополнительные ссылки'
        ordering = ('-created_at',)


class BaseInfo(BaseModel):
    email = models.EmailField(verbose_name='электронная почта')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    address = models.CharField(max_length=255, verbose_name='название адреса')
    latitude = models.FloatField(verbose_name="широта")
    longitude = models.FloatField(verbose_name="долгота")

    telegram_url = models.URLField(default='telegram.org', verbose_name="телеграм_url")
    instagram_url = models.URLField(default='instagram.com', verbose_name="инстаграм_url")
    facebook_url = models.URLField(default='facebook.com', verbose_name="фэйсбук_url")
    youtube_url = models.URLField(default='youtube.com', verbose_name="ютубе_url")
    twitter_url = models.URLField(default='twitter.com', verbose_name='твиттер_url')
    linkedin_url = models.URLField(default='linkedin.com', verbose_name='линкедин_url')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'
        ordering = ('-created_at',)


class Poll(BaseModel):
    name = models.CharField(max_length=150, verbose_name='название')

    started_at = models.DateField(verbose_name='дата начала')
    ended_at = models.DateField(verbose_name='дата окончания')

    status = models.PositiveIntegerField(choices=STATUS_POLL, default=1, verbose_name='Состояние')

    result = HTMLField(verbose_name='Результат')

    link_to_poll = models.URLField(verbose_name='Ссылка на опрос')
    sheet_id = models.CharField(verbose_name='Эксел ид')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = "Опросы"
        ordering = ('-created_at',)
