from email import contentmanager
from re import template
from typing import List
from attr import fields
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from main.models import Income
# Create your views here.

class LoginPage(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirected_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    redirected_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('homee')
        return super(RegisterPage,self).get(*args,**kwargs)

class HomePage(ListView):
    model = Income
    template_name = 'main/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['home'] = context['home'].filter(user=self.request.user)

        return context