# Generated by Django 5.1.2 on 2024-10-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_ipaddress_options_alter_ipaddress_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
                ('ip', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'Ip адрес',
                'verbose_name_plural': 'Ip адресы',
                'ordering': ('created_at',),
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='views_count',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, to='services.visitors', verbose_name='количество просмотров'),
        ),
        migrations.DeleteModel(
            name='IpAddress',
        ),
    ]
