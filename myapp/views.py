from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(
        request, 'index.html',
    )

def Contactus(request):
    return render(
        request, 'contact.html'
    )

def Courses(request):
    return render(
        request, 'courses.html'
    )

def About(request):
    return render(
        request, 'aboutus.html',
    )    

def add(request):
    fn=request.GET['fname']
    ln=request.GET['lname']

    return render(
        request, 'result.html',{'result':fn +" "+ ln}
    )



