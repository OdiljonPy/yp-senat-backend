# Generated by Django 5.1.2 on 2024-12-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_alter_management_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commissionmember',
            name='description',
            field=models.CharField(max_length=255, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='description_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='описание'),
        ),
    ]
