from accounts.serializers import SellerUserSerializer
from core.serializers import BrandSerializer, ProductSubcategorySerializer
from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from .models import (Product, ProductSpecification, ProductVariation,
                     ProductWarranty)


class ProductWarrantySerializer(ModelSerializer):
    class Meta:
        models = ProductWarranty
        fields = ("summary", "covered", "not_covered")


class ProductSpecificationSerializer(ModelSerializer):
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


class ProductVariationSerializer(ModelSerializer):
    brand = BrandSerializer(many=False)
    seller = SellerUserSerializer(many=False)
    subcategory = ProductSubcategorySerializer(many=False)
    warranty = ProductWarranty(many=False)
    specification = ProductSpecification(many=False)

    class Meta:
        model = Product
        fields = (
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


class ProductVariationSerializer(ModelSerializer):

    product = ProductVariationSerializer(many=False)

    class Meta:
        model = ProductVariation
        fields = (
            "PID",
            "product",
            "retail_price",
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
