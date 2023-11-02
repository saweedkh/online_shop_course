from django.contrib import admin

from .models import Product

# Register your models here.

@admin.register(Product)
class ProDuctAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active')