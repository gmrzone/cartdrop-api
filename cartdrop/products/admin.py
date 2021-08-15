from django.contrib import admin

from .models import (ACType, DisplayType, MobileVariant, OperatingSystem,
                     Product, ProductColor, ProductMobileFeatures,
                     ProductSeries, RefrigeratorType, ScreenType, SpeakerType,
                     WashingMethod)

# Register your models here.


@admin.register(WashingMethod)
class WashingMethodAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(DisplayType)
class DisplayTypeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(MobileVariant)
class MobileVariantAdmin(admin.ModelAdmin):

    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(ScreenType)
class SereenTypeAdmin(admin.ModelAdmin):

    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(ACType)
class ACTypeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(ProductSeries)
class ProductSeries(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(RefrigeratorType)
class RefrigratorTypeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(SpeakerType)
class SpeakerTypeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(ProductMobileFeatures)
class MobileFeaturesAdmin(admin.ModelAdmin):
    list_display = (
        "os",
        "display_size",
        "display_type",
        "resolution",
        "sim_type",
        "battery_capicity",
    )
    list_filter = ("touchscreen", "smart_phone", "os")
    search_fields = ("sim_type", "variant")
    list_select_related = ("variant",)
