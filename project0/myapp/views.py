from django.shortcuts import render
from django.http import HttpResponse

def LPU(request):
    a="LPU"
    return render(request, 'lpuhome.html', {"data" : a})

    # return HttpResponse("<h1> Good Morning LPU! </h1>")

# Create your views here.
