from django.shortcuts import render, redirect
import random
from time import strftime
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        print(request.session['gold'])
        request.session['activity'] = []
    return render(request, 'index.html')

def process_money(request):
    dtn = datetime.now()
    now = dtn.strftime("%Y-%m-%d %H:%M:%S")
    print(type(request.POST['name']))
    if request.POST['name'] == 'farm':
        turn = random.randint(10,20)
        request.session['gold'] += turn
        request.session['activity'].append(f"<p class='text-succsss'>Earned {turn} from the cave! ({now}) </p>")
    elif request.POST['name'] == 'cave':
        turn = random.randint(5,10)
        request.session['gold'] += turn
        request.session['activity'].append(f"<p class='text-succsss'>Earned {turn} from the farm! ({now}) </p>")
    elif request.POST['name'] == 'house':
        turn = random.randint(2,5)
        request.session['gold'] += turn
        request.session['activity'].append(f"<p class='text-succsss'>Earned {turn} from the house! ({now}) </p>")
    else:
        turn = random.randint(-50,50)
        request.session['gold'] += turn
        if turn > -1:
            request.session['activity'].append(f"<p class='text-succsss'>Gambled at the casino and won {turn}! Hazza! ({now}) </p>")
        else:
            request.session['activity'].append(f"<p class='text-danger'>Gambled at the casino and lost {turn}...Ouch! ({now}) </p>")
    return redirect('/')

def killit(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')