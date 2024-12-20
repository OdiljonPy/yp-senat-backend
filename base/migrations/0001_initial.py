# Generated by Django 5.1.2 on 2024-10-25 00:29

import django.db.models.deletion
import tinymce.models
import utils.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', tinymce.models.HTMLField(verbose_name='описание')),
                ('description_uz', tinymce.models.HTMLField(null=True, verbose_name='описание')),
                ('description_ru', tinymce.models.HTMLField(null=True, verbose_name='описание')),
                ('description_en', tinymce.models.HTMLField(null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AdditionalLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='название')),
                ('link', models.URLField(verbose_name='ссылка')),
                ('image', models.ImageField(upload_to='additional_links/', verbose_name='изображение')),
                ('is_visible', models.BooleanField(default=True, verbose_name='опубликован')),
            ],
            options={
                'verbose_name': 'Дополнительные ссылка',
                'verbose_name_plural': 'Дополнительные ссылки',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=255, verbose_name='текст')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('phone_number', models.CharField(max_length=14, validators=[utils.validations.phone_number_validation], verbose_name='номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='название адреса')),
                ('address_uz', models.CharField(max_length=255, null=True, verbose_name='название адреса')),
                ('address_ru', models.CharField(max_length=255, null=True, verbose_name='название адреса')),
                ('address_en', models.CharField(max_length=255, null=True, verbose_name='название адреса')),
                ('latitude', models.FloatField(verbose_name='широта')),
                ('longitude', models.FloatField(verbose_name='долгота')),
                ('telegram_url', models.URLField(default='telegram.org', verbose_name='телеграм_url')),
                ('instagram_url', models.URLField(default='instagram.com', verbose_name='инстаграм_url')),
                ('facebook_url', models.URLField(default='facebook.com', verbose_name='фэйсбук_url')),
                ('youtube_url', models.URLField(default='youtube.com', verbose_name='ютубе_url')),
            ],
            options={
                'verbose_name': 'Связаться с нами',
                'verbose_name_plural': 'Связаться с нами',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(max_length=700, verbose_name='вопрос')),
                ('question_uz', models.TextField(max_length=700, null=True, verbose_name='вопрос')),
                ('question_ru', models.TextField(max_length=700, null=True, verbose_name='вопрос')),
                ('question_en', models.TextField(max_length=700, null=True, verbose_name='вопрос')),
                ('answer', models.TextField(max_length=1000, verbose_name='ответ')),
                ('answer_uz', models.TextField(max_length=1000, null=True, verbose_name='ответ')),
                ('answer_ru', models.TextField(max_length=1000, null=True, verbose_name='ответ')),
                ('answer_en', models.TextField(max_length=1000, null=True, verbose_name='ответ')),
                ('is_visible', models.BooleanField(default=True, verbose_name='опубликован')),
            ],
            options={
                'verbose_name': 'Часто задаваемые вопросы',
                'verbose_name_plural': 'Часто задаваемые вопросы',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=100, verbose_name='текст')),
                ('text_uz', models.CharField(max_length=100, null=True, verbose_name='текст')),
                ('text_ru', models.CharField(max_length=100, null=True, verbose_name='текст')),
                ('text_en', models.CharField(max_length=100, null=True, verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('title_uz', models.CharField(max_length=100, null=True, verbose_name='заголовок')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='заголовок')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='заголовок')),
                ('description', tinymce.models.HTMLField(verbose_name='описание')),
                ('description_uz', tinymce.models.HTMLField(null=True, verbose_name='описание')),
                ('description_ru', tinymce.models.HTMLField(null=True, verbose_name='описание')),
                ('description_en', tinymce.models.HTMLField(null=True, verbose_name='описание')),
                ('participant_count', models.PositiveIntegerField(default=0, verbose_name='количество участники')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.poll', verbose_name='опрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.visitors', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Результат опроса',
                'verbose_name_plural': 'Результаты опроса',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', tinymce.models.HTMLField(verbose_name='текст')),
                ('text_uz', tinymce.models.HTMLField(null=True, verbose_name='текст')),
                ('text_ru', tinymce.models.HTMLField(null=True, verbose_name='текст')),
                ('text_en', tinymce.models.HTMLField(null=True, verbose_name='текст')),
                ('type', models.PositiveIntegerField(choices=[(1, 'Единственный выбор'), (2, 'Множественный выбор')], default=1, verbose_name='тип')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='base.poll', verbose_name='опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='PollAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ManyToManyField(to='base.option', verbose_name='вариант')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='base.pollresult', verbose_name='результат')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.question', verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'Ответ на опрос',
                'verbose_name_plural': 'Ответы на опросы',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='base.question', verbose_name='вопрос'),
        ),
    ]
