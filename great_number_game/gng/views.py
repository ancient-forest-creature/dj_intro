from django.shortcuts import render, redirect
import random

def index(request):
    if 'num' not in request.session:
        request.session['num'] = random.randint(1,100)
        print(request.session['num'])
        request.session['num_guess'] = 0
        request.session['display'] = True
    return render(request, 'index.html')

def guess(request):
    print(type(request.POST['guess']))
    if request.POST['guess'] != '':
        guess = int(request.POST['guess'])
        print(f'guess is: {guess}')
        # print(type(guess))
        # print(type(request.session['num']))
    else:
        guess = ''
    request.session['num_guess'] += 1
    print(f'num_guess is {request.session["num_guess"]}')
    if guess != "" and guess > 0 and guess < 101:
        request.session['guess'] = int(request.POST['guess'])
        if 'error' in request.session:
            del request.session['error']
    else:
        request.session['error'] = "You must put in a value between 1 & 100"
    if request.session['num_guess'] > 4:
        request.session['display'] = False
    if request.session['guess'] == request.session['num']:
        request.session['display'] = False
    return redirect('/')

def killit(request):
    del request.session['num']
    del request.session['guess']
    del request.session['num_guess']
    del request.session['display']
    return redirect('/')