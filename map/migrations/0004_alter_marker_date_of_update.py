# Generated by Django 4.0 on 2022-08-25 17:33

from django.db import migrations
import map.models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_marker_location_alter_marker_type_alter_marker_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='date_of_update',
            field=map.models.CustomDateTimeField(verbose_name='Дата обновления информации'),
        ),
    ]
