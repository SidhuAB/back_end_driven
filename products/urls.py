from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.prod_page,name='prod_page')
]
