# Generated by Django 3.2.3 on 2022-12-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_rename_description_staff_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=101),
        ),
    ]
