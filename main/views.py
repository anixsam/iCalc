from msilib import type_binary
from django.urls import reverse_lazy

from . import form

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

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
    form_class = form.UserCreationForm
    redirected_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage,self).get(*args,**kwargs)

class HomePage(LoginRequiredMixin,ListView):
    model = Income
    template_name = 'main/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['home'] = context['home'].filter(user=self.request.user)
        return context
    

class AddIncome(CreateView):
    model = Income
    fields = {'title','amount','date'}
    success_url = reverse_lazy('home')
    template_name = 'main/add_income.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddIncome, self).form_valid(form)