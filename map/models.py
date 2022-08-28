from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        print('HERE')
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class CustomUser(AbstractUser):
    pass


class Marker(models.Model):
    HOUSEHOLD = 'HH'
    TOILET = 'TL'
    DRINK = 'DR'
    TYPE_OF_WATER = [
        (HOUSEHOLD, 'бытовая'),
        (TOILET, 'туалетная'),
        (DRINK, 'питьевая')
    ]

    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
    location = models.CharField('место расположения', max_length=80, default='Не указано')
    type = models.CharField('ТИП', max_length=2, choices=TYPE_OF_WATER, default=HOUSEHOLD)
    status = models.BooleanField('Есть ли вода?')
    date_of_update = models.DateTimeField('Дата обновления информации')
    who = models.ForeignKey(CustomUser, verbose_name='Кто', on_delete=models.SET_DEFAULT, default=CustomUser.objects.get(username='admin').pk)

    def __str__(self):
        water = ''
        for i in Marker.TYPE_OF_WATER:
            if i[0] == self.type:
                water = i[1]

        return '{0}, {1} вода. Обновлено {2} пользователем {3}'.format(self.location, water, self.date_of_update.strftime('%Y-%m-%d %H:%M'), self.who)

