# Generated by Django 3.0.5 on 2021-12-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_stations', '0005_auto_20211226_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='airstation',
            name='town_id',
            field=models.IntegerField(null=True),
        ),
    ]
