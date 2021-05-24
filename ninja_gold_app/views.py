from django.shortcuts import render, redirect, HttpResponse

# def index(request):
#     return render(request, "index.html")

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    # request.session['counter'] += 1
    if request.method == "POST":
        # if 'name' == 'farm':
            request.session['counter'] += 5          
    return render(request, 'index.html')