from math import trunc

from django.db import models

from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation
from ckeditor.fields import RichTextField

POLL_TYPES = (
    (1, 'Единственный выбор'),
    (2, 'Множественный выбор')
)


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


class Poll(BaseModel):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = RichTextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = "Опросы"
        ordering = ('created_at',)


class Question(BaseModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='опрос')
    text = RichTextField(verbose_name='текст')
    type = models.PositiveIntegerField(choices=POLL_TYPES, default=1, verbose_name='тип')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы"
        ordering = ('created_at',)


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    text = models.CharField(max_length=100, verbose_name='текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = "Варианты"
        ordering = ('created_at',)


class PollResult(BaseModel):
    user = models.CharField(max_length=15, verbose_name='пользователь')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='опрос')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Результат опроса'
        verbose_name_plural = "Результаты опроса"
        ordering = ('created_at',)


class PollAnswer(BaseModel):
    result = models.ForeignKey(PollResult, on_delete=models.CASCADE, verbose_name='результат')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    answer = models.ManyToManyField(Option, verbose_name='вариант')

    def __str__(self):
        return self.result.user

    class Meta:
        verbose_name = 'Ответ на опрос'
        verbose_name_plural = "Ответы на опросы"
        ordering = ('created_at',)
