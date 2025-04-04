from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("2200032362 - Ch. Chandra Sekhar Reddy from AWS S02 DA Section")
def about(request):
    return HttpResponse("About Page")
def demo(request):
    return HttpResponse("Welcome to Demo Page")

def test(request):
    return render(request,"index.html")