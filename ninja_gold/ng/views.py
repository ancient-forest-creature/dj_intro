from django.shortcuts import render, redirect
import random, datetime
# from time import strftime
# from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        print(request.session['gold'])
        request.session['activity'] = ""
    return render(request, 'index.html')

def process_money(request):
    location = request.POST['location']
    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print(type(request.POST['location']))
    if location == 'farm':
        turn = random.randint(10,20)
    elif location == 'cave':
        turn = random.randint(5,10)
    elif location == 'house':
        turn = random.randint(2,5)
    else:
        turn = random.randint(-50,50)
    request.session['gold'] += turn
    if turn >= 0:
         new_msg = f"<p class='text-success'>You won {turn} gold from {location}! Hazza! ({now}) </p>"
    else:
         new_msg = f"<p class='text-danger'>Bad luck! You lost {turn} gold from {location}...Ouch! ({now}) </p>"
    request.session['activity'] += new_msg
    return redirect('/')

def killit(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')