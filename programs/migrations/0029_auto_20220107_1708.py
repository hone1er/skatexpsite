# Generated by Django 3.2.3 on 2022-01-08 01:08

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0028_auto_20211006_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peprogram',
            name='parent_address',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='skater_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='skater_grade',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='skater_id',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='skater_phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
