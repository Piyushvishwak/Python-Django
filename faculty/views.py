from django.shortcuts import render
from django.http import HttpResponse
def facultyDashboard(request):
    return render(request, 'facultyDashboard.html')

