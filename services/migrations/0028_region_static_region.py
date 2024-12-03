# Generated by Django 5.1.2 on 2024-12-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0027_alter_commissionmember_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='static_region',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Andijon viloyati'), (2, 'Buxoro viloyati'), (3, 'Farg‘ona viloyati'), (4, 'Jizzax viloyati'), (5, 'Qashqadaryo viloyati'), (6, 'Namangan viloyati'), (7, 'Navoiy viloyati'), (8, 'Samarqand viloyati'), (9, 'Sirdaryo viloyati'), (10, 'Surxondaryo viloyati'), (11, 'Toshkent shahar'), (12, 'Toshkent viloyati'), (13, 'Xorazm viloyati'), (14, 'Qoraqalpog‘iston Respublikasi')], null=True),
        ),
    ]
