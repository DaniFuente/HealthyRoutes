# Generated by Django 3.0.5 on 2022-01-08 16:36

from django.db import migrations, models
import djongo.models.fields
import routes.models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_node_routeranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='distance',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='nodes',
            field=djongo.models.fields.ArrayField(model_container=routes.models.Node, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='ranking_puntuation',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='end_latitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='end_longitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='init_latitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='init_longitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='routes',
            field=djongo.models.fields.ArrayField(model_container=routes.models.Route, null=True),
        ),
        migrations.AddField(
            model_name='routeranking',
            name='variation',
            field=models.DecimalField(decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='air_quality',
            field=models.IntegerField(null=True),
        ),
    ]