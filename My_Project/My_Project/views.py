from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello, Uday welcome to django")
def home(request):
    return render(request, 'websites/index.html')
