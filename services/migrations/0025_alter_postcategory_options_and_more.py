# Generated by Django 5.1.2 on 2024-12-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_merge_20241203_0255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'ordering': ('-created_at',), 'verbose_name': 'Категория постов', 'verbose_name_plural': 'Категории постов'},
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='facebook',
            field=models.URLField(default='facebook.com', verbose_name='фэйсбук_url'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='linkedin',
            field=models.URLField(default='linkedin.com', verbose_name='линкедин_url'),
        ),
        migrations.AlterField(
            model_name='commissionmember',
            name='twitter',
            field=models.URLField(default='twitter.com', verbose_name='твиттер_url'),
        ),
    ]
