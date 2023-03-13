from django.shortcuts import HttpResponse, redirect, render

from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse("placeholder to edit blog %s" % num)

def destroy(request, num):
    return redirect("/")

def package(request):
    return JsonResponse({"title":"My first blog", "content":"Lorem, ipsum dolor sit ament consectetur adipisicing elit."})

def names(request, name):
    context = {
        "name": name,
        "namelist":["Thor", "Odin", "Freya", "Sif", "Loki", "Freyr"]
    }

    return render(request, "index.html", context)

# Create your views here.
