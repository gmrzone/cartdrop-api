from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from .models import ProductCategory, ProductSubcategory


class ProductCategorySerializer(ModelSerializer):

    
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
