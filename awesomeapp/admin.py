from django.contrib import admin
from awesomeapp.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category",)
    search_fields = ("name",)