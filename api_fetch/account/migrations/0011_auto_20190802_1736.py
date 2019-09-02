# Generated by Django 2.0.2 on 2019-08-02 12:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20190802_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='uid',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='visitor_perma',
            name='uid',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]