from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .validators import number_validator
from cartdrop.core.behaviours import Timestamps, UUIDField

from .managers import CartDropUserManager
from .utils import user_photo_location
from .validators import number_validator, pincode_validator
from .fields import LowerCaseCharField, LowerCaseEmailField

# Create your models here.


class CartDropUser(AbstractBaseUser, PermissionsMixin):
    class UserTypes(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        SELLER = "SELLER", "Seller"

    username_validators = UnicodeUsernameValidator()
    number = models.CharField(
        _("Mobile Number"),
        max_length=10,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
        validators=[number_validator],
        error_messages={
            "unique": _(
                "This number is already registered with us please try logging in"
            )
        },
    )
    email = LowerCaseEmailField(
        _("Email address"),
        max_length=50,
        unique=True,
        db_index=True,
        error_messages={"unique": _("A user with this email already exist")},
    )
    username = LowerCaseCharField(
        _("Username"),
        max_length=50,
        db_index=True,
        unique=True,
        validators=[username_validators],
        error_messages={"unique": _("A user with that username already exist")},
        help_text=_(
            "Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    type = models.CharField(
        _("user type"),
        max_length=100,
        db_index=True,
        default=UserTypes.CUSTOMER,
        choices=UserTypes.choices,
    )
    first_name = models.CharField(_("first name"), max_length=25, blank=True)
    last_name = models.CharField(_("last name"), max_length=25, blank=True)
    date_joined = models.DateTimeField(_("date_joined"), default=timezone.now)
    photo = models.ImageField(
        _("profile picture"),
        upload_to=user_photo_location,
        default="default_profilepic.png",
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin panel."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "set this to false this instead of deleting accounts."
        ),
    )
    is_email_verified = models.BooleanField(
        _("email verified"),
        default=False,
        help_text="Designates whether the user has verified their email",
    )
    is_number_verified = models.BooleanField(
        _("number verified"),
        default=False,
        help_text="Designates whether the user has verified their number",
    )
    is_disabled = models.BooleanField(
        _("disabled"),
        default=False,
        help_text="Designates whether the user account has been disabled",
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "number"]

    objects = CartDropUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        fullname = "{0:s} {1:s}".format(self.first_name, self.last_name)
        return fullname

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[self.email],
            **kwargs
        )

    def __Str__(self):
        return self.username


class SellerUserManager(CartDropUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=CartDropUser.UserTypes.SELLER)


class SellerUser(CartDropUser):

    objects = SellerUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.type = self.UserTypes.SELLER
        return super().save(*args, **kwargs)


class UserAddress(UUIDField, Timestamps):
    class StateChoises(models.TextChoices):
        KA = "KA", "Karnataka"
        AP = "AP", "Andhra Pradesh"
        KL = "KL", "Kerala"
        TN = "TN", "Tamil Nadu"
        MH = "MH", "Maharashtra"
        UP = "UP", "Uttar Pradesh"
        GA = "GA", "Goa"
        GJ = "GJ", "Gujarat"
        RJ = "RJ", "Rajasthan"
        HP = "HP", "Himachal Pradesh"
        TG = "TG", "Telangana"
        AR = "AR", "Arunachal Pradesh"
        AS = "AS", "Assam"
        BR = "BR", "Bihar"
        CT = "CT", "Chhattisgarh"
        HR = "HR", "Haryana"
        JH = "JH", "Jharkhand"
        MP = "MP", "Madhya Pradesh"
        MN = "MN", "Manipur"
        ML = "ML", "Meghalaya"
        MZ = "MZ", "Mizoram"
        NL = "NL", "Nagaland"
        OR = "OR", "Odisha"
        PB = "PB", "Punjab"
        SK = "SK", "Sikkim"
        TR = "TR", "Tripura"
        UT = "UT", "Uttarakhand"
        WB = "WB", "West Bengal"

    user = models.ForeignKey(
        CartDropUser, on_delete=models.CASCADE, related_name="addresses"
    )
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100, choices=StateChoises.choices, default=StateChoises.MH
    )
    pincode = models.CharField(max_length=6, null=True, validators=[pincode_validator])
    is_primary = models.BooleanField(default=False)
