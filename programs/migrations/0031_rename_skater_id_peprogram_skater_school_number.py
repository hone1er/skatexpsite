# Generated by Django 3.2.3 on 2022-01-08 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0030_peprogram_slc_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peprogram',
            old_name='skater_id',
            new_name='skater_school_number',
        ),
    ]
