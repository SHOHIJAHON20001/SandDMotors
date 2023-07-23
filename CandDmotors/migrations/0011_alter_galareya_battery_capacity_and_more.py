# Generated by Django 4.2.3 on 2023-07-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandDmotors', '0010_alter_galareya_battery_capacity_alter_galareya_motor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galareya',
            name='battery_capacity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='max_cruising_range',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='galareya',
            name='max_speed',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='galareya',
            name='motor',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='galareya',
            name='passangers',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
