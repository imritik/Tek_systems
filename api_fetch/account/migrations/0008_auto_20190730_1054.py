# Generated by Django 2.0.2 on 2019-07-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190729_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='temp',
            name='whoto',
        ),
        migrations.RemoveField(
            model_name='visitor_perma',
            name='whoto',
        ),
    ]