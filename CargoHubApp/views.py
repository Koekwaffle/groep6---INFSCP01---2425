from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action


def say_hello(request):
    # pull data
    # Transform data
    # send mail
    return HttpResponse("Hello World")