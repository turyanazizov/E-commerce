from django.urls import path
from shop.views import checkout,cart,shop_detail,wishlist,shop,ShopDeleteView

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
    path('<slug:slug>', shop_detail, name='shop_detail'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('delete/<int:pk>', ShopDeleteView.as_view(),name='delete'),
]