# Generated by Django 4.2.3 on 2023-07-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandDmotors', '0009_alter_galareya_battery_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galareya',
            name='battery_capacity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='motor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]