from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_home(request):
    return render(request, 'Home.html')


def display_feh(request):
    return render(request, 'FeHtml.html')
