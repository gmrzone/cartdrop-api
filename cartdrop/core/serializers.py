from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Brand, CategoryImage, ProductCategory, ProductSubcategory


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


class ProductSubcategorySerializer(ModelSerializer):

    # photo = ImageField(required=True, allow_empty_file=False)

    class Meta:
        model = ProductSubcategory
        fields = ("name", "category", "slug", "uuid", "created")
        extra_kwargs = {
            "created": {"read_only": True},
            "uuid": {"read_only": True},
            "slug": {"read_only": True},
        }
