# Generated by Django 3.2.3 on 2021-08-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0023_auto_20210823_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('amount_off', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]