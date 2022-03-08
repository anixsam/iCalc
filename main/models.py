
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES =  [('in','Income'),('ex','Expense')]
CRON_TYPE = [('m','Monthly'),('w','Weekly'),('d','Daily')]

class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=False,blank=False)
    title = models.CharField(null=False,blank=False,max_length=200)
    date = models.DateField(default=now)
    type_choice = models.CharField(max_length=10,choices=TYPE_CHOICES,default='ex',verbose_name= 'Income or Expense')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']


class ScheduledIncomeExpense(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=False,blank=False)
    title = models.CharField(null=False,blank=False,max_length=200)
    date = models.DateField(default=now)
    cron_type = models.CharField(max_length=10,choices=CRON_TYPE,default='m',verbose_name= 'Scheduled Income or Expense')
    type_choice = models.CharField(max_length=10,choices=TYPE_CHOICES,default='ex',verbose_name= 'Income or Expense')

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['-date']