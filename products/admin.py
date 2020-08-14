from django.contrib import admin
from .models import Policy
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.

admin.site.register(Policy)

