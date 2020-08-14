from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.prod_page,name='prod_page')
]
admin.site.site_header = 'Premium Wallet'
admin.site.index_title = 'Admin_Page'
admin.site.site_title = 'Premium Wallet' 