from django.contrib import admin
from .models import About

@admin.register(About)
class AuthorAdmin(admin.ModelAdmin):
    # to disbale add functionality
    def has_add_permission(self, request):
        return False

    # to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False