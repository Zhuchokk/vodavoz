# Generated by Django 4.0 on 2022-08-15 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_marker_who'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='location',
            field=models.CharField(default='Не указано', max_length=80, verbose_name='место расположения'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='type',
            field=models.CharField(choices=[('HH', 'бытовая'), ('TL', 'туалетная'), ('DR', 'питьевая')], default='HH', max_length=2, verbose_name='ТИП'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='who',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='map.customuser', verbose_name='Кто'),
        ),
    ]
