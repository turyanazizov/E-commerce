from django.shortcuts import render

def shop(request):
    return render(request,'shop.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'shopping-cart.html')