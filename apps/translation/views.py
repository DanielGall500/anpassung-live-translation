from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Live translation from English to German.")