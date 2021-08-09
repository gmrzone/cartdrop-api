from rest_framework import serializers
from rest_framework.fields import ImageField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import CategoryImage, ProductCategory, ProductSubcategory


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

    photo = ImageField(required=True, allow_empty_file=False)

    class Meta:
        models = ProductSubcategory
        fields = ("name", "category", "slug", "uuid", "photo", "created")
        extra_kwargs = {
            "created": {"read_only": True},
            "uuid": {"read_only": True},
            "slug": {"read_only": True},
        }
