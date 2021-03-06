from unicodedata import name
from .views import AddIncome, Log, LoginPage,HomePage, RegisterPage, DeleteTxn, EditTxn
from django.urls import  path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('',HomePage.as_view(),name='home'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('addincome/',AddIncome.as_view(),name='addincome'),
    path('log/',Log.as_view(),name='log'),
    path('edit/<int:pk>/',EditTxn.as_view(),name="edit"),
    path('delete/<int:pk>/',DeleteTxn.as_view(),name="delete")
]