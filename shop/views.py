from django.shortcuts import get_object_or_404, render
from .models import Shops,Categories,Brands
import math

def shop(request):
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page = 1
    per_count=9
    all_shops=Shops.objects.all().count()
    total_page_count = math.ceil( all_shops / per_count )
    shops=Shops.objects.all()[per_count*(page-1):(page*per_count)]
    previous_page = page - 1 if not page == 1 else page
    next_page = page + 1 if not page == total_page_count else page
    page_range = range(1, total_page_count + 1)
    current_page = page
    to=per_count*current_page
    frm=per_count*current_page-per_count
    if frm==0:
        frm=1
    if to>all_shops:
        to=all_shops

    # shops=Shops.objects.all()
    categories=Categories.objects.all()
    brands=Brands.objects.all()
    shop_id=request.POST.get('shop_id')

    cat_id=request.GET.get('categories')
    if cat_id:
        shops=Shops.objects.all().filter(category=cat_id)
    brand_id=request.GET.get('brands')
    if brand_id:
        shops=Shops.objects.all().filter(brand=brand_id)
    
    price=request.GET.get('price')
    if price:
        values_str=price.split('-')
        values=[]
        for value in values_str:
            values.append(int(value))
        shops=Shops.objects.all().filter(price__gte=values[0]).filter(price__lte=values[1])
# Problem : Filter edende Pagination-da 2,3 ve s. sehifelere tesir etmir..... 
    context={
        'frm':frm,
        'all_shops':all_shops,
        'to':to,
        'current_page': current_page,
        'previous_page': previous_page,
        'next_page': next_page, 
        'page_range': page_range,
        'shops':shops,
        'categories':categories,
        'brands':brands,
    }
    response=render(request,'shop.html',context=context)
    liked_shops=request.COOKIES.get('liked_shops','')
    if request.method =='POST' and shop_id not in liked_shops:
        response.set_cookie('liked_shops', f'{liked_shops}{shop_id} ')
    elif request.method =='POST' and shop_id in liked_shops:
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
