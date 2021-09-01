from django.db.models import Max
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ImageField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Brand, CategoryImage, ProductCategory, ProductSubcategory, SubcategoryImage, CouponCode


class BrandSerializer(ModelSerializer):
    photo = ImageField(required=True, allow_empty_file=False)

    class Meta:
        model = Brand
        fields = ("name", "photo")


class CategoryImageSerializer(ModelSerializer):
    image = ImageField(required=True, allow_empty_file=False)

    class Meta:
        model = CategoryImage
        fields = ("image",)


class ProductCategorySerializer(ModelSerializer):

    category_images = CategoryImageSerializer(many=True)

    class Meta:
        model = ProductCategory
        fields = ("name", "slug", "uuid", "category_images", "created")
        extra_kwargs = {
            "created": {"read_only": True},
            "uuid": {"read_only": True},
            "slug": {"read_only": True},
        }


class SubcategoryImageSerializer(ModelSerializer):
    image = ImageField(required=True, allow_empty_file=False)
    class Meta:
        model = SubcategoryImage
        fields = ("image",)


class CouponSerializerBase(ModelSerializer):
    class Meta:
        model = CouponCode
        fields = ("code", "discount")

class ProductSubcategorySerializer(ModelSerializer):

    subcategory_images = SubcategoryImageSerializer(many=True)
    coupons = CouponSerializerBase(many=True)
    class Meta:
        model = ProductSubcategory
        fields = ("name", "slug", "uuid", "subcategory_images", "coupons")
        extra_kwargs = {
            "uuid": {"read_only": True},
            "slug": {"read_only": True},
        }



class ProductSubcategoryBase(ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = ("name",  "slug")
        extra_kwargs = {
            "slug": {"read_only": True},
        } 
