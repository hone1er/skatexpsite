# Generated by Django 3.2.3 on 2021-07-25 23:00

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0019_alter_customer_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('parent_email', models.EmailField(max_length=254)),
                ('student', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('student_grade', models.CharField(max_length=20)),
                ('student_address', models.CharField(max_length=254)),
                ('student_id', models.CharField(max_length=254)),
                ('food_program', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Hotdogger',
        ),
    ]
