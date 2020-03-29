# Generated by Django 3.0.4 on 2020-03-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0002_auto_20200329_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='day',
            field=models.PositiveSmallIntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='poem',
            name='month',
            field=models.PositiveSmallIntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='poem',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, max_length=4, null=True),
        ),
    ]
