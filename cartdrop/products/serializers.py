from accounts.serializers import SellerUserSerializer
from core.serializers import BrandSerializer, ProductSubcategorySerializer
from django.db import models
from django.db.models import fields
from django.db.models.fields.files import ImageField
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

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
        fields = ("name",)


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
        fields = ("name",)


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
    display_type = DisplayTypeSerializer(many=False)
    sim_type = SimTypeSerializer(many=False)
    os = OperatingSystemSerializer(many=False)
    series = ProductSeriesSerializer(many=False)

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
    display_type = DisplayTypeSerializer(many=False)
    series = ProductSeriesSerializer(many=False)
    os = OperatingSystemSerializer(many=False)

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
    series = ProductSeriesSerializer(many=False)
    screen_type = ScreenTypeSerializer(many=False)

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
    washing_method = WashingMethodSerializer(many=False)

    class Meta:
        model = ProductWashingMachineFeatures
        fields = (
            "energy_rating",
            "washing_capicity",
            "washing_method",
            "has_inbuilt_heater",
        )


class AirConditionerFeatureSerializer(ModelSerializer):
    type = ACTypeSerializer(many=False)
    series = ProductSeriesSerializer(many=False)

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
    type = RefrigeratorTypeSerializer(many=False)

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
    type = SpeakerTypeSerializer(many=False)

    class Meta:
        model = ProductSpeakersFeatures
        fields = ("power_output", "frequency_response", "has_bluetooth", "type")


class ProductWarrantySerializer(ModelSerializer):
    class Meta:
        model = ProductWarranty
        fields = ("summary", "covered", "not_covered")


class ProductSpecificationSerializer(ModelSerializer):
    laptop = LaptopFeatureSerializer(many=False)
    mobile = MobileFeatureSerializer(many=False)
    tv = TelevisionFeatureSerializer(many=False)
    washing_machine = WashingMachineFeatureSerializer(many=False)
    ac = AirConditionerFeatureSerializer(many=False)
    refrigerator = RefrigeratorFeatureSerializer(many=False)
    speaker = SpeakerFetaureSerializer(many=False)

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


class ProductSerializer(ModelSerializer):
    brand = BrandSerializer(many=False)
    seller = SellerUserSerializer(many=False)
    subcategory = ProductSubcategorySerializer(many=False)
    warranty = ProductWarranty(many=False)
    specification = ProductSpecification(many=False)

    class Meta:
        model = Product
        fields = (
            "uuid" "brand",
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
        fields = ("image_summary", "image", "primary")
        read_only_fields = ("image_summary",)


class ProductVariationSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True)
    product = ProductSerializer(many=False)
    discount = SerializerMethodField(method_name="calculate_discount")
    color = ProductColorSerializere(many=False)
    mobile_variant = MobileVariantSerializer(many=False)
    laptop_variant = LaptopVariantSerializer(many=False)
    tv_variant = TVVariantSerializer(many=False)
    ac_capacity_variant = ACCapacityVariantSerializer(many=False)
    ac_star_variant = ACStarRatingVariantSerializer(many=False)
    book_variation = BookVariantSerializer(many=False)
    size = FashionSizeSerializer()

    class Meta:
        model = ProductVariation
        fields = (
            "uuid" "PID",
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
        read_only_fields = ("PID", "uuid", "discount")

    def calculate_discount(self, obj):

        return round((100 - (self.price * 100 / self.retail_price)), 2)
