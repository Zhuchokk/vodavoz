from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import FormView
from .forms import CustomUserLoginForm, MarkerForm
from .models import Marker, CustomUser
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.utils import timezone


from django.http import Http404
# from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin

class UserMap(TemplateView):
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        context = super(UserMap, self).get_context_data(**kwargs)

        context.update({'markers': Marker.objects.all()})
        return context



class Info(View):

    def get(self, request):
        return render(request, 'map/info.html')


class LoginForm(FormView):
    template_name = 'map/login.html'
    form_class = CustomUserLoginForm
    success_url = '/edit/'

    def form_valid(self, form):
        print('NOW!')
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(self.request, user)
            return super(LoginForm, self).form_valid(form)
        else:
            form.add_error(None, 'Неверный логин или пароль')
            return super(LoginForm, self).form_invalid(form)


class CheckEditForm(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # return self.get(request)
            return EditForm.as_view
        else:
            return redirect("LoginForm")


class EditForm(ListView, FormView):
    model = Marker
    template_name = 'map/edit.html'
    form_class = MarkerForm

    def get_queryset(self):
        print(6789)
        objects = {}
        user = self.request.user
        # user = authenticate(username=data['username'], password=data['password'])

        markers = Marker.objects.filter(who=user.pk)
        objects[user.username] = []

        for marker in markers:
            data = {}

            for key in MarkerForm.declared_fields.keys():
                data[key] = getattr(marker, key)

            f = MarkerForm(initials=data)
            objects[user.username].append(f)


        for key, value in objects.items():
            print(key)
            for f in value:
                for k in f.declared_fields.keys():
                    print(f.declared_fields[k].initial)



        return objects.items()

    def form_valid(self, form):
        print(dir(form))
        print(dir(self.post))
        if self.request.POST.get('save'):

            data = form.cleaned_data
            print(data)
            m = Marker.objects.get(pk=data['id'])
            # for key in data.keys():
            #     if key != 'id':
            #         o = getattr(m, key)
            #         o = data[key]
            m.latitude = data['latitude']
            m.longitude = data['longitude']
            m.location = data['location']
            m.status = data['status']
            m.date_of_update = timezone.now()
            m.save()

        else:
            data = form.cleaned_data
            m = Marker.objects.get(pk=data['id'])
            m.delete()
            print('del')
        return super(EditForm, self).form_valid(form)

    def get_success_url(self):
        return reverse('EditForm')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("LoginForm")
        return super(EditForm, self).dispatch(request, *args, **kwargs)
