from django.shortcuts import render

def cart(request):
    return render(request, 'cart.html')

def games(request):
    return render(request, 'games.html')

def platform(request):
    return render(request, 'platform.html')
