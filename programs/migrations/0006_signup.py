# Generated by Django 3.2.3 on 2021-06-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_remove_program_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
