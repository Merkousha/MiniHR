from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def report(request):
    return render(request,'report.html')