# Generated by Django 3.2.3 on 2022-12-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_staff_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(max_length=75),
        ),
    ]