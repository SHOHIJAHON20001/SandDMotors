# Generated by Django 4.2.3 on 2023-07-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandDmotors', '0006_remove_galareya_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='galareya',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
