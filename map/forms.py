from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Marker
from django.utils import timezone

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='никнейм')
    password = forms.CharField(label='пароль')


class MarkerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if kwargs.get('initials'):
            for key in self.declared_fields.keys():
                self.declared_fields[key].initial = kwargs['initials'][key]
            del kwargs['initials']
        super(MarkerForm, self).__init__(*args, **kwargs)



    id = forms.IntegerField()
    longitude = forms.FloatField(label='Долгота')
    latitude = forms.FloatField(label='Широта')
    location = forms.CharField(label='место расположения', max_length=80)
    type = forms.ChoiceField(choices=Marker.TYPE_OF_WATER, label='тип')
    status = forms.BooleanField(label='Есть ли вода?', required=False)
    date_of_update = forms.DateTimeField(label='Дата обновления информации')

