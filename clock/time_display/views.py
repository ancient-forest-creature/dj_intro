from django.shortcuts import HttpResponse, redirect, render
from time import strftime
from datetime import datetime

def root(request):
    now = datetime.now()
    context = {
        "time": now.strftime("%Y-%m-%d %H:%M:%S")
    }

    return render(request, "index.html", context)

