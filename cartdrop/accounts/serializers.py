from django.contrib.auth.hashers import make_password
from django.forms import ValidationError
from rest_framework.serializers import CharField, ImageField, ModelSerializer

from .models import CartDropUser, SellerUser


class UserSerializer(ModelSerializer):
    photo = ImageField(required=False, allow_empty_file=True)
    confirm_password = CharField(required=True)

    class Meta:
        model = CartDropUser
        fields = (
            "number",
            "email",
            "username",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "photo",
        )

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]

        if password != confirm_password:
            raise ValidationError("Both password dont match please try again")
        else:
            return super().validate(attrs)


class SellerUserSerializer(ModelSerializer):
    photo = ImageField(required=False, allow_empty_file=True)

    class Meta:
        model = SellerUser
        fields = (
            "number",
            "email",
            "username",
            "first_name",
            "last_name",
            "photo",
        )
