from django.contrib import admin
from .models import Shops,Categories,Brands,Order,OrderItem

@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('category', 'title')
    list_display_links = list_display
    list_filter = ('category', 'brand','price')


admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Order)
admin.site.register(OrderItem)
