from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y \n %H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)
