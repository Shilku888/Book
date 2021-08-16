from django.shortcuts import render
from augapp.models import  Books
from django.http import HttpResponse
from augapp.forms import BooksForm,AuthorForm

# Create your views here.
def home(request):
    return HttpResponse("Hello Shilpi")

def form(request):
    #return HttpResponse("Hello Shilpi")
    if(request.method == "POST"):
        formdata = BooksForm(request.POST)
        if formdata.is_valid():
            formdata.save()

    return render(request,'form.html',{"BooksForm":BooksForm,},)
