# Generated by Django 3.2.3 on 2021-07-13 19:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='customer',
            name='student_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
