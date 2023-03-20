from django.shortcuts import HttpResponse, redirect, render

def reg(request):
    return HttpResponse("placeholder for users to create a new user record")

def index(request):
    return HttpResponse("placeholder for users to log in")

def show(request):
    return HttpResponse("placeholder to later display the list of all users")
