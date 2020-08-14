from django.shortcuts import render
from .models import Policy

# Create your views here.

def prod_page(request):

    pol = Policy.objects.all()
    return render(request,'prod_page.html',{'pol':pol})
 