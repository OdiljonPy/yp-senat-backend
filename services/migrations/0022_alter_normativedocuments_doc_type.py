# Generated by Django 5.1.2 on 2024-12-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_alter_management_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normativedocuments',
            name='doc_type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('DOCX', 'Word'), ('XLS', 'Excel')], editable=False, max_length=5, verbose_name='тип документа'),
        ),
    ]
