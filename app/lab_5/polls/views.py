from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
#Access model object  and templates for response

    return HttpResponse('Hello World')

