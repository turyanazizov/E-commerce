from django.contrib import admin
from .models import Blogs, Comments

admin.site.register(Comments)

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)