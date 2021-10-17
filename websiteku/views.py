from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def profile(request):
    return HttpResponse("<h1>Ini adalah Page Profile</h1>")