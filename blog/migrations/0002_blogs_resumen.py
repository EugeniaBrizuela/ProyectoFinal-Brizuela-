# Generated by Django 4.0.3 on 2022-04-18 13:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='resumen',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
