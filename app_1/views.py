from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app_2.models import Company
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'app_1/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                companys = Company.objects.all()
                context['companys'] = companys
                return render(request, 'app_2/index.html', context)
        return render(request, 'app_1/login.html', context)

class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'app_1/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return render(request, 'app_2/index.html')
        return render(request, 'app_1/registration.html', {'form': form})
