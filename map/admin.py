from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Marker


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'password',]


class MarkerAdmin(admin.ModelAdmin):
    list_display = ['location', 'type', 'status', 'date_of_update', 'who']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Marker, MarkerAdmin)