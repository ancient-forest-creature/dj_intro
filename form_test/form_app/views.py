from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def create_user(request):
    # print("got Post Info..............")
    # print(request.POST)
    name = request.POST['name']
    email = request.POST['email']
    # print(name)
    # print(email)
    context = {
        "temp_name":name,
        "temp_email":email
    }
    return redirect("/success")

def success(request):
    return render(request, "success.html")