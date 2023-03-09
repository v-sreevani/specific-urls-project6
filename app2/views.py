from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1><marquee> virat is best batsman</marquee></h1>')

def abcd(request):
    return HttpResponse('<h1> ABCD is MR 360,he is monster</h1>')
