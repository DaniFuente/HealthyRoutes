# Generated by Django 3.0.5 on 2022-01-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0008_route_date_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
