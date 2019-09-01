# Generated by Django 2.0.2 on 2019-08-31 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190807_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='dob',
            field=models.CharField(default='05-05-1996', max_length=200),
        ),
        migrations.AlterField(
            model_name='temp',
            name='uid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor_perma',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='visitor_perma',
            name='dob',
            field=models.CharField(default='05-05-1996', max_length=200),
        ),
        migrations.AlterField(
            model_name='visitor_perma',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='visitor_perma',
            name='uid',
            field=models.CharField(max_length=50),
        ),
    ]