from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=False,blank=False)
    title = models.CharField(null=False,blank=False,max_length=200)
    description = models.TextField(null=True,blank=False)
    date = models.DateTimeField()

