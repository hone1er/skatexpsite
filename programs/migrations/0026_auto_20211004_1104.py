# Generated by Django 3.2.3 on 2021-10-04 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0025_auto_20210823_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotdogger',
            old_name='student_address',
            new_name='parent_address',
        ),
        migrations.RenameField(
            model_name='peprogram',
            old_name='student_address',
            new_name='parent_address',
        ),
    ]
