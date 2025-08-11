from django.shortcuts import render

def all_chai(request):
    return render(request, 'chai/all_chai.html')
def Chaistore(request):
    return render(request, 'chai/chaistore.html')