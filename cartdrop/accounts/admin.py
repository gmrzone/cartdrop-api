from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CartDropUser, UserAddress

# Register your models here.


USERNAME_FIELD = get_user_model().USERNAME_FIELD
REQUIRED_FIELDS = (USERNAME_FIELD,) + tuple(get_user_model().REQUIRED_FIELDS)
BASE_FIELDS = (
    "Base Fields",
    {
        "fields": REQUIRED_FIELDS + ("password",),
    },
)
SIMPLE_PERMISSION_FIELDS = (
    _("Permissions"),
    {
        "fields": (
            "is_active",
            "is_staff",
            "is_superuser",
            "is_email_verified",
            "is_number_verified",
            "is_disabled",
        ),
    },
)

ADVANCE_PERMISSION_FIELDS = (
    _("Advance Permission"),
    {"fields": ("groups", "user_permissions")},
)


class CartDropUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form_template = None
    add_form = UserCreationForm
    form = UserChangeForm

    model = CartDropUser
    list_display = (
        "username",
        "email",
        "number",
        "is_active",
        "is_email_verified",
        "is_number_verified",
    )
    list_display_links = (USERNAME_FIELD,)
    list_filter = (
        "is_active",
        "is_email_verified",
        "is_number_verified",
        "is_disabled",
        "is_superuser",
        "is_staff",
    )
    readonly_fields = ("last_login", "date_joined")
    search_fields = (USERNAME_FIELD, "number", "email")
    ordering = None

    fieldsets = (
        BASE_FIELDS,
        (
            _("Extra fields"),
            {"fields": ("first_name", "last_name", "photo", "type")},
        ),
        SIMPLE_PERMISSION_FIELDS,
        ADVANCE_PERMISSION_FIELDS,
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": REQUIRED_FIELDS
                + (
                    "password1",
                    "password2",
                ),
            },
        ),
    )


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "pincode", "is_primary")
    list_filter = ("is_primary",)
    search_fields = ("address_1", "address_2", "city", "state", "pincode")
    list_select_related = ("user",)


admin.site.register(CartDropUser, CartDropUserAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
