from django.shortcuts import render, redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] = int(request.session['count']) + 1
    else:
        request.session['count'] = 1
        
    if 'added' in request.session:
        request.session['added'] = int(request.session['added']) + 1
    else:
        request.session['added'] = 1
    return render(request, 'index.html')

def addtwo(request):
    request.session['added'] = int(request.session['added']) + 2
    return redirect('/')

def addsome(request):
    request.session['added'] = int(request.session['added']) + int(request.POST['some'])
    return redirect('/')

def killit(request):
    del request.session['count']
    del request.session['added']
    return redirect('/')
