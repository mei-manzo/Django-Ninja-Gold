from django.shortcuts import render, redirect, HttpResponse

# def index(request):
#     return render(request, "index.html")

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return render(request, 'index.html')