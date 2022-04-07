from django.contrib import admin
from .models import Shops
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

admin.site.register(Shops)