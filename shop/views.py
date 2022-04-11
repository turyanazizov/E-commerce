from multiprocessing import context
from operator import concat
from urllib import response
from django.shortcuts import get_object_or_404, render
from .models import Shops,Categories,Brands

def shop(request):
    shops=Shops.objects.all()
    categories=Categories.objects.all()
    brands=Brands.objects.all()
    shop_id=request.POST.get('shop_id')
    context={
        'shops':shops,
        'categories':categories,
        'brands':brands,
    }
    response=render(request,'shop.html',context=context)
    liked_shops=request.COOKIES.get('liked_shops','')
    if request.method =='POST' and shop_id not in liked_shops:
        response.set_cookie('liked_shops', f'{liked_shops}{shop_id} ')
    if request.method =='POST' and shop_id in liked_shops:
        response.set_cookie('liked_shops', liked_shops.replace(shop_id,''))
    return response

def shop_detail(request,slug):
    shop = get_object_or_404(Shops, slug=slug)
    shops=Shops.objects.all().filter(category=shop.category).exclude(title=shop.title)
    context = {
        'shop':shop,
        'shops':shops,
    }
    return render(request,'shop-details.html',context=context)

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'shopping-cart.html')

def wishlist(request):
    liked_shops=request.COOKIES.get('liked_shops','')
    shop_id=request.POST.get('shop_id')
    l_shops=liked_shops.split(' ')
    indexes=[]
    for num in l_shops:
        if num:
            indexes.append(int(num))
    shops=Shops.objects.all()
    wished_shops=[]
    for index in indexes:
        if shops.filter(id=index):
            wished_shops.append(shops.filter(id=index))
    total=0
    for shops in wished_shops:
        for shop in shops:
            total+=shop.price
    context={
        'wished_shops':wished_shops,
        'total':total,
    }
    response = render(request,'wishlist.html',context=context)
    if request.method =='POST' and shop_id in liked_shops:
        response.set_cookie('liked_shops', liked_shops.replace(shop_id,''))
        return response
    return response