from django.contrib import admin
from .models import Shops,Categories,Brands

@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    
admin.site.register(Categories)
admin.site.register(Brands)