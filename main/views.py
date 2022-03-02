from django.urls import reverse_lazy
from django.db.models import Sum

from . import form

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.contrib.auth import login
from main.models import Income

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
        context['income'] = context['home'].filter(user=self.request.user,type_choice='in')
        context['expense'] = context['home'].filter(user=self.request.user,type_choice='ex')
        context['income_sum'] = context['home'].filter(user=self.request.user,type_choice='in').aggregate(Sum('amount'))['amount__sum']
        context['expense_sum'] = context['home'].filter(user=self.request.user,type_choice='ex').aggregate(Sum('amount'))['amount__sum']
        
        try:
            dat = Income.objects.get(title="Other Income")
            dat.delete()
        except:
            print("Other Income Not Found")
        
        try:
            dat2 = Income.objects.get(title="Other Expense")
            dat2.delete()
        except:
            print('Other Expense Not Found')

        try:
            income_sum = context['home'].filter(user=self.request.user,type_choice='in').aggregate(Sum('amount'))['amount__sum']
            expense_sum = context['home'].filter(user=self.request.user,type_choice='ex').aggregate(Sum('amount'))['amount__sum']
            if income_sum > expense_sum :
                balance_sum =  income_sum - expense_sum
                dat = Income(
                    user = self.request.user,
                    title = "Other Expense",
                    type_choice = 'ex',
                    amount = balance_sum
                )
                dat.save()      
            elif expense_sum > income_sum:
                balance_sum = expense_sum - income_sum
                dat = Income(
                    user = self.request.user,
                    title = "Other Income",
                    type_choice = 'in',
                    amount = balance_sum
                )
                print(dat.amount)
                dat.save()  
        except:
                print("Error from user" + str(self.request.user.id) + " No Data Found ")     


        return context
    
class Log(LoginRequiredMixin,ListView):
    model = Income
    template_name = 'main/log.html'
    context_object_name = 'log'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['log'] = context['log'].filter(user=self.request.user,type_choice='in', ).aggregate(Sum('amount'))
        return context


class AddIncome(CreateView):
    model = Income
    fields = {'title','amount','date','type_choice'}
    success_url = reverse_lazy('home')
    template_name = 'main/add_income.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddIncome, self).form_valid(form)


class EditTxn(LoginRequiredMixin,UpdateView):
    model = Income
    fields = {'title','amount','date','type_choice'}
    template_name = 'main/edit_income.html'
    success_url = reverse_lazy('home')

class DeleteTxn(LoginRequiredMixin,DeleteView):
    model = Income
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'main/delete_income.html'