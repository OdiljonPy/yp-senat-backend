# Generated by Django 5.1.2 on 2024-10-23 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_visitors_remove_post_views_count_post_views_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterModelOptions(
            name='appeal',
            options={'ordering': ('-created_at',), 'verbose_name': 'Запрос', 'verbose_name_plural': 'Запросы'},
        ),
        migrations.AlterModelOptions(
            name='commissioncategory',
            options={'ordering': ('-created_at',), 'verbose_name': 'Категория комиссии', 'verbose_name_plural': 'Категория комиссий'},
        ),
        migrations.AlterModelOptions(
            name='commissionmember',
            options={'ordering': ('-created_at',), 'verbose_name': 'член комиссии', 'verbose_name_plural': 'члены комисси'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ('-created_at',), 'verbose_name': 'Проект', 'verbose_name_plural': 'проекты'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('-created_at',), 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterModelOptions(
            name='visitors',
            options={'ordering': ('-created_at',), 'verbose_name': 'Ip адрес', 'verbose_name_plural': 'Ip адресы'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='telegram_url',
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='birthdate',
            field=models.DateField(verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='commission_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.commissioncategory', verbose_name='Категория комиссии'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='facebook_url',
            field=models.URLField(blank=True, null=True, verbose_name='фэйсбук_url'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='инстаграм_url'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='telegram_url',
            field=models.URLField(blank=True, null=True, verbose_name='телеграм_url'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='изображение'),
        ),
    ]
