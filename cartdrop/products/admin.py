from django.contrib import admin

from .models import (
    ACType,
    DisplayType,
    FashionSize,
    MobileVariant,
    OperatingSystem,
    Product,
    ProductAirConditionerFeature,
    ProductColor,
    ProductHighlight,
    ProductImages,
    ProductLaptopFeatures,
    ProductMobileFeatures,
    ProductRefrigeratorFeature,
    ProductSeries,
    ProductSpeakersFeatures,
    ProductSpecification,
    ProductTelivisionFeatures,
    ProductVariation,
    ProductWarranty,
    ProductWashingMachineFeatures,
    RefrigeratorType,
    ScreenType,
    SimType,
    SpeakerType,
    WashingMethod,
    LaptopVariant,
    TVVariant
)

# Register your models here.


@admin.register(SimType)
class SimeTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


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
    list_display = ("name", "subcategory", "brand", "seller")
    search_fields = ("name", "brand", "subcategory")
    list_select_related = ("brand", "subcategory")


@admin.register(DisplayType)
class DisplayTypeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(MobileVariant)
class MobileVariantAdmin(admin.ModelAdmin):

    list_display = ("__str__",)
    search_fields = ("name",)

@admin.register(LaptopVariant)
class LaptopVariantAdmin(admin.ModelAdmin):

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
    list_select_related = ("os",)


@admin.register(ProductLaptopFeatures)
class LaptopFeatureAdmin(admin.ModelAdmin):
    list_display = ("display_size", "display_type", "series", "os", "processor")
    list_filter = ("touchscreen", "os")
    list_select_related = ("os", "series")
    search_fields = ("os", "processor", "series")


@admin.register(ProductTelivisionFeatures)
class TelivisionFeatureAdmin(admin.ModelAdmin):
    list_display = ("display_size", "series", "is_3d", "is_curved", "has_wify")
    list_filter = ("is_3d", "is_curved", "has_wify")
    search_fields = ("series",)
    list_select_related = ("series",)


@admin.register(ProductWashingMachineFeatures)
class WashingMachineFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "energy_rating",
        "washing_capicity",
        "washing_method",
        "has_inbuilt_heater",
    )
    list_filter = ("has_inbuilt_heater",)


@admin.register(ProductAirConditionerFeature)
class AirConditionerFeatureAdmin(admin.ModelAdmin):
    list_display = ("type", "compressor", "series", "cooling_capacity")
    list_filter = ("type",)
    search_fields = ("series",)
    list_select_related = ("series", "type")


@admin.register(ProductRefrigeratorFeature)
class RefrigeratorFeatureAdmin(admin.ModelAdmin):

    list_display = ("type", "capacity", "energy_rating", "compressor_type")
    list_filter = ("stabilizer_required", "type")
    search_fields = ("type",)


@admin.register(ProductSpeakersFeatures)
class SpeakerFeatureAdmin(admin.ModelAdmin):
    list_display = ("type", "has_bluetooth", "frequency_response", "power_output")
    list_filter = ("has_bluetooth",)
    search_fields = ("type",)


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ("model_no", "model_name", "in_box", "launched_date")
    list_filter = ("launched_date",)
    search_fields = ("model_no", "model_name")


@admin.register(ProductWarranty)
class ProductWarrentyAdmin(admin.ModelAdmin):
    list_display = ("summary",)
    search_fields = ("summary",)


@admin.register(FashionSize)
class FashionSizeAdmin(admin.ModelAdmin):

    list_display = ("name", "code")
    search_fields = ("name", "code")
    list_editable = ("code",)


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "product", "retail_price", "price")
    list_filter = ("size", "color", "active")
    search_fields = ("product",)
    list_select_related = ("product", "mobile_variant", "laptop_variant", "color")


@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "image_summary",
        "primary",
        "image",
    )
    # search_fields = ('product_variation',)


@admin.register(ProductHighlight)
class ProductHighlightsAdmin(admin.ModelAdmin):
    list_display = ("product", "name")
    search_fields = ("name",)
    list_select_related = ("product",)


@admin.register(TVVariant)
class TVVariantAdmin(admin.ModelAdmin):
    list_display = ('display_size',)
    search_fields = ('display_size',)
    
