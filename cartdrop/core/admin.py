from django.contrib import admin

from .models import (Brand, CategoryImage, CouponCode, ProductCategory,
                     ProductSubcategory, SubcategoryImage, UserCouponIntermidiary)

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
    list_display = ("name",)
    search_fields = ("__str__",)


@admin.register(CouponCode)
class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "discount", "valid_from", "valid_to")
    list_filter = ("active",)
    list_editable = ("discount", "valid_from", "valid_to")


@admin.register(UserCouponIntermidiary)
class UserCouponIntermidiaryTable(admin.ModelAdmin):
    list_display = ("user", "coupon", "created", "updated")
    list_filter = ("created",)
    
