# Generated by Django 3.0.5 on 2022-01-23 12:13

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0010_auto_20220123_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
