from django.urls import path
from shop.views import shop,checkout,cart,shop_detail,wishlist

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
    path('<slug:slug>', shop_detail, name='shop_detail'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
]