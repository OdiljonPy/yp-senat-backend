# Generated by Django 5.1.2 on 2024-12-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_aboutus_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='short_description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='краткое описание'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='short_description_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='краткое описание'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='short_description_ru',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='краткое описание'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='short_description_uz',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='краткое описание'),
        ),
    ]
