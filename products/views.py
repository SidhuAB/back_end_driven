from django.shortcuts import render
from .models import Policy

# Create your views here.

def prod_page(request):

    pol = Policy.objects.all()
  #  print(pol.name)
    return render(request,'prod_page.html',{'pol':pol})
 