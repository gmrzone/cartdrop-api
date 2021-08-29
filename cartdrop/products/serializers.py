from django.db import models
from rest_framework.fields import ImageField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from cartdrop.accounts.serializers import SellerUserSerializer
from cartdrop.core.serializers import BrandSerializer, ProductSubcategorySerializer, ProductSubcategoryBase

from .models import (
    ACCapacityVariant,
    ACStarRatingVariant,
    ACType,
    BookVariant,
    DisplayType,
    FashionSize,
    LaptopVariant,
    MobileVariant,
    OperatingSystem,
    Product,
    ProductAirConditionerFeature,
    ProductColor,
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
    TVVariant,
    WashingMethod,
)


class ProductColorSerializere(ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ("name", "slug")


class MobileVariantSerializer(ModelSerializer):
    class Meta:
        model = MobileVariant
        fields = ("name",)


class LaptopVariantSerializer(ModelSerializer):
    class Meta:
        model = LaptopVariant
        fields = ("name",)


class TVVariantSerializer(ModelSerializer):
    class Meta:
        model = TVVariant
        fields = ("display_size",)


class ACCapacityVariantSerializer(ModelSerializer):
    class Meta:
        model = ACCapacityVariant
        fields = ("capacity",)


class ACStarRatingVariantSerializer(ModelSerializer):
    class Meta:
        model = ACStarRatingVariant
        fields = ("star",)


class BookVariantSerializer(ModelSerializer):
    class Meta:
        model = BookVariant
        fields = ("name",)


class FashionSizeSerializer(ModelSerializer):
    class Meta:
        model = FashionSize
        fields = ("name", "code")
        extra_kwargs = {"name": {"write_only": True}}


class SpeakerTypeSerializer(ModelSerializer):
    class Meta:
        model = SpeakerType
        fields = ("name",)


class RefrigeratorTypeSerializer(ModelSerializer):
    class Meta:
        model = RefrigeratorType
        fields = ("name",)


class ACTypeSerializer(ModelSerializer):
    class Meta:
        model = ACType
        fields = ("name",)


class WashingMethodSerializer(ModelSerializer):
    class Meta:
        model = WashingMethod
        fields = ("name",)


class ScreenTypeSerializer(ModelSerializer):
    class Meta:
        model = ScreenType
        fields = ("name",)


class SimTypeSerializer(ModelSerializer):
    class Meta:
        model = SimType
        fields = ("name",)


class OperatingSystemSerializer(ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = ("name",)


class ProductSeriesSerializer(ModelSerializer):
    class Meta:
        model = ProductSeries
        fields = ("name",)


class DisplayTypeSerializer(ModelSerializer):
    class Meta:
        model = DisplayType
        fields = ("name",)


class MobileFeatureSerializer(ModelSerializer):
    display_type = DisplayTypeSerializer()
    sim_type = SimTypeSerializer()
    os = OperatingSystemSerializer()
    series = ProductSeriesSerializer()

    class Meta:
        model = ProductMobileFeatures
        fields = (
            "display_size",
            "display_type",
            "resolution",
            "sim_type",
            "touchscreen",
            "smart_phone",
            "battery_capicity",
            "os",
            "ram",
            "series",
        )


class LaptopFeatureSerializer(ModelSerializer):
    display_type = DisplayTypeSerializer()
    series = ProductSeriesSerializer()
    os = OperatingSystemSerializer()

    class Meta:
        model = ProductLaptopFeatures
        fields = (
            "display_size",
            "display_type",
            "series",
            "os",
            "processor",
            "resolution",
            "battery_backup",
            "touchscreen",
        )


class TelevisionFeatureSerializer(ModelSerializer):
    series = ProductSeriesSerializer()
    screen_type = ScreenTypeSerializer()

    class Meta:
        model = ProductTelivisionFeatures
        fields = (
            "display_size",
            "series",
            "screen_type",
            "is_3d",
            "is_curved",
            "has_wifi",
            "usb_count",
            "refresh_rate",
            "includes_wallmount",
        )


class WashingMachineFeatureSerializer(ModelSerializer):
    washing_method = WashingMethodSerializer()

    class Meta:
        model = ProductWashingMachineFeatures
        fields = (
            "energy_rating",
            "washing_capicity",
            "washing_method",
            "has_inbuilt_heater",
        )


class AirConditionerFeatureSerializer(ModelSerializer):
    type = ACTypeSerializer()
    series = ProductSeriesSerializer()

    class Meta:
        model = ProductAirConditionerFeature
        fields = (
            "type",
            "compressor",
            "cooling_capacity",
            "series",
            "cooling_coverage_area",
        )


class RefrigeratorFeatureSerializer(ModelSerializer):
    type = RefrigeratorTypeSerializer()

    class Meta:
        model = ProductRefrigeratorFeature
        fields = (
            "capacity",
            "energy_rating",
            "compressor_type",
            "type",
            "stabilizer_required",
        )


class SpeakerFetaureSerializer(ModelSerializer):
    type = SpeakerTypeSerializer()

    class Meta:
        model = ProductSpeakersFeatures
        fields = ("power_output", "frequency_response", "has_bluetooth", "type")


class ProductWarrantySerializer(ModelSerializer):
    class Meta:
        model = ProductWarranty
        fields = ("summary", "covered", "not_covered")


class ProductSpecificationSerializer(ModelSerializer):
    laptop = LaptopFeatureSerializer()
    mobile = MobileFeatureSerializer()
    tv = TelevisionFeatureSerializer()
    washing_machine = WashingMachineFeatureSerializer()
    ac = AirConditionerFeatureSerializer()
    refrigerator = RefrigeratorFeatureSerializer()
    speaker = SpeakerFetaureSerializer()

    class Meta:
        model = ProductSpecification
        fields = (
            "in_box",
            "launched_date",
            "model_no",
            "model_name",
            "mobile",
            "laptop",
            "tv",
            "washing_machine",
            "ac",
            "refrigerator",
            "speaker",
        )


class ProductDetailSerializer(ModelSerializer):
    brand = BrandSerializer()
    seller = SellerUserSerializer()
    subcategory = ProductSubcategorySerializer()
    warranty = ProductWarranty()
    specification = ProductSpecification()

    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "name",
            "slug",
            "seller",
            "subcategory",
            "description",
            "overall_rating",
            "replacement_days",
            "warranty",
            "weight",
            "specification",
        )
        read_only_fields = ("uuid", "slug")


class ProductImageSerializer(ModelSerializer):
    image = ImageField(required=True, allow_empty_file=False)

    class Meta:
        model = ProductImages
        fields = ("image", "primary")



class ProductVariationDetailSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True)
    product = ProductDetailSerializer()
    discount = SerializerMethodField(method_name="calculate_discount")
    color = ProductColorSerializere()
    mobile_variant = MobileVariantSerializer()
    laptop_variant = LaptopVariantSerializer()
    tv_variant = TVVariantSerializer()
    ac_capacity_variant = ACCapacityVariantSerializer()
    ac_star_variant = ACStarRatingVariantSerializer()
    book_variation = BookVariantSerializer()
    size = FashionSizeSerializer()

    class Meta:
        model = ProductVariation
        fields = (
            "uuid",
            "pid",
            "product",
            "retail_price",
            "discount",
            "price",
            "color",
            "available_stock",
            "mobile_variant",
            "laptop_variant",
            "tv_variant",
            "ac_capacity_variant",
            "refrigerator_capacity",
            "ac_star_variant",
            "book_variation",
            "juices_quantity",
            "size",
            "images",
        )
        read_only_fields = ("pid", "uuid", "discount")

    def calculate_discount(self, obj):

        return round((100 - (obj.price * 100 / obj.retail_price)), 2)



# Base Serializers
class ProductBaseSerializer(ModelSerializer):
    subcategory = ProductSubcategoryBase(   )
    class Meta:
        model = Product
        fields = ("uuid", "subcategory", "name", "slug", "overall_rating")
        read_only_fields = ("uuid", "slug")


class ProductVariationBaseSerializer(ProductVariationDetailSerializer):
    product = ProductBaseSerializer()




