from django.urls import path
from shop.views import checkout,updateItem,shop_detail,wishlist,shop,cart

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
    path('<slug:slug>', shop_detail, name='shop_detail'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
]