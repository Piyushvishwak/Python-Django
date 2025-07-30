from django.http import HttpResponse
def hello_print(request):
    return HttpResponse("<h1>Hello there! I am learning Django.</h1>")