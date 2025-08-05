from django.shortcuts import render
from django.http import HttpResponse

def studentDashboard(request):
    return render(request, 'StudentDashboard.html')
