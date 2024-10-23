from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from abstract_models.base_model import BaseModel
from services.models import Visitors
from utils.validations import phone_number_validation

POLL_TYPES = (
    (1, 'Единственный выбор'),
    (2, 'Множественный выбор')
)


class Banner(BaseModel):
    image = models.ImageField(upload_to='banner/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='текст')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ('-created_at',)

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
    description = HTMLField(verbose_name="описание")

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
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

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'
        ordering = ('-created_at',)


class Poll(BaseModel):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = HTMLField(verbose_name='описание')
    participant_count = models.PositiveIntegerField(default=0, verbose_name='количество участники')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = "Опросы"
        ordering = ('-created_at',)


class Question(BaseModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='опрос', related_name='questions')
    text = HTMLField(verbose_name='текст')
    type = models.PositiveIntegerField(choices=POLL_TYPES, default=1, verbose_name='тип')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы"
        ordering = ('-created_at',)


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос', related_name='options')
    text = models.CharField(max_length=100, verbose_name='текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = "Варианты"
        ordering = ('-created_at',)


class PollResult(BaseModel):
    user = models.ForeignKey(Visitors, on_delete=models.CASCADE, verbose_name='пользователь')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='опрос')

    def __str__(self):
        return self.user.ip

    class Meta:
        verbose_name = 'Результат опроса'
        verbose_name_plural = "Результаты опроса"
        ordering = ('-created_at',)


class PollAnswer(BaseModel):
    result = models.ForeignKey(PollResult, on_delete=models.CASCADE, verbose_name='результат')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    answer = models.ManyToManyField(Option, verbose_name='вариант')

    def __str__(self):
        return self.result.user.ip

    class Meta:
        verbose_name = 'Ответ на опрос'
        verbose_name_plural = "Ответы на опросы"
        ordering = ('-created_at',)
