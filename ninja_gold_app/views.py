from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from pytz import timezone
import random, pytz

# def index(request):
#     return render(request, "index.html")

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0  
        request.session['activities'] = []     
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'POST':
        myGold = request.session['gold']
        activities = request.session['activities']
        place = request.POST['place']
        if place == 'farm':
            gold_amount = round(random.random() * 10 + 10)
        elif place == 'cave':
            gold_amount = round(random.random() * 5 + 10)
        elif place == 'house':
            gold_amount = round(random.random() * 3 + 2)
        else: 
            win_lose = round(random.random())
            if win_lose == 1:
                gold_amount = round(random.random()*50)
            else:
                gold_amount = (round(random.random()*50)*-1)
        date_format='%m/%d/%Y %H:%M:%S %Z'
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        myTime = date.strftime(date_format)

        myGold += gold_amount
        request.session['gold'] = myGold

        if gold_amount>= 0:
            str = f"Earned {gold_amount} from the {place} {myTime}"
        else:
            str = f"Lost {gold_amount} from the {place} {myTime}"
        activities.append(str)
        request.session['activities'] = activities
    return redirect('/')