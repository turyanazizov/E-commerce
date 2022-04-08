from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Shops,Categories,Brands

def shop(request):
    shops=Shops.objects.all()
    categories=Categories.objects.all()
    brands=Brands.objects.all()
    context={
        'shops':shops,
        'categories':categories,
        'brands':brands,
    }
    return render(request,'shop.html',context=context)

def shop_detail(request,slug):
    shop = get_object_or_404(Shops, slug=slug)
    context = {
        'shop':shop,
    }
    return render(request,'shop-details.html',context=context)

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'shopping-cart.html')