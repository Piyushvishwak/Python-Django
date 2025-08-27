from django.shortcuts import render
from django.http import HttpResponse
def tweet_list(request):
    return HttpResponse("This is the tweet list response.")
