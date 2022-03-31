from django.urls import path
from shop.views import shop,checkout,cart

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
]