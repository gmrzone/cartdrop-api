from django.contrib import admin

from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "active")
    list_filter = ("active",)
    list_editable = ("price",)
    search_fields = ("name",)
