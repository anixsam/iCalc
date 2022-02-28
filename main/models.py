from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=False,blank=False)
    title = models.CharField(null=False,blank=False,max_length=200)
    date = models.DateField()
    TYPE_CHOICES =  [('in','Income'),('ex','Expense')]
    type_choice = models.CharField(max_length=2,choices=TYPE_CHOICES,default='in')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']