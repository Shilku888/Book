from django.shortcuts import render
from augapp.models import  Books
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Shilpi")


