from django.contrib import admin

from .models import Product, ProductColor, DisplayType, MobileVariant, OperatingSystem, ScreenType, DryerType, ACType, ProductSeries, RefrigeratorType, SpeakerType, ProductMobileFeatures

# Register your models here.
    
@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "active")
    list_filter = ("active",)
    list_editable = ("price",)
    search_fields = ("name",)


@admin.register(DisplayType)
class DisplayTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(MobileVariant)
class MobileVariantAdmin(admin.ModelAdmin):

    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)


@admin.register(ScreenType)
class SereenTypeAdmin(admin.ModelAdmin):

    list_display = ('__str__',)
    search_fields = ("name",)


@admin.register(DryerType)
class DryerTypeAdmin(admin.ModelAdmin):

    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(ACType)
class ACTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)

    
@admin.register(ProductSeries)
class ProductSeries(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(RefrigeratorType)
class RefrigratorTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(SpeakerType)
class SpeakerTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ("name",)

@admin.register(ProductMobileFeatures)
class MobileFeaturesAdmin(admin.ModelAdmin):
    list_display = ('os', 'variant', 'display_size', 'display_type', 'resolution', 'sim_type', 'battery_capicity')
    list_filter = ('touchscreen', 'smart_phone', 'os')
    search_fields = ('sim_type', 'variant')
    list_select_related = ('variant',)
    