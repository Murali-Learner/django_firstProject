from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'user':'Sai'})
    
def login(request):
    return render(request,'login.html')