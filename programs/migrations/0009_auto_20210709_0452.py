# Generated by Django 3.2.3 on 2021-07-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_delete_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='price',
            new_name='cost',
        ),
        migrations.AddField(
            model_name='program',
            name='subtitle',
            field=models.CharField(default='', max_length=150),
        ),
    ]
