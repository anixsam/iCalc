from unicodedata import name
from .views import LoginPage,HomePage, RegisterPage
from django.urls import  path

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('',HomePage.as_view(),name='home'),
    path('register/',RegisterPage.as_view(),name='register')
]