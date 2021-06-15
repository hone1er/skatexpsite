# Generated by Django 3.2.3 on 2021-06-15 06:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_rename_description_staff_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='content',
        ),
        migrations.AddField(
            model_name='staff',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
