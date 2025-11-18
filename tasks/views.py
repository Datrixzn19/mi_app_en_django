from django.shortcuts import render

from django.shortcuts import render, redirect 

from django.http import HttpResponse

# Create your views here.

def prueba(request):
    #return  HttpResponse("working")
    return render(request, 'a.html')