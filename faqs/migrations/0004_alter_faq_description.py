# Generated by Django 5.0.2 on 2024-03-12 20:13

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0003_alter_faq_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]
