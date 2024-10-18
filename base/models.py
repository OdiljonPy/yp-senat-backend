
from django.db import models
from tinymce.models import HTMLField

from abstract_models.base_model import BaseModel
from utils.validations import phone_number_validation

POLL_TYPES = (
    (1, 'Единственный выбор'),
    (2, 'Множественный выбор')
)


class FAQ(BaseModel):
    question = models.CharField(max_length=200, verbose_name='вопрос')
    answer = models.CharField(max_length=200, verbose_name='ответ')
    is_visible = models.BooleanField(default=True, verbose_name='видимый')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ['question']


class AboutUs(BaseModel):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    description = HTMLField()

    telegram_url = models.URLField(default='telegram.org')
    instagram_url = models.URLField(default='instagram.com')
    facebook_url = models.URLField(default='facebook.com')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['title']


class AdditionalLinks(BaseModel):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    link = models.URLField(verbose_name='ссылка')
    image = models.ImageField(upload_to='additional_links/', verbose_name='')
    is_visible = models.BooleanField(default=True, verbose_name='изображение')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Дополнительные ссылка'
        verbose_name_plural = 'Дополнительные ссылки'
        ordering = ['title']


class ContactUs(BaseModel):
    email = models.EmailField(verbose_name='электронная почта')
    phone_number = models.CharField(max_length=14, validators=[phone_number_validation], verbose_name='номер телефона')
    address = models.CharField(max_length=300, verbose_name='адрес')

    def __str__(self):
        return str(self.id) or ''

    class Meta:
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'
        ordering = ['phone_number']


class Poll(BaseModel):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = HTMLField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = "Опросы"
        ordering = ('created_at',)


class Question(BaseModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='опрос')
    text = HTMLField(verbose_name='текст')
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
