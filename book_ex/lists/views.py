from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePageView(request):
    return HttpResponse('<html><title>To-do list</title></html>')
