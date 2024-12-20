# Generated by Django 5.1.2 on 2024-11-28 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_commissioncategory_description_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'ordering': ('-created_at',), 'verbose_name': 'изображение категории', 'verbose_name_plural': 'изображение категорий'},
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='commission_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_categories', to='services.commissioncategory', verbose_name='Категория комиссии'),
        ),
    ]
