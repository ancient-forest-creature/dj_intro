from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def results(request):
    # print("got Post Info..............")
    # print(request.POST)
    # name = request.POST['name']
    # dojo = request.POST['dojo']
    # print(name)
    # print(email)
    context = {
        "form_name":request.POST['name'],
        "form_dojo":request.POST['dojo'],
        "form_lang":request.POST['lang'],
        "form_comment":request.POST['comment'],
    }
    return render(request, "results.html", context)
