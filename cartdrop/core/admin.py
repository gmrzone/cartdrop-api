from django.contrib import admin

from .models import CategoryImage, ProductCategory, ProductSubcategory, Brand, SubcategoryImage

# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ("category",)
    list_filter = ("category",)


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

@admin.register(SubcategoryImage)
class SubcategoryImageAdmin(admin.ModelAdmin):
    list_display = ("subcategory",)
    list_filter = ("subcategory",)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('__str__',)
