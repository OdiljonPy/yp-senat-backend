# Generated by Django 5.1.2 on 2024-11-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_remove_commissionmember_mandat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandatcategory',
            name='name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Назавние'),
        ),
        migrations.AddField(
            model_name='mandatcategory',
            name='name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Назавние'),
        ),
        migrations.AddField(
            model_name='mandatcategory',
            name='name_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Назавние'),
        ),
    ]
