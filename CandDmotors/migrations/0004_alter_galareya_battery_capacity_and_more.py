# Generated by Django 4.2.3 on 2023-07-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandDmotors', '0003_galareya_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galareya',
            name='battery_capacity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='gibrid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='max_cruising_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='max_speed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='motor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='passangers',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
