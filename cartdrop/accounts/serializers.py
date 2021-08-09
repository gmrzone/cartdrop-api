from rest_framework.serializers import ModelSerializer, ImageField
from .models import CartDropUser, SellerUser


class UserSerializer(ModelSerializer):
    photo = ImageField(required=False, allow_empty_file=True)
    class Meta:
        model = CartDropUser
        fields = ('number', 'email', 'username', 'first_name', 'last_name', "photo", "type", "is_email_verified")


class SellerUserSerializer(ModelSerializer):
    photo = ImageField(required=False, allow_empty_file=True)
    class Meta:
        model = SellerUser
        fields = ('number', 'email', 'username', 'first_name', 'last_name', "photo", "type", "is_email_verified")