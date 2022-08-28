from django.urls import include, path
from .views import UserMap, Info, LoginForm, EditForm

urlpatterns = [
    path('', UserMap.as_view(), name='UserMap'),
    path('info/', Info.as_view(), name='Info'),
    path('login/', LoginForm.as_view(), name='LoginForm'),
    path('edit/', EditForm.as_view(), name='EditForm')
]