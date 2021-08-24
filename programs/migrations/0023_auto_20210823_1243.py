# Generated by Django 3.2.3 on 2021-08-23 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0022_auto_20210817_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotdogger',
            name='coupon',
            field=models.CharField(default='null', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peprogram',
            name='coupon',
            field=models.CharField(default='no coupon', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotdogger',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='peprogram',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
