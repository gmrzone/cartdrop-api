from django.contrib import admin

from .models import ProductCategory, ProductSubcategory, CategoryImage

# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_filter = ('category',)

@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
