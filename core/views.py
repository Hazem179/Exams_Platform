from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'core/home.html')


def exams(request):
    if request.method == "POST":
        print(request.POST)
    return render(request,'core/exams.html')

def questions(request):
    return render(request,'core/questions.html')