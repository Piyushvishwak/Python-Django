from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Hello world. I am learning Django.</h1>")

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')
