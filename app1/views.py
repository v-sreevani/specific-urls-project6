from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def dhoni(request):
    return HttpResponse('<h1>MS dhoni is a best finisher</h1>')

def raina(request):
    return HttpResponse('<h1><marquee> raina ia known as MR.IPL</marquee></h1>')
